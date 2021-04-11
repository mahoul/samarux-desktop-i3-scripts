#!/bin/bash

IMG_DATE=$(date +%d-%m-%Y)

[ -x /usr/bin/bing_wallpaper.py ] && /usr/bin/bing_wallpaper.py

WALLPAPER=$HOME/Pictures/bing/wallpaper.jpg
WALLPAPER_BLURRED=$HOME/Pictures/bing/wallpaper-blurred.jpg

find $HOME/Pictures -iname "bing*$IMG_DATE*" -exec cp -f {} $WALLPAPER \;
convert $WALLPAPER -blur 10x10 $WALLPAPER_BLURRED

feh --bg-fill $WALLPAPER

gsettings set org.gnome.desktop.screensaver picture-uri "file://$WALLPAPER_BLURRED"

