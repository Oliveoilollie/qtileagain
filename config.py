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
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import socket
import subprocess


from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
#extras
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
terminal = "alacritty"
mybrowser = "firefox"
#altterm = "kitty"
filemanager = "pcmanfm"


#Please change this to where your start.sh file is at in the qtile config
launcher = "/home/ollie/.config/qtile/start.sh"


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
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
    #return
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "Return", lazy.spawn(filemanager), desc="pcmanfm prob"),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    #rofi and menu thing
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="rofi"),
    Key([mod], "p", lazy.spawn(launcher), desc="launcher"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    #my own shortcuts (old)
    Key([mod], "b", lazy.spawn("brave"), desc="brave"),
    #Key([mod], "t", lazy.spawn("pcmanfm"), desc="File Explorer"),
    Key([mod], "f", lazy.spawn(mybrowser), desc="firefox"),
    Key([mod], "s", lazy.spawn("steam"), desc="steam"),
    #Key([mod], "d", lazy.spawn("discord"), desc="discord"),
    Key([mod], "g", lazy.spawn("heroic"), desc="heroic"),
    Key([mod], "c", lazy.spawn("cider"), desc="cider"),
    Key([mod], "n", lazy.spawn("nemo"), desc="nemo"),
    


    #super + letter thing
    Key([mod], "d", lazy.spawn(launcher), desc="launcher"),
    Key([mod], "h", lazy.spawn("urxvt 'htop task manager' -e htop"), desc="launcher"),
    Key([mod], "t", lazy.spawn("urxvt"), desc="File Explorer"),
    Key([mod], "m", lazy.spawn("pragha"), desc="music player"),
    Key([mod], "r", lazy.spawn("rofi-theme-selector"), desc="music player"),
    Key([mod], "v", lazy.spawn("pavucontrol"), desc="music player"),



    #ctrl and alt
    Key([ "control", "mod1" ], "h", lazy.spawn("urxvt 'htop task manager' -e htop"), desc="htop"),
    Key([ "control", "mod1" ], "a", lazy.spawn("xfce4-appfinder"), desc="htop"),
    Key([ "control", "mod1" ], "b", lazy.spawn("thunar"), desc="discord"),
    Key([ "control", "mod1" ], "c", lazy.spawn("catfish"), desc="catfish"),
    Key([ "control", "mod1" ], "d", lazy.spawn("discord"), desc="launcher"),
    Key([ "control", "mod1" ], "e", lazy.spawn("archlinux-tweak-tool"), desc="tweaks"),
    Key([ "control", "mod1" ], "f", lazy.spawn("firefox"), desc="broweser"),
    Key([ "control", "mod1" ], "g", lazy.spawn("chromium -no-default-browser-check"), desc="broweser"),
    Key([ "control", "mod1" ], "i", lazy.spawn("minecraft-launcher"), desc="minecraft"),
    Key([ "control", "mod1" ], "k", lazy.spawn("archlinux-logout"), desc="logout"),
    Key([ "control", "mod1" ], "l", lazy.spawn("archlinux-logout"), desc="archlinux-logout"),
    Key([ "control", "mod1" ], "m", lazy.spawn("xfce4-settings-manager"), desc="settimgs"),
    Key([ "control", "mod1" ], "o", lazy.spawn("kitty"), desc="kitty"),
    Key([ "control", "mod1" ], "p", lazy.spawn("pamac-manager"), desc="software"),
    Key([ "control", "mod1" ], "r", lazy.spawn("rofi-theme-selector"), desc="rofi-themes"),
    Key([ "control", "mod1" ], "w", lazy.spawn("arcolinux-welcome-app"), desc="WELCOME"),



    #F keys shortcuts (super)
    Key([mod], "F1", lazy.spawn("chromium"), desc="chrome"),
    Key([mod], "F2", lazy.spawn("brave"), desc="brave"),
    Key([mod], "F3", lazy.spawn(mybrowser), desc="Default_Browser"),
    Key([mod], "F4", lazy.spawn("gimp"), desc="gimp"),
    Key([mod], "F5", lazy.spawn("obs"), desc="Screenrecoder"),
    Key([mod], "F6", lazy.spawn("vlc --video-on-top"), desc="vlc"),
    Key([mod], "F7", lazy.spawn("virtualbox"), desc="VM"),
    Key([mod], "F8", lazy.spawn("thunar"), desc="XFCE-FM"),
    Key([mod], "F9", lazy.spawn("evolution"), desc="email"),
    Key([mod], "F10", lazy.spawn("spotify"), desc="musioc"),
    Key([mod], "F11", lazy.spawn("rofi -theme-str 'window {width: 100%;height: 100%;}' -show drun"), desc="rofi2"),
    Key([mod], "F12", lazy.spawn("rofi -show drun"), desc="rofi-again"),

    #loging out bois
    Key([mod], "x", lazy.spawn("archlinux-logout"), desc="nemo"),
#rofi
    #Key([mod], "p", lazy.spawn("rofi -show run"), desc="rofi"),

#working dmenu
    #Key(['mod4'], 'm', lazy.run_extension(extension.DmenuRun(
        #dmenu_prompt=">",
        #dmenu_font="Andika-8",
        #background="#15181a",
        #foreground="#00ff00",
        #selected_background="#079822",
        #selected_foreground="#fff",
    #))),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#2B0E66", "#2B0E66"], border_width=7, border_focus=["#00BE67"], border_normal=["#001D31"]),
    layout.Max(),
    layout.Floating(border_focus=["#00BE67"])
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    #layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    #layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="nerd-fonts-ubuntu-mono",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

#powerlineextras
powerline = {
    "decorations": [
        PowerLineDecoration(path='arrow_right')
    ]
}
screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.Image(
                    #filename = "~/.config/qtile/icons/arch.png",
                    #mouse_callbacks = { 'Button1': lazy.spawn( ['jgmenu_run'] ) },
                    #background='#00BE67',
                       #),
                widget.Image(
                    filename = "~/.config/qtile/icons/arch.png",
                    mouse_callbacks = { 'Button1': lazy.spawn( [launcher] ) },
                    background='#00BE67',
                       ),
                widget.CurrentLayout(background='#00BE67', foreground="#FFFFFF", **powerline),
                #ik take in the chaos lmao
                widget.GroupBox(highlight_method='line', foreground="#FFFFFF", active="#00BE67", this_current_screen_border="#00BE67", other_current_screen_border="#00BE67", this_screen_border="00A1D5", inactive="#FFFFFF"),
                #yes its over
                widget.Prompt(),
                widget.WindowName(foreground="#00BE67"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("Ollie OS", name="default"),
                widget.Cmus(),
                widget.TextBox("i use arch btw!", foreground="#00BE67", **powerline),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                # #my mess (LOL)
                widget.Systray(background='#00BE67', **powerline),
                #widget.Bluetooth(),
                widget.CPU(background='#00A1D5', foreground='FFFFFF', **powerline),
                widget.Memory(background='#00BE67', foreground='FFFFFF', **powerline),
                widget.Memory(format='Swap: {SwapUsed: .0f}{ms}/{SwapTotal: .0f}{ms}', background='#00A1D5', foreground='FFFFFF', **powerline),
                widget.ThermalSensor(background='#00BE67', foreground='FFFFFF', **powerline),
                #the end of my mess
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", background='#00A1D5', foreground='FFFFFF', **powerline),
                #widget.Bluetooth(background='#C05746', foreground='FFFFFF', **powerline)
                widget.QuickExit(background='#00BE67', foreground='#FFFFFF', **powerline),
                #widget.Image(
                    #filename = "~/.config/qtile/icons/arch.png",
                    #mouse_callbacks = { 'Button1': lazy.spawn( ['jgmenu_run'] ) },
                       #),
                #widget.Image(
                    #filename = "~/.config/qtile/icons/shutdown.png",
                    #mouse_callbacks = { 'Button1': lazy.spawn( ['shutdown', 'now'] ) },
                       #),



            ],
            24,
             border_width=[2, 0, 2, 0],  # Draw top and bottom borders
             #background="#30343f"
             background="#001D31"
             #border_color=["48A9A6", "48A9A6", "48A9A6", "48A9A6"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
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

#autostart
import os
import subprocess

from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.Popen([home])



