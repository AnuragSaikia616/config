#!/bin/bash


echo "Installing packages..."

yay -S qtile qtile-extras-git xmenu alacritty picom librewolf chromium rofi rofi-calc rofi-bluetooth-git redshift-git xcape-git conky-git emacs  

pip install pywal

mkdir qtile_backup

mv ~/.config/qtile/* qtile_backup/

cp * ~/.config/qtile/
