'''
░▒█░▄▀░█▀▀░█░░█░█▀▀▄░░▀░░█▀▀▄░█▀▄░░▀░░█▀▀▄░█▀▀▀░█▀▀
░▒█▀▄░░█▀▀░█▄▄█░█▀▀▄░░█▀░█░▒█░█░█░░█▀░█░▒█░█░▀▄░▀▀▄
░▒█░▒█░▀▀▀░▄▄▄▀░▀▀▀▀░▀▀▀░▀░░▀░▀▀░░▀▀▀░▀░░▀░▀▀▀▀░▀▀▀
'''
from libqtile.config import Key, KeyChord, Mouse, Drag, Click
from functions import *

# modifiers:
mod="mod4"
alt = "mod1"
shift = "shift"
# APPS
terminal = 'alacritty'
browser = "librewolf"
launcher = "rofi -config .config/qtile/rofi_main.rasi -show drun"


# Keyboard
keys = [
    # Switch groups
    Key([mod], "period", lazy.screen.next_group()),
    Key([mod], "comma", lazy.screen.prev_group()),


    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="change focus"),


    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),


    #Commands to GROW/SHRINK Windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),lazy.layout.shrink(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),lazy.layout.grow(), desc="Grow window up"),
    
    # To grow and shrink floating windows
    Key([alt,"control"],"x",resize_FW(30,30,expand=True)), 
    Key([alt,"control"],"z",resize_FW(-30,-30,expand=True)), 
    
    # To resize floating windows
    Key([alt,'control'],"l", resize_FW(40,0,expand=False)),
    Key([alt,'control'],"h", resize_FW(-40,0,expand=False)),
    Key([alt,'control'],"k", resize_FW(0,-40,expand=False)),
    Key([alt,'control'],"j", resize_FW(0,40,expand=False)),
    # To move floating windows
    Key([alt,"shift"],'l', move_FW(40,0)),
    Key([alt,"shift"],'h', move_FW(-40,0)),
    Key([alt,"shift"],'k', move_FW(0,-40)),
    Key([alt,"shift"],'j', move_FW(0,40)),
    # Center focused window
    Key([alt],"c",lazy.window.center()),

    #Focused window FULLSCREEN TOGGLE
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    
    
    #Focused window TOGGLE FLOATING
    Key([mod], "g", lazy.window.toggle_floating()),
    
    # Minimize all windows
    Key([mod, "shift"], "m", hide_windows()),
    
    #MINIMIZE focused window
    Key([mod], "m", lazy.window.toggle_minimize()),
    
    
    # multiple stack panes
    Key([mod, "shift"],"Return", lazy.layout.toggle_split(),),
   
    

    # Toggle E tween different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Volute and Brightness control
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn(
        "playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn(
        "brightnessctl s 5%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
        "brightnessctl s 5%-"), desc='brightness Down'),


   # Open programs
   KeyChord(
           [mod],"o",
           [
               Key([mod],"c", lazy.spawn('code')),
               Key([mod],"e",lazy.spawn('emacs')),
               Key([mod],"p",lazy.spawn('pycharm')),
               Key([mod],"s",lazy.spawn('spotify-tray')),
               Key([mod],"j",lazy.spawn('jupyter notebook')),
               ]
           ), 

    # Spawn rofi launcher
    Key([mod],'p',lazy.spawn(launcher)),

    # Run prompt
    Key([mod],'r',lazy.spawn("rofi -show run")),

    #Spotify Controls
    Key([mod],"right",lazy.spawn('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next')),
    Key([mod],"left",lazy.spawn('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous')),

    #Spawn rofi control panel
    Key([mod,'control'],"p",control_panel()),


    # Launch Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    # Open browser
    Key([mod], "b", lazy.spawn(browser)),
    
    # Open screenshot tool
    Key([mod], "s", lazy.spawn("rofi-screenshot"), desc='Screenshot'),
    
    # Lockscreen
    Key([mod], "Escape", lazy.spawn("betterlockscreen -l pixel")),

    # Terminal scratchpad
    Key([mod], "0", lazy.group['scratchpad'].dropdown_toggle('term'),),

    # Copyq(clipboard) scratchpad
    Key([mod], "9", lazy.group['scratchpad'].dropdown_toggle('browser'), desc="open scratchpad browser"),

    # Chatgpt scratchpad
    Key([mod], "8", lazy.group['scratchpad'].dropdown_toggle('chatgpt')),
    # Launch xmenu 
    Key([mod, "control"], "b", lazy.spawn("./.config/qtile/xmenu.sh")),
    
    # Launch system monitor
    Key([mod], "t", lazy.spawn("alacritty -e htop")),
    
    # Increase or Decrease focused window opacity
    Key([alt], "m", lazy.window.up_opacity()),
    Key([alt], "n", lazy.window.down_opacity()),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([alt], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    # Click([], "Button1", lazy.window.bring_to_front()),
    Click([mod], "Button1", lazy.window.bring_to_front())
]



# This function returns the keybindings to the main config.py file
def init_keys():
    return keys

# This function returns the muose bindings to the main config.py file
def init_mouse():
    return mouse
