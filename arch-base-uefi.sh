#! /bin/bash

ln -sf /usr/share/zoneinfo/Europe/Brussels /etc/localtime
hwclock --systohc
sed -i '177s/.//' /etc/locale.gen
locale-gen
echo "LANG=en_US.UTF-8" >> /etc/locale.conf
echo "arch" >> /etc/hostname
echo "::1       localhost" >> /etc/hosts
echo "127.0.0.1 localhost.localdomain arch" >> /etc/hosts
echo root:password | chpasswd


pacman -S grub efibootmgr networkmanager avahi linux-headers xdg-user-dirs xdg-utils gvfs gvfs-smb alsa-utils pipewire pipewire-alsa pipewire-pulse pipewire-jack openssh

# pacman -S --noconfirm xf86-video-amdgpu
# pacman -S --noconfirm nvidia nvidia-utils nvidia-settings

grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg

systemctl enable NetworkManager
systemctl enable sshd
#systemctl enable reflector.timer
systemctl enable fstrim.timer
systemctl enable avahi-daemon

useradd -m preben
echo preben:password | chpasswd

echo "preben ALL=(ALL) ALL" >> /etc/sudoers.d/preben


printf "\e[1;32mDone! Type exit, umount -a and reboot.\e[0m"

