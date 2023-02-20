#!/bin/sh

nitrogen --restore 

nm-applet &

ibus-daemon &
xcape -e "Super_L=Super_L|Control_L|b"&

#blueman-applet &

picom -b &

exit 0
