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

default_font = "Monospace"
default_fontsize = 18
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
                # widget.TextBox(
                #     text="",
                #     fontsize=27,
                #     mouse_callbacks = {'Button1': commit_push()}
                # ),

                widget.TextBox(
                  foreground=colors[7],
                  # text = ' ',
                  text = ' ',
                  fontsize = 23,
                  mouse_callbacks = {'Button1': lazy.spawn("rofi -config .config/qtile/rofi_apps.rasi -show drun")}
                ),



                widget.GroupBox(
                    padding=12,
                    borderwidth=5,
                    highlight_method='line',
                    active="#090",
                    block_highlight_text_color=colors[2],
                    highlight_color="#00000000",
                    inactive=colors[7],
                    # inactive = colors['black'],
                    foreground=colors[7],
                    # background=colors['black'],
                    this_current_screen_border=bar_color,
                    this_screen_border=colors[7],
                    other_current_screen_border='#fff',
                    other_screen_border='#fff',
                    urgent_border='#fff',
                    rounded=False,
                    disable_drag=True,
                ),

                widget.CurrentLayoutIcon(
                    padding=0,
                    scale=0.5,
                    # foreground=colors[7]
                ),
                widget.TaskList(
                    border=colors[7],
                    foreground=colors[0],
                    unfocused_border='#888',
                    # max_title_width=300,
                    highlight_method='block',
                    title_width_method='uniform',
                    rounded=True,
                    # font = default_font+' Bold'
                ),

                Spotify(
                    foreground=colors[7],
                    format="{icon} {artist} - {track}"
                ),


                widget.Spacer(length=30),

                widget.CPU(
                    format='  {load_percent}%'
                        ),
                widget.Spacer(length=30),
                widget.TextBox(
                    text = "󰤨",
                    fontsize = 18,
                    foreground = colors[7],
               ),
                widget.Wlan(
                    format = "{percent:2.0%}",
                    mouse_callbacks = {'Button1': lazy.spawn("alacritty -e nmtui")},
                    foreground=colors[7],
                ),
                widget.Spacer(length=30),

                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    fontsize=18,
                    padding=0,
                    foreground=colors[7],
                    # background=colors['black'],
                    mouse_callbacks={"Button1": lazy.spawn('pavucontrol')}
                ),
                widget.Volume(
                    foreground=colors[7],
                    # background=colors['black']
                ),
                widget.Spacer(length=30),


                widget.UPowerWidget(
                    margin=0,
                    fill_charge='#0e0',
                    fill_low="#f00",
                    border_critical_colour='#f00',
                    border_charge_colour=colors[7],
                    fill_normal=colors[7],
                    border_colour=colors[7],
                    battery_height=14,
                    battery_width=30,
                    text_charging=' {percentage:.0f}% {ttf}',
                    text_discharging='{percentage:.0f}% {tte}',
                    text_displaytime=2,
                ),



                widget.Spacer(length=30),


                widget.Clock(
                    format='%I:%M %p',
                    # format=' %B-%d %I:%M %p ',
                    foreground=colors[7],
                    # format='%a %d-%m-%y ',
                    # foreground=colors['white'],
                    # background=colors[0],
                    mouse_callbacks = {'Button1': control_panel()}
                ),
                widget.Spacer(length=10),
                widget.Pomodoro(
                    prefix_inactive="󱎫",
                    fontsize=18,
                    color_inactive=colors[7],
                    length_pomodori=50,
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
            # opacity=bar_opacity
        ),
    ),
    Screen(
        bottom=bar.Bar(
            get_widgets(),
            bar_thickness,
            # margin=[0, 10, 5, 10],
            background=bar_color,
            # opacity=bar_opacity
        ),
    ),

]



# GROUPS

groups = [Group(f"{i}", label=i) for i in range(1, 6)]

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
    "scratchpad", [DropDown("term", scratch,
                            width=0.6, height=0.6, x=0.2, y=0.01, opacity=1),
                   DropDown("browser", "copyq",width=0.6,height=0.6,x=0.2,y=0.01,opacity=1),
                   DropDown("chatgpt", "chromium --app=https://chat.openai.com",width=0.6,height=0.6,x=0.2,y=0.01,opacity=1),
                   ]))




# LAYOUT

layouts = [

    layout.Columns(
                   margin=10,
                   border_focus=colors[7],
                   border_normal='#000',
                   border_width=3
                   ),
    layout.Floating(
        border_normal='#000',
        border_focus=colors[7],
        # margin=_margin,
        border_width=3,
    ),

    # layout.Max(
    #     border_focus=colors[7],
    #            border_normal='#000',
    #            # margin=_margin,
    #            border_width=0,
    #            ),


    # layout.MonadTall(
    #     border_focus=colors[7],
    #     ),
    # layout.Tile(border_focus=colors[2],
    #             border_normal='#000',
    #             border_width=2,
    #             # margin=_margin
    #             ),
]

floating_layout = layout.Floating(
    border_focus='#fff',
    border_normal='#000',
    border_width=3,
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
