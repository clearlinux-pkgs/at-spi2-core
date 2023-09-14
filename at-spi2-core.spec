#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : at-spi2-core
Version  : 2.48.4
Release  : 46
URL      : https://download.gnome.org/sources/at-spi2-core/2.48/at-spi2-core-2.48.4.tar.xz
Source0  : https://download.gnome.org/sources/at-spi2-core/2.48/at-spi2-core-2.48.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: at-spi2-core-data = %{version}-%{release}
Requires: at-spi2-core-lib = %{version}-%{release}
Requires: at-spi2-core-libexec = %{version}-%{release}
Requires: at-spi2-core-license = %{version}-%{release}
Requires: at-spi2-core-locales = %{version}-%{release}
Requires: at-spi2-core-services = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : dbus-broker
BuildRequires : glib-dev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : libxkbcommon-dev
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xt)
BuildRequires : pkgconfig(xtst)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Building ATK with Visual Studio
===============================
Meson is now the supported method of building ATK using Visual Studio.

%package data
Summary: data components for the at-spi2-core package.
Group: Data

%description data
data components for the at-spi2-core package.


%package dev
Summary: dev components for the at-spi2-core package.
Group: Development
Requires: at-spi2-core-lib = %{version}-%{release}
Requires: at-spi2-core-data = %{version}-%{release}
Provides: at-spi2-core-devel = %{version}-%{release}
Requires: at-spi2-core = %{version}-%{release}

%description dev
dev components for the at-spi2-core package.


%package lib
Summary: lib components for the at-spi2-core package.
Group: Libraries
Requires: at-spi2-core-data = %{version}-%{release}
Requires: at-spi2-core-libexec = %{version}-%{release}
Requires: at-spi2-core-license = %{version}-%{release}

%description lib
lib components for the at-spi2-core package.


%package libexec
Summary: libexec components for the at-spi2-core package.
Group: Default
Requires: at-spi2-core-license = %{version}-%{release}

%description libexec
libexec components for the at-spi2-core package.


%package license
Summary: license components for the at-spi2-core package.
Group: Default

%description license
license components for the at-spi2-core package.


%package locales
Summary: locales components for the at-spi2-core package.
Group: Default

%description locales
locales components for the at-spi2-core package.


%package services
Summary: services components for the at-spi2-core package.
Group: Systemd services
Requires: systemd

%description services
services components for the at-spi2-core package.


