
Debian
====================
This directory contains files used to package BFNd/BFN-qt
for Debian-based Linux systems. If you compile BFNd/BFN-qt yourself, there are some useful files here.

## BFN: URI support ##


BFN-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install BFN-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your BFN-qt binary to `/usr/bin`
and the `../../share/pixmaps/BFN128.png` to `/usr/share/pixmaps`

BFN-qt.protocol (KDE)

