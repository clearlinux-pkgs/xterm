#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x702353E0F7E48EDB (dickey@invisible-island.net)
#
Name     : xterm
Version  : 364
Release  : 23
URL      : https://invisible-mirror.net/archives/xterm/xterm-364.tgz
Source0  : https://invisible-mirror.net/archives/xterm/xterm-364.tgz
Source1  : https://invisible-mirror.net/archives/xterm/xterm-364.tgz.asc
Summary  : X terminal emulator (development version)
Group    : Development/Tools
License  : MIT X11
Requires: xterm-bin = %{version}-%{release}
Requires: xterm-data = %{version}-%{release}
Requires: xterm-license = %{version}-%{release}
Requires: xterm-man = %{version}-%{release}
BuildRequires : cppcheck
BuildRequires : ctags
BuildRequires : desktop-file-utils
BuildRequires : elfutils-dev
BuildRequires : groff
BuildRequires : libXaw-dev
BuildRequires : libXcursor-dev
BuildRequires : libXft-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(xpm)

%description
xterm is the standard terminal emulator for the X Window System.
It provides DEC VT102 and Tektronix 4014 compatible terminals for
programs that cannot use the window system directly.  This version
implements ISO/ANSI colors, Unicode, and most of the control sequences
used by DEC VT220 terminals.

This package provides four commands:
 a) %{fullname}, which is the actual terminal emulator
 b) u%{fullname}, which is a wrapper around %{fullname}
    which sets %{fullname} to use UTF-8 encoding when
    the user's locale supports this,
 c) koi8r%{fullname}, a wrapper similar to u%{fullname}
    for locales that use the KOI8-R character set, and
 d) resize%{my_suffix}.

A complete list of control sequences supported by the X terminal emulator
is provided in /usr/share/doc/%{fullname}.

The %{fullname} program uses bitmap images provided by the xbitmaps package.

Those interested in using koi8r%{fullname} will likely want to install the
xfonts-cyrillic package as well.

This package is configured to use "%{fullname}" and "%{my_class}"
for the program and its resource class, to avoid conflict with other packages.

%package bin
Summary: bin components for the xterm package.
Group: Binaries
Requires: xterm-data = %{version}-%{release}
Requires: xterm-license = %{version}-%{release}

%description bin
bin components for the xterm package.


%package data
Summary: data components for the xterm package.
Group: Data

%description data
data components for the xterm package.


%package license
Summary: license components for the xterm package.
Group: Default

%description license
license components for the xterm package.


%package man
Summary: man components for the xterm package.
Group: Default

%description man
man components for the xterm package.


%prep
%setup -q -n xterm-364
cd %{_builddir}/xterm-364

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612383892
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --enable-freetype
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1612383892
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xterm
cp %{_builddir}/xterm-364/COPYING %{buildroot}/usr/share/package-licenses/xterm/2a211dc0248a187c771d8183ba139328f0ad014b
cp %{_builddir}/xterm-364/package/debian/copyright %{buildroot}/usr/share/package-licenses/xterm/6a5d4ed854eca449f5fa350c5cb2781014541d61
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/X11/app-defaults/KOI8RXTerm
/usr/lib/X11/app-defaults/KOI8RXTerm-color
/usr/lib/X11/app-defaults/UXTerm
/usr/lib/X11/app-defaults/UXTerm-color
/usr/lib/X11/app-defaults/XTerm
/usr/lib/X11/app-defaults/XTerm-color

%files bin
%defattr(-,root,root,-)
/usr/bin/koi8rxterm
/usr/bin/resize
/usr/bin/uxterm
/usr/bin/xterm

%files data
%defattr(-,root,root,-)
/usr/share/pixmaps/filled-xterm_32x32.xpm
/usr/share/pixmaps/filled-xterm_48x48.xpm
/usr/share/pixmaps/mini.xterm_32x32.xpm
/usr/share/pixmaps/mini.xterm_48x48.xpm
/usr/share/pixmaps/xterm-color_32x32.xpm
/usr/share/pixmaps/xterm-color_48x48.xpm
/usr/share/pixmaps/xterm_32x32.xpm
/usr/share/pixmaps/xterm_48x48.xpm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xterm/2a211dc0248a187c771d8183ba139328f0ad014b
/usr/share/package-licenses/xterm/6a5d4ed854eca449f5fa350c5cb2781014541d61

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/koi8rxterm.1
/usr/share/man/man1/resize.1
/usr/share/man/man1/uxterm.1
/usr/share/man/man1/xterm.1
