import json
from urllib.request import urlopen
import os
import sys
import time
import requests


#with urlopen('https://raw.githubusercontent.com/luca-alexander-thomas/AutoHome-Wallpaper/main/wallpaper.json') as response:
  #  source = response.read()

with open('wallpaper.json') as f:
    source = f.read()

url = 'https://raw.githubusercontent.com/luca-alexander-thomas/AutoHome-Wallpaper/main/wallpaper.json'
if url.find('/'):
    filename = url.rsplit('/', 1)[1]
    print(filename)
r = requests.get(url, allow_redirects=True)
open('bin/' + filename, 'wb').write(r.content)

check = 'not checked'
raw_data = json.loads(source)
data = json.dumps(raw_data, indent=4, sort_keys=True)
picture_dict = dict()
count_len = len(raw_data['pictures'])

for item in raw_data['meta']:
    count_meta = item['count']


if count_len == count_meta:
    check = True
    print(check)
else:
    check = False
    print(check)
    exit()



for item in raw_data['pictures']:
    id = item['id']
    url = item['url']
    picture_dict[id] = url


print(picture_dict['1'])


