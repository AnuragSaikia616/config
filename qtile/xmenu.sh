#!/bin/sh

xmenu <<EOF | sh &
IMG:/home/anurag/.config/qtile/icons/files.png	File_manager	(pcmanfm) 
IMG:/home/anurag/.config/qtile/icons/programming.png	Programming
	VScode	code
	Pycharm	pycharm	
	Rstudio	rstudio
	Jupyter	(jupyter notebook)
	Emacs	emacs
	Neo-vim	(alacritty -e nvim)
IMG:/home/anurag/.config/qtile/icons/spotify.png	Spotify		spotify-tray
IMG:/home/anurag/.config/qtile/icons/terminals.png	Terminal 	alacritty 
IMG:/home/anurag/.config/qtile/icons/screenshot.png	Screenshot 	(scrot -d 0)
IMG:/home/anurag/.config/qtile/icons/nightlight.png	Night Light 
	IMG:/home/anurag/.config/qtile/icons/nightlight_on.png	ON (5500k)	(redshift -P -O 5500k)
	IMG:/home/anurag/.config/qtile/icons/nightlight_off.png	OFF (6500k)	(redshift -P -O 6500k)
IMG:/home/anurag/.config/qtile/icons/appr.png	Customize 	lxappearance
EOF
