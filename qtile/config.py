# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. import subprocess
import os
from libqtile import hook
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from qtile_extras import widget

mod = "mod4"
terminal = "kitty --config=.config/qtile/kitty/kitty.conf"
scratch = "kitty --config=.config/qtile/kitty/scratchpad_kitty.conf"
browser = "google-chrome-stable"
launcher = "rofi -show drun"
ranger = "kitty --config=.config/qtile/kitty/kitty.conf ranger"
_font = "Sourcecodepro"
# Function to hide all windows:


@lazy.function
def hide_windows(qtile):
    for win in qtile.current_group.windows:
        win.toggle_minimize()


# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch groups
    Key([mod], "period", lazy.screen.next_group()),
    Key([mod], "comma", lazy.screen.prev_group()),


    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "g", lazy.window.toggle_floating()),
    Key([mod], "m", lazy.window.toggle_minimize()),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle E tween different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "p", lazy.spawn(launcher),
        desc="Spawn a command using a prompt widget"),

    # CUSTOM
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
        "brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
        "brightnessctl s 10%-"), desc='brightness Down'),

    # Other stuff
    Key([mod], "e", lazy.spawn("emacs")),
    Key([mod], "n", lazy.spawn("nitrogen")),
    Key([mod, "shift"], "n", lazy.spawn(
        "/usr/bin/nitrogen --set-zoom-fill --random Downloads/wallpapers --save")),
    Key([mod], "b", lazy.spawn(browser)),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
    Key([mod], "r", lazy.spawn(ranger)),
    Key([mod], "c", lazy.spawn("code")),

    # PowerMenu
    Key([mod], "Escape", lazy.spawn(
        "rofi -show power-menu -modi power-menu:rofi-power-menu"
    )),

    Key([mod], "0", lazy.group['scratchpad'].dropdown_toggle(
        'term'), desc="Open Scratchpad terminal"),
    Key([mod], "9", lazy.group['scratchpad'].dropdown_toggle('files')),

    # HIdes the bar
    # Key([mod, "control"], "b", lazy.hide_show_bar("all")),
    Key([mod, "control"], "b", lazy.spawn("./.config/qtile/xmenu.sh")),
    Key([mod, "shift"], "m", hide_windows()),
    Key([mod], "t", lazy.spawn("kitty btop")),
    # Key([mod, "shift"], "l", lazy.spawn("betterlockscreen -l"))
]

# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█


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
# ScratchPad
groups.append(ScratchPad(
    "scratchpad", [DropDown("term", scratch,
                            width=0.6, height=0.6, x=0.2, y=0.2, opacity=1),
                   ]))


fs = 20
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

###𝙇𝙖𝙮𝙤𝙪𝙩###
_margin = 5
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
    # Try more layouts by unleashing below layouts
    #  layout.Stack(num_stacks=2),
    #  layout.Bsp(),
    # layout.Matrix(border_focus=colors['accent'],
    #               border_normal='#1F1D2E',
    #               margin=_margin,
    #               border_width=3,
    #               ),
    # layout.MonadTall(border_focus=colors['accent'],
    #               border_normal='#1F1D2E',
    #                 margin=4,
    #                 border_width=3,
    #                 ),
    # layout.MonadWide(border_focus='#1F1D2E',
    #                 border_normal='#1F1D2E',
    #                 margin=4,
    #                 border_width=0,
    #                 ),
    #  layout.RatioTile(),
    layout.Tile(border_focus=colors['accent'],
                border_normal='#1F1D2E',
                border_width=2,
                margin=_margin
                ),
    #  layout.TreeTab(),
    #  layout.VerticalTile(),
    # layout.Zoomy(
    #     margin=0
    # ),
]


widget_defaults = dict(
    font="sans",
    fontsize=20,
    padding=3,
)
extension_defaults = [widget_defaults.copy()
                      ]


def open_launcher():
    qtile.cmd_spawn("rofi -show drun")


# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄
screens = [

    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    # background=colors['main'],
                    padding=0,
                    scale=0.5,
                ),
                # widget.CurrentLayout(
                #     foreground=colors['white'],
                #     background=colors['black'],
                #     font=_font,
                # ),

                widget.GroupBox(
                    font=_font,
                    fontsize=fs,
                    padding=12,
                    borderwidth=5,
                    highlight_method='line',
                    active=colors['white'],
                    block_highlight_text_color=colors['green'],
                    highlight_color=colors['black'],
                    inactive='#666',
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
                # widget.TextBox(
                #     text='',
                #     fontsize=40,
                #     font=_font,
                #     padding=20,
                #     foreground=colors['white'],
                #     mouse_callbacks={"Button1": lazy.spawn(
                #         ranger)}
                # ),
                #
                # widget.Spacer(
                #     length=200
                # ),
                widget.TaskList(
                    border=colors['white'],
                    foreground="#000",
                    unfocused_border="#666",
                    max_title_width=300,
                    # font=_font,
                    highlight_method='block',
                    title_width_method='uniform',
                    # padding_x=10,
                    # padding_y=5,
                    # icon_size=0,
                    # theme_mode="preferred",
                    rounded=True
                ),
                # widget.Spacer(
                #     length=200
                # ),
                #
       
                # widget.TextBox(
                #     text="Apps",
                #     font=_font,
                #     mouse_callbacks={"Button1": lazy.spawn(launcher)}
                # ),
   # widget.Pomodoro(
   #                  font=_font,
   #                  fontsize=fs,
   #                  # prefix_inactive='',
   #                  length_pomodori=50,
   #                  color_inactive=colors['white']
   #              ),
                widget.Spacer(length=50),

                widget.Systray(
                    icon_size=32,
                    # background=["#00000000", "#00000000", "#00000000"],
                    padding=50
                ),
                # widget.TextBox(
                #     text='       ',
                #     background=colors['black']
                # ),
                widget.Spacer(length=50),
            
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    fontsize=fs+6,
                    padding=0,
                    foreground=colors["white"],
                    # background=colors['black'],
                    mouse_callbacks={"Button1": lazy.spawn('pavucontrol')}
                ),
                widget.Volume(
                    font=_font,
                    fontsize=fs,
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
                    font=_font,
                    text_charging=' {percentage:.0f}% {ttf}',
                    text_discharging='{percentage:.0f}% {tte}',
                    text_displaytime=2,
                ),
               


                widget.Spacer(length=50),


                widget.Clock(
                    format=' %B-%d %I:%M %p ',
                    # format='%a %d-%m-%y ',
                    foreground=colors['white'],
                    # background=colors['black'],
                    font=_font,
                    fontsize=fs,
                    mouse_callbacks={
                        "Button1": lazy.spawn(terminal+' tty-clock -ctB')}
                ),
             




            ],
            40,
            # margin=[5, 5, 0, 5],
            background=colors['black'],
            opacity=0.7
        ),

    ),

]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Click([mod], "Button1", lazy.spawn("./xmenu/xmenu.sh"))
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus='#1F1D2E',
    border_normal='#1F1D2E',
    border_width=0,
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

# some other imports
# stuff


@ hook.subscribe.startup_once
def autostart():
    # path to my script, under my user directory
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
