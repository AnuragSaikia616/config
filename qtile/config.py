'''
░▒█▀▀█░▀▀█▀▀░▀█▀░▒█░░░░▒█▀▀▀
░▒█░▒█░░▒█░░░▒█░░▒█░░░░▒█▀▀▀
░░▀▀█▄░░▒█░░░▄█▄░▒█▄▄█░▒█▄▄▄
'''
import os
import subprocess
from libqtile import bar, layout, hook
from libqtile.config import Group, Match, hook, Screen, ScratchPad, DropDown
# from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from libqtile import extension
from qtile_extras import widget
from keybindings import *
from spotify import Spotify

default_font = "Jetbrainsmono Nerd Font"
default_fontsize = 20
bar_opacity = 0
bar_thickness = 35
colors = get_colors()
foreground="#000"
background="#fff"
bar_color=colors[0] + "ff"
# COLORS 
# colors = {0:"#121212",2:"#ffffff",3:"#ffffff",7:"#ffffff",8:"#666666"}

# WIDGETS

def get_widgets():
    w = [
        widget.TextBox(
            text="#",
            fontsize=27,
            foreground=colors[0],
            background=colors[3],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun -config ~/.config/qtile/rofi_main.rasi -show-icons")}
        ),

                widget.GroupBox(
                    padding=12,
                    borderwidth=3,
                    # spacing=15,
                    rounded=False,
                    highlight_method='line',
                    active="#090",
                    block_highlight_text_color=colors[7],
                    highlight_color=colors[0],
                    inactive="#444444",
                    # inactive = colors['black'],
                    foreground=colors[7],
                    # background=colors['black'],
                    this_current_screen_border=colors[0],
                    this_screen_border=colors[7],
                    other_current_screen_border='#fff',
                    other_screen_border='#fff',
                    urgent_border='#fff',
                    disable_drag=True,
                    hide_unused=False,
                ),


                # widget.WindowName(),

                # widget.Spacer(length=30),
                widget.TaskList(
                    border=colors[1],
                    foreground=colors[7],
                    unfocused_border='#222',
                    # max_title_width=400,
                    highlight_method='block',
                    title_width_method='uniform',
                    rounded=False,
                    font="Jetbrainsmono nerd font",
                    margin=0,
                    padding=4,
                    borderwidth=1,
                ),

                # Spotify(
                #     foreground=colors[7],
                #     font="Jetbrainsmono nerd font",
                #     format="{icon} {artist} - {track}",
                #     # format="{icon} {track}",
                #     width=250,
                #     scroll=True,
                #     scroll_interval=0.02,
                # ),


                widget.Spacer(length=10),

                # widget.CPU(
                #     format='  {load_percent}%'
                #         ),
                # widget.Spacer(length=10),

                widget.Systray(icon_size = 33,
                               background=colors[5],),
                widget.Wlan(
                    format = " {percent:2.0%}",
                    mouse_callbacks = {'Button1': lazy.spawn("alacritty -e nmtui")},
                    foreground=colors[0],
                    background=colors[5],
                ),

                widget.Spacer(length=10,),


                widget.Battery(
                    format="{char} {percent:2.0%} {hour:d}:{min:02d}",
                    charge_char="󱐋",
                    discharge_char="󰁹",
                    update_interval=5,
                    low_percentage=0.20,
                    low_foreground="#000",
                    low_background="#f55",
                    foreground="#000",
                    background="#7a5"
        ),
                widget.Spacer(length=10),
                widget.TextBox(
                    text=" ",
                    # font="Font Awesome 6 Free Solid",
                    padding=5,
                    foreground=colors[0],
                    background=colors[12],
                ),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    format = "{percent:2.0%}",
                    foreground=colors[0],
                background=colors[12]
                ),

                widget.Spacer(length=10),

                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    padding=5,
                    foreground=colors[0],
                    background=colors[6],
                ),
                widget.Volume(
                    foreground=colors[0],
                    background=colors[6],
                    fmt=" {} ",
                    padding=0,
                ),
                widget.Spacer(length=10),
        widget.Clock(
                    # format='%I:%M %p',
                    format='%b-%d | %I:%M %p ',
                    foreground=colors[0],
                    background=colors[8],
                    margin=3,
                    padding=5,
                    # format='%a %d-%m-%y ',
                    # foreground=colors['white'],
                    # background=colors[0],
        ),

    ]
    return w

# BAR

screens = [

    Screen(
        bottom=bar.Bar(
            get_widgets(),
            bar_thickness,
            # margin=[0, 10, 5, 10],
            background=bar_color,
            # opacity=bar_opacity,
            # margin=[5,5,0,5],
            border_width=[5,5,5,5],
            border_color=[colors[0],colors[0],colors[0],colors[0]],
        ),
    ),

]



# GROUPS

groups = [Group(f"{i}", label=i) for i in range(1, 8)]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
        ]
    )
scratch = terminal
groups.append(ScratchPad(
    "scratchpad", [DropDown("term", scratch,on_focus_lost_hide=False,width=0.5, height=0.5, x=0.25, y=0.01, opacity=1),
                   DropDown("files", filebrowser,on_focus_lost_hide=False, width=0.8, height=0.8, x=0.1, y=0.0, opacity=1),
                   DropDown("chatgpt", "chromium --app=https://chat.openai.com",width=0.6,height=0.6,on_focus_lost_hide=False,x=0.2,y=0.01,opacity=1),
                   ]))




# LAYOUT

layouts = [

    layout.Columns(
                   margin=0,
                   border_focus=colors[3],
                   border_normal='#000',
                   border_width=3
                   ),
    layout.Max(
        border_focus=colors[7],
               border_normal='#000',
               # margin=_margin,
               border_width=0,
               ),
]

floating_layout = layout.Floating(
    border_focus='#0a0',
    border_normal='#000',
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)




# DEFAULTS for widgets
widget_defaults = dict(
    font = default_font,
    fontsize = default_fontsize,
    foreground = colors[7]
)
extension_defaults = [widget_defaults.copy()]


# Keys
keys = init_keys()
# Mouse
mouse = init_mouse()


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False




@ hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"
