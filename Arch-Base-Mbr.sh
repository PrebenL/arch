#!/bin/bash

ln -sf /usr/share/zoneinfo/Europe/Brussels /etc/localtime
hwclock --systohc
sed -i '177s/.//' /etc/locale.gen
locale-gen
echo "LANG=en_US.UTF-8" >> /etc/locale.conf
echo "arch" >> /etc/hostname
echo "::1       localhost" >> /etc/hosts
echo "127.0.0.1 arch.localdomain arch" >> /etc/hosts
echo root:password | chpasswd

# You can add xorg to the installation packages, I usually add it at the DE or WM install script
# You can remove the tlp package if you are installing on a desktop or vm

pacman -S --noconfirm grub networkmanager reflector linux-headers xdg-user-dirs xdg-utils gvfs gvfs-smb alsa-utils pulseaudio bash-completion openssh rsync reflector terminus-font

# pacman -S --noconfirm xf86-video-amdgpu
# pacman -S --noconfirm nvidia nvidia-utils nvidia-settings

grub-install --target=i386-pc /dev/sdX # replace sdx with your disk name, not the partition
grub-mkconfig -o /boot/grub/grub.cfg

systemctl enable NetworkManager
systemctl enable sshd
systemctl enable tlp # You can comment this command out if you didn't install tlp, see above
systemctl enable reflector.timer
systemctl enable fstrim.timer

useradd -m preben
echo preben:password | chpasswd

echo "preben ALL=(ALL) ALL" >> /etc/sudoers.d/preben


printf "\e[1;32mDone! Type exit, umount -a and reboot.\e[0m"
