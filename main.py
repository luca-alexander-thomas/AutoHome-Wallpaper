import json
from urllib.request import urlopen
import os
import sys
import time


with urlopen('https://raw.githubusercontent.com/luca-alexander-thomas/AutoHome-Wallpaper/main/wallpaper.json') as response:
    source = response.read()

raw_data = json.loads(source)
data = json.dumps(raw_data, indent=4, sort_keys=True)
print(data)

