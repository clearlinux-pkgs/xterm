#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xCC2AF4472167BE03 (dickey@his.com)
#
Name     : xterm
Version  : 381
Release  : 41
URL      : https://invisible-mirror.net/archives/xterm/xterm-381.tgz
Source0  : https://invisible-mirror.net/archives/xterm/xterm-381.tgz
Source1  : https://invisible-mirror.net/archives/xterm/xterm-381.tgz.asc
Summary  : X terminal emulator (development version)
Group    : Development/Tools
License  : MIT X11
Requires: xterm-bin = %{version}-%{release}
Requires: xterm-data = %{version}-%{release}
Requires: xterm-license = %{version}-%{release}
Requires: xterm-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : cppcheck
BuildRequires : ctags
BuildRequires : desktop-file-utils
BuildRequires : elfutils-dev
BuildRequires : groff
BuildRequires : libXaw-dev
BuildRequires : libXft-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xpm)
BuildRequires : pkgconfig(xt)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n xterm-381
cd %{_builddir}/xterm-381
pushd ..
cp -a xterm-381 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685478682
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --enable-freetype
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-freetype
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1685478682
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xterm
cp %{_builddir}/xterm-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xterm/e93c812d7c561104fbcdbb553ac56a35f113dfbb || :
cp %{_builddir}/xterm-%{version}/package/debian/copyright %{buildroot}/usr/share/package-licenses/xterm/4094ca68b138cda87c9fcbcb4f9975b975ef4c4c || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/bin/resize
/V3/usr/bin/xterm
/usr/bin/koi8rxterm
/usr/bin/resize
/usr/bin/uxterm
/usr/bin/xterm

%files data
%defattr(-,root,root,-)
/usr/share/pixmaps/filled-xterm_16x16.xpm
/usr/share/pixmaps/filled-xterm_32x32.xpm
/usr/share/pixmaps/filled-xterm_48x48.xpm
/usr/share/pixmaps/mini.xterm_16x16.xpm
/usr/share/pixmaps/mini.xterm_32x32.xpm
/usr/share/pixmaps/mini.xterm_48x48.xpm
/usr/share/pixmaps/xterm-color_16x16.xpm
/usr/share/pixmaps/xterm-color_32x32.xpm
/usr/share/pixmaps/xterm-color_48x48.xpm
/usr/share/pixmaps/xterm_16x16.xpm
/usr/share/pixmaps/xterm_32x32.xpm
/usr/share/pixmaps/xterm_48x48.xpm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xterm/4094ca68b138cda87c9fcbcb4f9975b975ef4c4c
/usr/share/package-licenses/xterm/e93c812d7c561104fbcdbb553ac56a35f113dfbb

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/koi8rxterm.1
/usr/share/man/man1/resize.1
/usr/share/man/man1/uxterm.1
/usr/share/man/man1/xterm.1
