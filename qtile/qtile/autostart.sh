#!/bin/sh

# Autostart these programs on qtile start

# nitrogen --restore
wal -R
ibus-daemon &
nm-applet &
# xcape -e "Super_L=Super_L|Control_L|b" &
picom --config .config/qtile/picom/picom.conf -b
# conky -c .config/qtile/conky/conky_date_time.conf
# conky -c .config/qtile/conky/conky_mat.conf

exit 0
