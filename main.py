import json
import requests
from datetime import datetime
import getpass
import random
import ctypes
import os
import platform
import subprocess

username = getpass.getuser()
main_dir = 'C:\\Users\\'+ username +'\\AppData\\Roaming\\AutoHomeWallpaper\\'
subdirs = ['Wallpapers', 'Bin']
url = open(main_dir + 'url.txt', 'r').read()
def log(text):
    """Log text to file."""
    now = datetime.now()
    dt_string = now.strftime("%d.%m.%Y %H:%M:%S")

    logtext = dt_string + ': ' + text
    with open(main_dir + 'ath-wp.log', 'a') as f:
        f.write(logtext + '\n')
        print(logtext)
    return
def download(url):
    """Download file from url and save it to maindir/filename."""
    if url.find('/'):
       filename = url.rsplit('/', 1)[1]
    r = requests.get(url, allow_redirects=True)
    open(main_dir + filename, 'wb').write(r.content)
    log('Downloaded: ' + filename)
def down_load(url, subdir, filename):
    """Download file from url and save it to subdir/filename."""
    if url.find('/'):
        rootfilename = url.rsplit('/', 1)[1]
        root_filename = '  original: ' + rootfilename
    directory = main_dir + subdir + '\\'
    r = requests.get(url, allow_redirects=True)
    open(directory + filename, 'wb').write(r.content)
    log('Downloaded: ' + filename + root_filename)
def ping():
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


if ping() == False:
    log('No internet connection')
    log('Exiting')
    exit()
if ping() == True:
    log('Internet connection found')
    download(url)

with open(main_dir + 'wallpaper.json') as f:
    source = f.read()


check = 'not checked'
raw_data = json.loads(source)
data = json.dumps(raw_data, indent=4, sort_keys=True)
picture_dict = dict()
count_len = len(raw_data['pictures'])

for item in raw_data['meta']:
    count_meta = item['count']

if count_len == count_meta:
    check = True
    log('Count Check: ' + str(check))
else:
    check = False
    log('Count Check: ' + str(check))
    exit()

for item in raw_data['pictures']:
    id = item['id']
    url = item['url']
    picture_dict[id] = url


pic_url = random.choice(list(picture_dict.values()))
log('Random URL: ' + pic_url)
down_load(pic_url, 'Wallpapers', 'Wallpaper.jpg')
pic_path = main_dir + 'Wallpapers\\Wallpaper.jpg'
ctypes.windll.user32.SystemParametersInfoW(20, 0, pic_path , 0)


