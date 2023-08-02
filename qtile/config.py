import os
from libqtile import hook
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Group, Match, hook, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from libqtile import extension
from qtile_extras import widget
from keybindings import *


default_font = "sourcecodepro"
default_fontsize = 18
bar_opacity = 0.6
bar_thickness = 35

# COLORS 
colors = dict(
    black="#000000",
    accent='#0f0',
    main='#121212',
    bg='#1a1b26',
    trans='#121212',
    blue='#00afff',
    green='#0b0',
    red='#fa2573',
    yellow='#fabd2f',
    white='#ced1d4',
    purple='#ae81ff'
)


# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄
screens = [

    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    padding=0,
                    scale=0.5,
                ),

                widget.GroupBox(
                    padding=12,
                    borderwidth=5,
                    highlight_method='line',
                    active=colors['white'],
                    block_highlight_text_color=colors['black'],
                    highlight_color=colors['white'],
                    inactive='#666',
                    # inactive = colors['black'],
                    foreground=colors['white'],
                    # background=colors['black'],
                    this_current_screen_border=colors['black'],
                    this_screen_border=colors['white'],
                    other_current_screen_border='#fff',
                    other_screen_border='#fff',
                    urgent_border='#fff',
                    rounded=False,
                    disable_drag=True,
                ),

                widget.TaskList(
                    border=colors['white'],
                    foreground="#000",
                    unfocused_border="#666",
                    max_title_width=300,
                    highlight_method='block',
                    title_width_method='uniform',
                    rounded=False
                ),

                widget.Spacer(length=50),

                # widget.Systray(
                #     icon_size=32,
                #     # background=["#00000000", "#00000000", "#00000000"],
                #     padding=50,
                # ),

                widget.CheckUpdates(
                    mouse_callbacks = {'Button1': lazy.spawn(terminal+" sudo pacman -Syu")}    
                ),
                widget.Spacer(length=50),
                widget.TextBox(text = "󰖩",fontsize = 28),
                widget.Wlan(
                    format = "{percent:2.0%}", 
                    mouse_callbacks = {'Button1': lazy.spawn("rofi-wifi-menu")}
                ),
                widget.Spacer(length=50),
            
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    fontsize=default_fontsize+6,
                    padding=0,
                    # background=colors['black'],
                    mouse_callbacks={"Button1": lazy.spawn('pavucontrol')}
                ),
                widget.Volume(
                    foreground=colors["white"],
                    # background=colors['black']
                ),
                widget.Spacer(length=50),


                widget.UPowerWidget(
                    margin=0,
                    fill_charge='#0e0',
                    fill_low="#f00",
                    border_critical_colour='#f00',
                    border_charge_colour="#dbdbe0",
                    battery_height=16,
                    battery_width=40,
                    text_charging=' {percentage:.0f}% {ttf}',
                    text_discharging='{percentage:.0f}% {tte}',
                    text_displaytime=2,
                ),
               


                widget.Spacer(length=50),


                widget.Clock(
                    format=' %B-%d %I:%M %p ',
                    # format='%a %d-%m-%y ',
                    # foreground=colors['white'],
                    # background=colors['black'],
                    mouse_callbacks = {'Button1': control_panel()} 
                ),
            ],
            bar_thickness,
            # margin=[5, 5, 0, 5],
            background=colors['main'],
            opacity=bar_opacity
        ),
    ),
]


# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█

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
# ScratchPad
scratch = terminal
groups.append(ScratchPad(
    "scratchpad", [DropDown("term", scratch,
                            width=0.6, height=0.6, x=0.2, y=0.2, opacity=1),
                   DropDown("browser", "copyq",width=0.6,height=0.6,x=0.2,y=0.2,opacity=1),
                   ]))

###𝙇𝙖𝙮𝙤𝙪𝙩###
_margin = 0
layouts = [
    layout.Columns(margin=_margin, border_focus=colors['accent'],
                   border_normal='#111',
                   border_width=3
                   ),

    layout.Max(border_focus=colors['accent'],
               border_normal='#1F1D2E',
               margin=_margin,
               border_width=3,
               ),

    layout.Floating(
        border_normal='#ffffff',
        border_focus='#ffffff',
        margin=_margin,
        border_width=3,
    ),
    layout.Tile(border_focus=colors['accent'],
                border_normal='#1F1D2E',
                border_width=2,
                margin=_margin
                ),
]

floating_layout = layout.Floating(
    border_focus='#0f0',
    border_normal='#aaaaaa',
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
    fontsize = default_fontsize
)
extension_defaults = [widget_defaults.copy()]


# Keys
keys = init_keys()
# Mouse
mouse = init_mouse()


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
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
