#!/bin/sh

#wiget things
nm-applet &
volumeicon &
flameshot &
#blueman-manager --restore
blueberry-tray &
#clipit &
pamac-tray &


#wallpapers
variety &
#nitrogen --restore

#compositor
picom --config $HOME/.config/qtile/scripts/picom.conf &

#Important things you might want
#dex -a
#lxsession &
numlockx on &

#FOR ARCO LINUX!!!!!!!!!!!!!!!
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &


#NOT NEEDED BUT JUST IN CASE LOL
#dex -a
#rofi
#lxsession &
#picom --vsync --sw-opti &
#lxappearance --restore
#compton --backend glx --paint-on-overlay --glx-no-stencil --vsync opengl-swc --unredir-if-possible
#picom --vsync --xrender-sync-fence
#picom --vsync --sw-opti --xrender-sync-fence --unredir-if-possible --paint-on-overlay --force-win-blend --backend
#picom --vsync  --xrender-sync-fence --unredir-if-possible --force-win-blend --backend glx --sw-opti --experimental-backends &
#picom --vsync &
#clipit &
#xfce4-display-settings --restore
#xfce-theme-manager --restore
#xfsettingsd &
