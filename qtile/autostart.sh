#!/bin/sh

nitrogen --restore 

nm-applet &

ibus-daemon &

#blueman-applet &

picom -b &

exit 0
