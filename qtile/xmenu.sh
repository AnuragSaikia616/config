#!/bin/sh

xmenu <<EOF | sh &
IMG:/home/anurag/.config/qtile/icons/chrome2.png	Browser	(google-chrome-stable) 
IMG:/home/anurag/.config/qtile/icons/files.png	File_manager	(pcmanfm) 
IMG:/home/anurag/.config/qtile/icons/programming.png	Programming
	VScode	code
	Pycharm	pycharm	
	Rstudio	rstudio
	Jupyter	(jupyter notebook)
	Emacs	emacs
	Neo-vim	(kitty --config=.config/qtile/kitty/kitty.conf nvim)
IMG:/home/anurag/.config/qtile/icons/spotify.png	Spotify		spotify-tray
IMG:/home/anurag/.config/qtile/icons/terminals.png	Terminal 
	Kitty	(kitty)
	Alacritty	alacritty
IMG:/home/anurag/.config/qtile/icons/screenshot.png	Screenshot 	(scrot -d 0)
IMG:/home/anurag/.config/qtile/icons/appr.png	Customize 	lxappearance
EOF
