#!/usr/bin/bash

# Tweak GNOME flashback settings

gsettings set org.gnome.gnome-flashback desktop false
gsettings set org.gnome.gnome-flashback notifications false
gsettings set org.gnome.gnome-flashback status-notifier-watcher false

# Tweak GNOME Terminal settings

DEFAULT_TERMINAL_PROFILE=$(gsettings get org.gnome.Terminal.ProfilesList default | awk -F "'" '{print $2}')

gsettings set org.gnome.Terminal.Legacy.Settings default-show-menubar false
gsettings set org.gnome.Terminal.Legacy.Settings headerbar false
dconf write /org/gnome/terminal/legacy/profiles:/:"${DEFAULT_TERMINAL_PROFILE}"/scrollbar-policy "'never'"

# Tweak GNOME Fonts

gsettings set org.gnome.desktop.interface document-font-name 'Fira Sans Medium 11'
gsettings set org.gnome.desktop.interface font-name 'Fira Sans Medium 11'
gsettings set org.gnome.desktop.interface monospace-font-name 'Fira Code Medium 10'
gsettings set org.gnome.desktop.wm.preferences titlebar-font 'Fira Sans Bold 11'

# Resize windows with secondary mouse button

gsettings set org.gnome.desktop.wm.preferences resize-with-right-button true

# Disable input switch via Super+Space
gsettings set org.gnome.desktop.wm.keybindings switch-input-source '[]'
gsettings set org.gnome.desktop.wm.keybindings switch-input-source-backward '[]'
