#!/usr/bin/zsh
exec $(ls ~/Pictures/wallpapers/ | fzf --preview="feh --bg-fill ~/Pictures/wallpapers/{}")
