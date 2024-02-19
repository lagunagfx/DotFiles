#!/bin/sh

# according to https://nonfree.eu/

# locally trust the ci key:
sudo pacman-key --recv-keys B728DB23B92CB01B && sudo pacman-key --lsign-key B728DB23B92CB01B
#  add the repo configuration:
sudo sh -c "curl -s https://nonfree.eu/$(pacman-mirrors -G)/ > /etc/pacman.d/mesa-nonfree.pre.repo.conf"
# include the repo configuration:
sudo sed -i '/^\[core\]/i \Include = /etc/pacman.d/mesa-nonfree.pre.repo.conf\n' /etc/pacman.conf
# then refresh the mirrors/database with:
sudo pacman-mirrors -f5 && sudo pacman -Syyu
