#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : at-spi2-core
Version  : 2.24.0
Release  : 7
URL      : https://download.gnome.org/sources/at-spi2-core/2.24/at-spi2-core-2.24.0.tar.xz
Source0  : https://download.gnome.org/sources/at-spi2-core/2.24/at-spi2-core-2.24.0.tar.xz
Summary  : Accessibility Technology software library
Group    : Development/Tools
License  : LGPL-2.0
Requires: at-spi2-core-config
Requires: at-spi2-core-data
Requires: at-spi2-core-lib
Requires: at-spi2-core-bin
Requires: at-spi2-core-doc
Requires: at-spi2-core-locales
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-staticdev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libSM-dev32
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(32dbus-1)
BuildRequires : pkgconfig(32gio-2.0)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32gobject-2.0)
BuildRequires : pkgconfig(32ice)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xi)
BuildRequires : pkgconfig(32xt)
BuildRequires : pkgconfig(32xtst)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xt)
BuildRequires : pkgconfig(xtst)

%description
D-Bus AT-SPI
------------
This version of at-spi is a major break from version 1.x.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

%package bin
Summary: bin components for the at-spi2-core package.
Group: Binaries
Requires: at-spi2-core-data
Requires: at-spi2-core-config

%description bin
bin components for the at-spi2-core package.


%package config
Summary: config components for the at-spi2-core package.
Group: Default

%description config
config components for the at-spi2-core package.


%package data
Summary: data components for the at-spi2-core package.
Group: Data

%description data
data components for the at-spi2-core package.


%package dev
Summary: dev components for the at-spi2-core package.
Group: Development
Requires: at-spi2-core-lib
Requires: at-spi2-core-bin
Requires: at-spi2-core-data
Provides: at-spi2-core-devel

%description dev
dev components for the at-spi2-core package.


%package dev32
Summary: dev32 components for the at-spi2-core package.
Group: Default
Requires: at-spi2-core-lib32
Requires: at-spi2-core-bin
Requires: at-spi2-core-data
Requires: at-spi2-core-dev

%description dev32
dev32 components for the at-spi2-core package.


%package doc
Summary: doc components for the at-spi2-core package.
Group: Documentation

%description doc
doc components for the at-spi2-core package.


%package lib
Summary: lib components for the at-spi2-core package.
Group: Libraries
Requires: at-spi2-core-data
Requires: at-spi2-core-config

%description lib
lib components for the at-spi2-core package.


%package lib32
Summary: lib32 components for the at-spi2-core package.
Group: Default
Requires: at-spi2-core-data
Requires: at-spi2-core-config

%description lib32
lib32 components for the at-spi2-core package.


%package locales
Summary: locales components for the at-spi2-core package.
Group: Default

%description locales
locales components for the at-spi2-core package.


%prep
%setup -q -n at-spi2-core-2.24.0
pushd ..
cp -a at-spi2-core-2.24.0 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491312950
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1491312950
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang at-spi2-core

%files
%defattr(-,root,root,-)
/usr/lib32/girepository-1.0/Atspi-2.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/libexec/at-spi-bus-launcher
/usr/libexec/at-spi2-registryd

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/user/at-spi-dbus-bus.service

%files data
%defattr(-,root,root,-)
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
/usr/include/at-spi-2.0/atspi/atspi-device-listener-private.h
/usr/include/at-spi-2.0/atspi/atspi-device-listener.h
/usr/include/at-spi-2.0/atspi/atspi-document.h
/usr/include/at-spi-2.0/atspi/atspi-editabletext.h
/usr/include/at-spi-2.0/atspi/atspi-enum-types.h
/usr/include/at-spi-2.0/atspi/atspi-event-listener-private.h
/usr/include/at-spi-2.0/atspi/atspi-event-listener.h
/usr/include/at-spi-2.0/atspi/atspi-gmain.c
/usr/include/at-spi-2.0/atspi/atspi-gmain.h
/usr/include/at-spi-2.0/atspi/atspi-hyperlink.h
/usr/include/at-spi-2.0/atspi/atspi-hypertext.h
/usr/include/at-spi-2.0/atspi/atspi-image.h
/usr/include/at-spi-2.0/atspi/atspi-matchrule.h
/usr/include/at-spi-2.0/atspi/atspi-misc.h
/usr/include/at-spi-2.0/atspi/atspi-object.h
/usr/include/at-spi-2.0/atspi/atspi-private.h
/usr/include/at-spi-2.0/atspi/atspi-registry.h
/usr/include/at-spi-2.0/atspi/atspi-relation.h
/usr/include/at-spi-2.0/atspi/atspi-selection.h
/usr/include/at-spi-2.0/atspi/atspi-stateset.h
/usr/include/at-spi-2.0/atspi/atspi-table-cell.h
/usr/include/at-spi-2.0/atspi/atspi-table.h
/usr/include/at-spi-2.0/atspi/atspi-text.h
/usr/include/at-spi-2.0/atspi/atspi-types.h
/usr/include/at-spi-2.0/atspi/atspi-value.h
/usr/include/at-spi-2.0/atspi/atspi.h
/usr/lib64/libatspi.so
/usr/lib64/pkgconfig/atspi-2.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libatspi.so
/usr/lib32/pkgconfig/32atspi-2.pc
/usr/lib32/pkgconfig/atspi-2.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/libatspi/AtspiAccessible.html
/usr/share/gtk-doc/html/libatspi/AtspiDeviceListener.html
/usr/share/gtk-doc/html/libatspi/AtspiEventListener.html
/usr/share/gtk-doc/html/libatspi/AtspiHyperlink.html
/usr/share/gtk-doc/html/libatspi/AtspiMatchRule.html
/usr/share/gtk-doc/html/libatspi/AtspiObject.html
/usr/share/gtk-doc/html/libatspi/AtspiRelation.html
/usr/share/gtk-doc/html/libatspi/AtspiStateSet.html
/usr/share/gtk-doc/html/libatspi/annotation-glossary.html
/usr/share/gtk-doc/html/libatspi/api-index-full.html
/usr/share/gtk-doc/html/libatspi/ch01.html
/usr/share/gtk-doc/html/libatspi/home.png
/usr/share/gtk-doc/html/libatspi/index.html
/usr/share/gtk-doc/html/libatspi/left-insensitive.png
/usr/share/gtk-doc/html/libatspi/left.png
/usr/share/gtk-doc/html/libatspi/libatspi-AtspiApplication.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-action.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-collection.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-component.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-constants.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-document.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-editabletext.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-hypertext.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-image.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-listener-private.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-misc-private.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-misc.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-registry.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-selection.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-table-cell.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-table.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-text.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-types.html
/usr/share/gtk-doc/html/libatspi/libatspi-atspi-value.html
/usr/share/gtk-doc/html/libatspi/libatspi.devhelp2
/usr/share/gtk-doc/html/libatspi/object-tree.html
/usr/share/gtk-doc/html/libatspi/right-insensitive.png
/usr/share/gtk-doc/html/libatspi/right.png
/usr/share/gtk-doc/html/libatspi/style.css
/usr/share/gtk-doc/html/libatspi/up-insensitive.png
/usr/share/gtk-doc/html/libatspi/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libatspi.so.0
/usr/lib64/libatspi.so.0.0.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libatspi.so.0
/usr/lib32/libatspi.so.0.0.1

%files locales -f at-spi2-core.lang
%defattr(-,root,root,-)

