#!/usr/bin/bash

BING_POTD=/usr/share/backgrounds/default.png
WALLPAPER_BLURRED=$HOME/.wallpaper_blurred.png

if [ -s $BING_POTD ]; then
	convert $BING_POTD -blur 10x10 $WALLPAPER_BLURRED
	feh --bg-fill $BING_POTD
fi

