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
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from qtile_extras import widget


mod = "mod4"
terminal = "kitty"
browser = "chromium"
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
    Key([mod], "p", lazy.spawn("rofi -show run"),
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
    Key([mod], "b", lazy.spawn(browser)),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
    Key([mod], "e", lazy.spawn("kitty ranger")),
    Key([mod], "c", lazy.spawn("code")),
    Key(["mod1"], "space", lazy.spawn('nitrogen')),

    # PowerMenu
    Key([mod], "Escape", lazy.spawn(
        "rofi -show power-menu -modi power-menu:rofi-power-menu"
    ))





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


_font = "Monospace"
colors = dict(
    black="#000000",
    accent='#cccccc80',
    main='#00000000',
    bg='#1a1b26',
    trans='#000000',
    blue='#24f',
    green='#44ee33',
    red='#f44',
    yellow='#fd0',
    white='#ffffff40'
)

###𝙇𝙖𝙮𝙤𝙪𝙩###
_margin = 10
layouts = [
    layout.Columns(margin=_margin, border_focus=colors['accent'],
                   border_normal='#1F1D2E',
                   border_width=3
                   ),

    layout.Max(border_focus=colors['accent'],
               border_normal='#1F1D2E',
               margin=_margin,
               border_width=3,
               ),

    layout.Floating(border_focus=colors['accent'],
                    border_normal='#1F1D2E',
                    margin=_margin,
                    border_width=3,
                    ),
    # Try more layouts by unleashing below layouts
    #  layout.Stack(num_stacks=2),
    #  layout.Bsp(),
    layout.Matrix(border_focus=colors['accent'],
                  border_normal='#1F1D2E',
                  margin=_margin,
                  border_width=3,
                  ),
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
    layout.Zoomy(
        margin=0
    ),
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
                    background=colors['black'],
                    padding=0,
                    scale=0.5,
                ),
                # widget.CurrentLayout(
                #     foreground='#000',
                #     background=colors['accent'],
                #     font=_font,
                # ),

                widget.GroupBox(
                    font=_font,
                    fontsize=25,
                    padding=10,
                    borderwidth=5,
                    highlight_method='line',
                    active='#fff',
                    block_highlight_text_color="#000",
                    highlight_color='#f5f5f5bf',
                    inactive=colors['black'],
                    foreground=colors['white'],
                    background=colors['white'],
                    this_current_screen_border=colors['green'],
                    this_screen_border='#fff',
                    other_current_screen_border='#fff',
                    other_screen_border='#fff',
                    urgent_border='#fff',
                    rounded=False,
                    disable_drag=True,
                ),
                widget.TextBox(
                    text=' ',
                    fontsize=25,
                    font=_font,
                    padding=20,
                    mouse_callbacks={"Button1": lazy.spawn(
                        "thunar"), "Button3": lazy.spawn("kitty ranger")},
                ),
                widget.TextBox(
                    text=' ',
                    fontsize=25,
                    padding=10,
                    mouse_callbacks={"Button3": lazy.spawn(
                        "chromium youtube.com --start-fullscreen"), "Button1": lazy.spawn("chromium youtube.com")}
                ),
                widget.TextBox(
                    text=' ',
                    fontsize=35,
                    padding=17,
                    mouse_callbacks={"Button1": lazy.spawn(
                        "pycharm"), "Button3": lazy.spawn("jupyter-lab")}
                ),
                widget.TextBox(
                    text='R',
                    font='JetBrainsMono Extra Bold',
                    fontsize=25,
                    padding=0,
                    mouse_callbacks={"Button1": lazy.spawn(
                        "rstudio")}
                ),
                # widget.Wallpaper(
                #    directory='~/Downloads/wallpapers',
                #    label=' ',
                #    padding=10,
                #    background=colors['black'],
                # ),


                widget.Spacer(),

                widget.WidgetBox(
                    text_closed='< Arch Linux >',
                    text_open='->',
                    font='terminus bold',
                    fontsize=22,
                    foreground='#fff',
                    widgets=[

                        widget.TextBox(
                            text=' S-tui',
                            foreground=colors['green'],
                            fontsize=22,
                            font=_font,
                            padding=30,
                            mouse_callbacks={
                                "Button1": lazy.spawn("kitty s-tui")}
                        ),

                        widget.TextBox(
                            text=' Vtop',
                            fontsize=22,
                            font=_font,
                            padding=30,
                            foreground=colors['yellow'],
                            mouse_callbacks={
                                "Button1": lazy.spawn("kitty vtop")}
                        ),
                        widget.TextBox(
                            text=' Duc',
                            foreground='#fff',
                            # background=colors['red'],
                            fontsize=22,
                            font=_font,
                            padding=30,
                            mouse_callbacks={
                                "Button1": lazy.spawn('kitty duc ui')}
                        ),

                    ]
                ),

                widget.Spacer(),
                # widget.WidgetBox(
                #    widgets=[
                #        widget.Memory(
                #            foreground='#fff', font=_font, fontsize=23),
                #        widget.TextBox(padding=5),
                #        widget.CPU(
                #            foreground='#fff', font=_font, fontsize=23)
                #    ],
                #    text_closed='<',
                #    text_open='>',
                #    fontsize=30
                # ),
                widget.Systray(
                    icon_size=35,
                    background=colors['main'],
                    foreground=colors['blue'],
                    fontsize=2,
                    padding=50
                ),

                widget.Battery(
                    format='{char}{percent:2.0%}',
                    charge_char='  ',
                    discharge_char='   ',
                    font=_font,
                    fontsize=22,
                    padding=50,
                    background=colors["main"],
                ),


                widget.TextBox(
                    text="",
                    font="Font Awesome 6 Free Solid",
                    fontsize=25,
                    padding=0,
                    background=colors["main"],
                    mouse_callbacks={"Button1": lazy.spawn('kitty alsamixer')}
                ),

                widget.Volume(
                    font=_font,
                    fontsize=22,
                    padding=20,
                    background=colors["main"],
                ),




                widget.Clock(
                    format=' %B-%d %I:%M %p ',
                    foreground="#000",
                    background='#ffffffbf',
                    font=_font,
                    fontsize=22,
                    mouse_callbacks={
                        "Button1": lazy.spawn('kitty tty-clock -ctB')}
                ),




            ],
            40,
            margin=[5, 10, 0, 10],
            background=colors['main']
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


@hook.subscribe.startup_once
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
