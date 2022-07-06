import json
import requests
from datetime import datetime
import getpass
import random
import ctypes
import platform
import subprocess

username = getpass.getuser()  # Get Username for Main Path
main_dir = 'C:\\Users\\' + username + '\\AppData\\Roaming\\AutoHomeWallpaper\\'
url = open(main_dir + 'url.txt', 'r').read() # Read url from url.txt


def log(text): #define log function
    """Log text to file."""
    now = datetime.now()
    dt_string = now.strftime("%d.%m.%Y %H:%M:%S") # get current date and time

    logtext = dt_string + ': ' + text
    with open(main_dir + 'ath-wp.log', 'a') as file: # open log file and write text
        file.write(logtext + '\n')
        print(logtext) # print log text to console
    return
def download(url, subdir, filename): # define download function
    """Download file from url and save it to subdir/filename."""
    if filename == '': # if filename is empty use Filename from url
        filename = url.rsplit('/', 1)[1]
        rootfilename = ''
    else:
        filename = filename # use filename from parameter
        rootfilename = url.rsplit('/', 1)[1]

    if subdir == 'root': # if subdir is root use root directory
        directory = main_dir
    else:
        directory = main_dir + subdir + '\\' # else use subdir from parameter

    r = requests.get(url, allow_redirects=True) # download file from url
    open(directory + filename, 'wb').write(r.content) # save file to subdir/filename
    log('Downloaded: ' + filename + rootfilename)
    return filename
def ping(): # define ping function for checking internet connection
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', '1.1.1.1']
    return subprocess.call(command) == 0
log('Started')


if ping() == False: # check internet connection
    log('No internet connection')
    log('Exiting') # if false exit without changing wallpaper
    exit()
if ping() == True:
    log('Internet connection found')
    jsonfilename = download(url, 'root', '') # if true download json library file


library = str(main_dir) + str(jsonfilename) # generate library path
log('Using Library: ' + library)

with open(library, ) as f: # open library file
    source = f.read()


check = 'not checked'
raw_data = json.loads(source) # load json library file
data = json.dumps(raw_data, indent=4, sort_keys=True) # convert json library file to python dictionary
picture_dict = dict() # create empty dictionary for pictures
count_len = len(raw_data['pictures']) # get length of Library to check it with its value

for item in raw_data['meta']:
    count_meta = item['count'] # get count value from meta key in json library file

if count_len == count_meta:
    check = True # if count_len and count_meta are equal check is true
    log('Count Check: ' + str(check))
else:
    check = False # if count_len and count_meta are not equal check is false
    log('Count Check: ' + str(check))
    exit()

for item in raw_data['pictures']: # add library contents to dictionary
    id = item['id']
    url = item['url']
    picture_dict[id] = url


pic_url = random.choice(list(picture_dict.values())) # get random picture from dictionary
log('Random URL: ' + pic_url)

pic_path = main_dir + 'Wallpapers\\' + download(pic_url, 'Wallpapers', '') # download random picture and save it to Wallpapers directory
log('Using Picture: ' + pic_path)
ctypes.windll.user32.SystemParametersInfoW(20, 0, pic_path , 0) # set wallpaper to the random picture


