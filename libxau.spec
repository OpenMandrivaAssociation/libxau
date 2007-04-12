%define libxau %mklibname xau 6
Name: libxau
Summary: X authorization file management library
Version: 1.0.3
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXau-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X authorization file management library

#-----------------------------------------------------------

%package -n %{libxau}
Summary: X authorization file management library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxau}
X authorization file management library

#-----------------------------------------------------------

%package -n %{libxau}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxau} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxau-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxau}-devel
Development files for %{name}

%pre -n %{libxau}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxau}-devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/xau.pc
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.la
%{_libdir}/libXau.so
%{_mandir}/man3/Xau*

#-----------------------------------------------------------

%package -n %{libxau}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxau}-devel >= %{version}
Provides: libxau-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxau}-static-devel
Static development files for %{name}

%files -n %{libxau}-static-devel
%defattr(-,root,root)
%{_libdir}/libXau.a

#-----------------------------------------------------------

%prep
%setup -q -n libXau-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxau}
%defattr(-,root,root)
%{_libdir}/libXau.so.6
%{_libdir}/libXau.so.6.0.0


