#!/usr/bin/env bash
set_wall() {
	# Wal sets wallpaper and genates new color scheme
	wal -i $WALLPAPER
	cp $WALLPAPER ~/.config/qtile/cache/background.jpg
	# betterlockscreen -u $WALLPAPER
	dunstify "Wallpaper" "Background set!" --timeout 2000
}

get_wall() {
	rofi -show file-browser-extended -theme ~/.config/qtile/rofi_setwal.rasi -file-browser-dir ~/Downloads/ -file-browser-stdout
}

WALLPAPER=$(get_wall)

if [ -z "$WALLPAPER" ]; then
	notify-send -a 'Piwal' "Wallpaper Not Selected"
else
	set_wall
fi
