from qtile_extras import widget
from functions import get_colors

colors = get_colors()
widgets = [
    widget.Clock(
        # format='%I:%M %p',
        format='  %b-%d | %I:%M %p ',
        foreground=colors[0],
        background=colors[8],
        margin=3,
        padding=5,
    ),
    widget.CurrentLayout(),
    widget.WindowCount(
        foreground=colors[0],
        background=colors[7],
        fmt="󰖲 {}"
    ),
    widget.WindowName(),
    widget.Spacer(),
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
    widget.Spacer(),
    widget.CPU(fmt = '{}'),
    widget.Memory(fmt = '{}'),
    widget.Systray(icon_size = 33),
    widget.Spacer(length=10,),
    widget.Battery(
        # format="{char} {percent:2.0%} {hour:d}:{min:02d}",
        format="{char} {percent:2.0%}",
        charge_char="󱐋 pwr^",
        discharge_char="󰁹 bat~",
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
]

widgets_simple = [
    widget.GroupBox(highlight_method='block',padding=7,rounded=False,this_current_screen_border=colors[3],block_highlight_text_color=colors[0],active="#0a0"),
    widget.CurrentLayout(),
    widget.WindowCount(background=colors[7],foreground=colors[0]),
    widget.WindowName(),
    widget.Systray(icon_size = 32,),
    widget.Sep(padding=20),
    widget.Pomodoro(length_pomodori=40,prefix_inactive='start(40-5-15)', color_inactive=colors[7],),
    widget.Sep(padding=20),
    widget.CPU(format='CPU: {load_percent}%'),
    widget.Sep(padding=20),
    widget.Memory(format='RAM:{MemUsed: .0f}{mm}'),
    widget.Sep(padding=20),
    widget.Battery(
        format = "{char} {percent:2.0%}",        
        charge_char="󱐋 pwr^",
        discharge_char="󰁹 bat~",
        foreground="#0f0",
        low_foreground="#f00",
    ),
    widget.Sep(padding=20),
    widget.Volume(
        fmt="Vol: {}"
    ),
    widget.Sep(padding=20),
    widget.Backlight(
        backlight_name="intel_backlight",
        format = "BL: {percent:2.0%}",
    ),
    widget.Sep(padding=20),
    widget.Clock(format="%b-%d %I:%M %p "),
]

def get_widgets(w):
    return w
