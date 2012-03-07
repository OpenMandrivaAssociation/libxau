%define major 6
%define libxau %mklibname xau %{major}
%define develname %mklibname xau -d

Name: libxau
Summary: X authorization file management library
Version: 1.0.7
Release: 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXau-%{version}.tar.bz2
Patch0: libxau-visibility.patch

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X authorization file management library

%package -n %{libxau}
Summary: X authorization file management library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxau}
X authorization file management library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxau} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}xau6-devel
Obsoletes: %{_lib}xau-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXau-%{version}
%patch0 -p1 -b .visibility

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxau}
%{_libdir}/libXau.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/xau.pc
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.so
%{_mandir}/man3/Xau*

