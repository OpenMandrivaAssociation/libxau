%define major 6
%define libxau %mklibname xau %{major}
%define devname %mklibname xau -d

Summary:	X authorization file management library
Name:		libxau
Version:	1.0.9
Release:	2
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXau-%{version}.tar.bz2
Patch0:		libxau-visibility.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
X authorization file management library.

%package -n %{libxau}
Summary:	X authorization file management library
Group:		Development/X11
Provides:	%{name} = %{version}

%description -n %{libxau}
X authorization file management library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxau} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -n libXau-%{version} -p1

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files -n %{libxau}
%{_libdir}/libXau.so.%{major}*

%files -n %{devname}
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.so
%{_libdir}/pkgconfig/xau.pc
%{_mandir}/man3/Xau*

