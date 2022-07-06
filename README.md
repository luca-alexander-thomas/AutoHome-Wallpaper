![GitHub all releases](https://img.shields.io/github/downloads/luca-alexander-thomas/autohome-wallpaper/total?logo=github&style=flat-square)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/luca-alexander-thomas/autohome-wallpaper?logo=github&style=flat-square)

# AutoHome-Wallpaper
AutoHome-Wallpaper is an open-source programme for automatically changing wallpapers based on a database. Similar to Bing Wallpaper, it uses online images that are loaded in advance.

## How to use?
Go to the Realeases Tab and Download the newest Release and execute the ```Install-AutoHome-Wallpaper.exe``` file.<br>
Now the AutoHome-Wallpaper Application runs on every login and changes your Wallpaper to an random one in the Library.<br><br>

#### Changing the Library
To Change the Library read the Dokument at [Librarys](https://github.com/luca-alexander-thomas/AutoHome-Wallpaper/tree/main/Libarys)

## How to run from source
To run the Python Script from Source you need to install following Python-Librarys using PYpip
```
pip install requests datetime
```
Make sure you have also the following Packages installed (normaly preinstalled)
```
json
getpass
random
ctypes
platform
subprocess
```
Now to run the following Directorys and files must be available:
```
"C:\Users\%USERNAME%\AppData\Roaming\AutoHomeWallpaper\url.txt"
```
In the ```url.txt``` File you write the URL of the Library in expample the Standart:
```
https://github.com/luca-alexander-thomas/AutoHome-Wallpaper/raw/main/Libarys/landscape.json
```
<br>

```
"C:\Users\%USERNAME%\AppData\Roaming\AutoHomeWallpaper\Wallpapers"
```
<br>
Now you can execute the ```main.py``` Script.

