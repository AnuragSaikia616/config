#!/bin/sh

nitrogen --restore 

nm-applet &

ibus-daemon &

xcape -e "Super_L=Super_L|Control_L|b"&

picom --config .config/qtile/picom/picom.conf &

conky -c .config/qtile/conky/conky-computer-metrics &


exit 0
