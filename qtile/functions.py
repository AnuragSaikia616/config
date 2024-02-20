'''
░█▀▀░█░▒█░█▀▀▄░█▀▄░▀█▀░░▀░░▄▀▀▄░█▀▀▄░█▀▀
░█▀░░█░▒█░█░▒█░█░░░░█░░░█▀░█░░█░█░▒█░▀▀▄
░▀░░░░▀▀▀░▀░░▀░▀▀▀░░▀░░▀▀▀░░▀▀░░▀░░▀░▀▀▀
'''
from libqtile.lazy import lazy
from libqtile import qtile
import subprocess
import os
from rofi import Rofi
import random
import json

# Rofi configuration files
rofi_panel = Rofi(rofi_args=['-theme', '~/.config/qtile/rofi_main.rasi'])
# rofi_panel = Rofi(rofi_args=['-theme', '~/.config/rofi/config.rasi'])



# Function to Minimize windows:
@lazy.function
def hide_windows(qtile):
    for win in qtile.current_group.windows:
        win.toggle_minimize()

# Control panel
@lazy.function
def control_panel(qtile):
    
    options = ['󰖩 wifi',' bluetooth',' calculator','󱩌 night light','󰸉 wallpaper','󱪰 lockscreen BG','󱣴 screenshot', '󰜉 Restart', '⭘ Poweroff', ' Lock']
    index, key = rofi_panel.select(prompt='System', options=options)
    rofi_panel
    if index == 0:
        os.system("rofi-wifi-menu")
    elif index == 1:
        os.system("rofi-bluetooth -c .config/qtile/rofi_panel.rasi")
    elif index == 2:
        os.system('rofi -show calc')
    elif index == 3:
        nl.toggle()
    elif index == 4:
        # os.system('./.config/qtile/setwal_script.sh')waterfox
        os.system('wal -i Downloads/wallpapers/')
        qtile.reload_config()
    elif index == 5:
        os.system('betterlockscreen -u .config/qtile/cache/background.jpg --fx pixel')
        os.system('dunstify "Betterlockscreen" "Lockscreen background set"')
    elif index==6:
        os.system('rofi-screenshot')
    elif index == 7:
        os.system("reboot")
    elif index == 8:
        os.system("poweroff")
    elif index == 9:
        os.system("betterlockscreen -l pixel")
        
# Night Light
class nightLight:
    def __init__(self):
        self.isNight = False
    def toggle(self):
        if self.isNight == False:
            os.system("redshift -P -O 3000k")
            self.isNight = True
        elif self.isNight == True:
            os.system("redshift -P -O 6500k")
            self.isNight = False
nl = nightLight()

# PyWal colors from cache   
with open('.cache/wal/colors.json') as imp_colors:
    data = json.load(imp_colors) 
    col = list(data['colors'].values())
    def get_colors():
        return [*col]


# This function grows and shrinks the current window while maintaining its center
@lazy.function
def resize_FW(qtile,width=0,height=0,expand=False):
    win = qtile.current_window
    x, y = win.cmd_get_position()
    win.cmd_resize_floating(width,height)
    if expand:
        win.cmd_set_position_floating(x-(width/2),y-(height/2))

@lazy.function
def move_FW(qtile,x,y):
    win = qtile.current_window
    curr_x, curr_y = win.cmd_get_position()
    win.cmd_set_position_floating(curr_x+x,curr_y+y)

@lazy.function
def commit_push(qtile):
    os.system("cd ~/.config/ && git add qtile && git commit -m 'Fly commit' && git push origin master")
