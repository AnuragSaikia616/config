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
rofi_panel = Rofi(rofi_args=['-theme', '~/.config/qtile/rofi_panel.rasi'])



# Function to Minimize windows:
@lazy.function
def hide_windows(qtile):
    for win in qtile.current_group.windows:
        win.toggle_minimize()

# Control panel
@lazy.function
def control_panel(qtile):
    
    options = ['󰖩 Wifi',' Bluetooth',' Calculator','󱩌 Night Light','󰸉 Pywal','󱪰 Lockscreen BG','󱣴 Screenshot', '󰜉 Restart', '⭘ Poweroff', ' Lock']
    index, key = rofi_panel.select(prompt='Control Panel ', options=options)
    rofi_panel
    if index == 0:
        os.system("alacritty -e nmtui")
    elif index == 1:
        os.system("rofi-bluetooth -c .config/qtile/rofi_panel.rasi")
    elif index == 2:
        os.system('rofi -show calc')
    elif index == 3:
        night_light()
    elif index == 4:
        os.system('./.config/qtile/setwal_script.sh')
        # os.system('wal -i Downloads/wallpapers/')
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
def night_light():
    options = ['ON (5000k)','Off (6500k)']
    index, key = rofi_panel.select(prompt='Night Light', options=options)

    if index == 0:
        os.system("redshift -P -O 5000k")
    elif index == 1:
        os.system("redshift -P -O 6500k")

# Piwal random wallpaper and betterlockscreen 
def wallpaper():
    home = 'Downloads/wallpapers/'
    wallpaper = random.choice(os.listdir(home))
    os.system('cp '+home+wallpaper+' .config/qtile/cache/background.jpg')
    os.system('dunstify "Piwal" "Wallpaper Changed!" -u normal')
    os.system('wal -i '+home+wallpaper)
    qtile.reload_config()
    # os.system('betterlockscreen -u '+home+wallpaper)
    # os.system('dunstify "BETTERLOCKSCREEN" "Lockscreen changed!"')
   
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