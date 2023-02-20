#!/bin/sh

nitrogen --restore 
# wal -i Downloads/wallpapers
nm-applet &

ibus-daemon &

#blueman-applet &
xcape -e "Super_L=Super_L|Control_L|b" &
picom -b &

exit 0
