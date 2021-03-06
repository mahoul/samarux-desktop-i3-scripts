Name:           samarux-desktop-i3-scripts
Version:        0.1
Release:        32
Summary:        Auxiliary scripts for samarux-desktop-i3 environment
License:        GPL
Source: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
Packager: 	Enrique Gil (mahoul@gmail.com)
BuildArch:	noarch
BuildRequires:	rsync

%description
Auxiliary scripts for samarux-desktop-i3 environment.
Most of the files for this are minimal tweaked versions from files
from the awesome Regolith project (https://regolith-linux.org/)

%prep
#[ -d %{name} ] && rm -Rfv %{name}
#[ -d %{_topdir}/SOURCES ] && rsync -avP --exclude '.git' --delete %{_topdir}/SOURCES/ .
%autosetup


%install
%{__install} -D -m644 etc/dconf/db/distro.d/00-samarux-i3 %{buildroot}/etc/dconf/db/distro.d/00-samarux-i3
%{__install} -D -m755 usr/bin/dmenu_hotkeys.py		  %{buildroot}/usr/bin/dmenu_hotkeys.py
%{__install} -D -m755 usr/bin/polybar-launch.sh		  %{buildroot}/usr/bin/polybar-launch.sh
%{__install} -D -m755 usr/bin/set-bing-wallpaper.sh	  %{buildroot}/usr/bin/set-bing-wallpaper.sh
%{__install} -D -m755 usr/bin/system-fan-speed.sh	  %{buildroot}/usr/bin/system-fan-speed.sh
%{__install} -D -m755 usr/bin/toggle-picom.sh		  %{buildroot}/usr/bin/toggle-picom.sh

%post
[ -s /etc/dconf/db/distro ] && dconf update

%clean

%files
%defattr(-, root, root)
/etc/dconf/db/distro.d/00-samarux-i3
/usr/bin/dmenu_hotkeys.py
/usr/bin/polybar-launch.sh
/usr/bin/set-bing-wallpaper.sh
/usr/bin/system-fan-speed.sh
/usr/bin/toggle-picom.sh

%changelog
* Sun May 02 2021 Enrique Gil <mahoul@gmail.com> - 0.1-32
- Run only dconf update if distro DB exists

* Sun May 02 2021 Enrique Gil <mahoul@gmail.com> - 0.1-31
- Moved gsettings calls to dconf system wide defaults

* Sat May 01 2021 Enrique Gil <mahoul@gmail.com> - 0.1-30
- Increased release

* Sun Apr 25 2021 Enrique Gil <mahoul@gmail.com> - 0.1-29
- Fixed post install script on package

* Sun Apr 25 2021 Enrique Gil <mahoul@gmail.com> - 0.1-28
- Fixed TMP file removal on get-bing-potd.sh script

* Sun Apr 25 2021 Enrique Gil <mahoul@gmail.com> - 0.1-27
- Fixed TMP file removal on get-bing-potd.sh script

* Sat Apr 24 2021 Enrique Gil <mahoul@gmail.com> - 0.1-26
- Force symlink to default wallpaper on get-bing-potd.sh script

* Sat Apr 24 2021 Enrique Gil <mahoul@gmail.com> - 0.1-25
- Replaced bing wallpaper scripts and added systemd services

* Sun Apr 11 2021 Enrique Gil <mahoul@gmail.com> - 0.1-24
- Replaced prep section with autosetup

* Sun Apr 11 2021 Enrique Gil (mahoul@gmail.com) - 0.1-23
- Test build with hybrid prep section

* Sun Apr 11 2021 Enrique Gil (mahoul@gmail.com) - 0.1-23
- Updated prep section to use autosetup.

* Sun Apr 11 2021 Enrique Gil (mahoul@gmail.com) - 0.1-22
- Renamed pkg to samarux-desktop-i3-scripts

* Sat Apr 10 2021 Enrique Gil (mahoul@gmail.com) - 0.1-21
- Changed feh --bg-scale to --bg-fill

* Sat Apr 10 2021 Enrique Gil (mahoul@gmail.com) - 0.1-20
- Renamed package to samarux-desktop-scripts

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-19
- Changed default mono font and enabled window resize with secondary button

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-18
- Resize windows with secondary mouse button

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-17
- Removed volumeicon disabling desktop file as it is created by
  samarux-desktop-skel package

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-16
- Added dmenu_hotkeys.py script

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-15
- Disable input layout switching via Super+Space

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-14
- Disable volume icon autostart on samarux-look.sh run

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-13
- Disable volume icon autostart on samarux-look.sh run

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-12
- Disable volume icon autostart on samarux-look.sh run

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-11
- Disable volume icon autostart on samarux-look.sh run

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-10
- Set fan speed to 0 if running virtual

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-9
- Added set-bing-wallpaper.sh script and python dep script

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-8
- Added system-fan-speed.sh

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-7
- Updated toggle-picom.sh script to not run in a VM

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-6
- Updated samarux-look.sh script

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-5
- Added toggle-picom.sh script

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-4
- Added samarux-look.sh script

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-3
- Fixed permissions for polybar-launch.sh

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-2
- Initial package build

* Sat Mar 27 2021 Enrique Gil (mahoul@gmail.com) - 0.1-1
- Initial release.