%prep
%setup -q -n at-spi2-core-2.48.4
cd %{_builddir}/at-spi2-core-2.48.4
pushd ..
cp -a at-spi2-core-2.48.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694732092
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/at-spi2-core
cp %{_builddir}/at-spi2-core-%{version}/COPYING %{buildroot}/usr/share/package-licenses/at-spi2-core/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang at-spi2-core
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Atk-1.0.typelib
/usr/lib64/girepository-1.0/Atspi-2.0.typelib
/usr/share/dbus-1/accessibility-services/org.a11y.atspi.Registry.service
/usr/share/dbus-1/services/org.a11y.Bus.service
/usr/share/defaults/at-spi2/accessibility.conf
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/at-spi-2.0/atspi/atspi-accessible.h
/usr/include/at-spi-2.0/atspi/atspi-action.h
/usr/include/at-spi-2.0/atspi/atspi-application.h
/usr/include/at-spi-2.0/atspi/atspi-collection.h
/usr/include/at-spi-2.0/atspi/atspi-component.h
/usr/include/at-spi-2.0/atspi/atspi-constants.h
/usr/include/at-spi-2.0/atspi/atspi-device-legacy.h
/usr/include/at-spi-2.0/atspi/atspi-device-listener.h
/usr/include/at-spi-2.0/atspi/atspi-device-x11.h
/usr/include/at-spi-2.0/atspi/atspi-device.h
/usr/include/at-spi-2.0/atspi/atspi-document.h
/usr/include/at-spi-2.0/atspi/atspi-editabletext.h
/usr/include/at-spi-2.0/atspi/atspi-enum-types.h
/usr/include/at-spi-2.0/atspi/atspi-event-listener.h
/usr/include/at-spi-2.0/atspi/atspi-gmain.h
/usr/include/at-spi-2.0/atspi/atspi-hyperlink.h
/usr/include/at-spi-2.0/atspi/atspi-hypertext.h
/usr/include/at-spi-2.0/atspi/atspi-image.h
/usr/include/at-spi-2.0/atspi/atspi-matchrule.h
/usr/include/at-spi-2.0/atspi/atspi-misc.h
/usr/include/at-spi-2.0/atspi/atspi-object.h
/usr/include/at-spi-2.0/atspi/atspi-registry.h
/usr/include/at-spi-2.0/atspi/atspi-relation.h
/usr/include/at-spi-2.0/atspi/atspi-selection.h
/usr/include/at-spi-2.0/atspi/atspi-stateset.h
/usr/include/at-spi-2.0/atspi/atspi-table-cell.h
/usr/include/at-spi-2.0/atspi/atspi-table.h
/usr/include/at-spi-2.0/atspi/atspi-text.h
/usr/include/at-spi-2.0/atspi/atspi-types.h
/usr/include/at-spi-2.0/atspi/atspi-value.h
/usr/include/at-spi-2.0/atspi/atspi-version.h
/usr/include/at-spi-2.0/atspi/atspi.h
/usr/include/at-spi2-atk/2.0/atk-bridge.h
/usr/include/atk-1.0/atk/atk-autocleanups.h
/usr/include/atk-1.0/atk/atk-enum-types.h
/usr/include/atk-1.0/atk/atk.h
/usr/include/atk-1.0/atk/atkaction.h
/usr/include/atk-1.0/atk/atkcomponent.h
/usr/include/atk-1.0/atk/atkdocument.h
/usr/include/atk-1.0/atk/atkeditabletext.h
/usr/include/atk-1.0/atk/atkgobjectaccessible.h
/usr/include/atk-1.0/atk/atkhyperlink.h
/usr/include/atk-1.0/atk/atkhyperlinkimpl.h
/usr/include/atk-1.0/atk/atkhypertext.h
/usr/include/atk-1.0/atk/atkimage.h
/usr/include/atk-1.0/atk/atkmisc.h
/usr/include/atk-1.0/atk/atknoopobject.h
/usr/include/atk-1.0/atk/atknoopobjectfactory.h
/usr/include/atk-1.0/atk/atkobject.h
/usr/include/atk-1.0/atk/atkobjectfactory.h
/usr/include/atk-1.0/atk/atkplug.h
/usr/include/atk-1.0/atk/atkrange.h
/usr/include/atk-1.0/atk/atkregistry.h
/usr/include/atk-1.0/atk/atkrelation.h
/usr/include/atk-1.0/atk/atkrelationset.h
/usr/include/atk-1.0/atk/atkrelationtype.h
/usr/include/atk-1.0/atk/atkselection.h
/usr/include/atk-1.0/atk/atksocket.h
/usr/include/atk-1.0/atk/atkstate.h
/usr/include/atk-1.0/atk/atkstateset.h
/usr/include/atk-1.0/atk/atkstreamablecontent.h
/usr/include/atk-1.0/atk/atktable.h
/usr/include/atk-1.0/atk/atktablecell.h
/usr/include/atk-1.0/atk/atktext.h
/usr/include/atk-1.0/atk/atkutil.h
/usr/include/atk-1.0/atk/atkvalue.h
/usr/include/atk-1.0/atk/atkversion.h
/usr/include/atk-1.0/atk/atkwindow.h
/usr/lib64/libatk-1.0.so
/usr/lib64/libatk-bridge-2.0.so
/usr/lib64/libatspi.so
/usr/lib64/pkgconfig/atk-bridge-2.0.pc
/usr/lib64/pkgconfig/atk.pc
/usr/lib64/pkgconfig/atspi-2.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gtk-2.0/modules/libatk-bridge.so
/V3/usr/lib64/libatk-1.0.so.0.24813.1
/V3/usr/lib64/libatk-bridge-2.0.so.0.0.0
/V3/usr/lib64/libatspi.so.0.0.1
/usr/lib64/gtk-2.0/modules/libatk-bridge.so
/usr/lib64/libatk-1.0.so.0
/usr/lib64/libatk-1.0.so.0.24813.1
/usr/lib64/libatk-bridge-2.0.so.0
/usr/lib64/libatk-bridge-2.0.so.0.0.0
/usr/lib64/libatspi.so.0
/usr/lib64/libatspi.so.0.0.1

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/at-spi-bus-launcher
/V3/usr/libexec/at-spi2-registryd
/usr/libexec/at-spi-bus-launcher
/usr/libexec/at-spi2-registryd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/at-spi2-core/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/at-spi-dbus-bus.service

%files locales -f at-spi2-core.lang
%defattr(-,root,root,-)

