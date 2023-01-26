#!/bin/sh
nm-applet &
volumeicon &
nitrogen --restore
dex -a
flameshot &
#rofi
lxsession &
#picom --vsync --sw-opti &
lxappearance --restore
#compton --backend glx --paint-on-overlay --glx-no-stencil --vsync opengl-swc --unredir-if-possible
#picom --vsync --xrender-sync-fence
#picom --vsync --sw-opti --xrender-sync-fence --unredir-if-possible --paint-on-overlay --force-win-blend --backend
picom --vsync  --xrender-sync-fence --unredir-if-possible --force-win-blend --backend glx --sw-opti --experimental-backends &
#picom --vsync &
blueman-manager --restore
#clipit &
xfce4-display-settings --restore
#xfce-theme-manager --restore
xfsettingsd &
