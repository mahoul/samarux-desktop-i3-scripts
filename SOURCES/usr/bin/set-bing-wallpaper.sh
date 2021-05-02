#!/usr/bin/bash

BING_POTD=/usr/share/backgrounds/default.png

if [ -s $BING_POTD ]; then
	feh --bg-fill $BING_POTD
fi

