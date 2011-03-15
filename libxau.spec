%define libxau %mklibname xau 6
%define develname %mklibname xau -d
%define staticname %mklibname xau -s -d

Name: libxau
Summary: X authorization file management library
Version: 1.0.6
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXau-%{version}.tar.bz2
Patch0: libxau-visibility.patch
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

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxau} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxau6-devel = %{version}-%{release}
Provides: libxau-devel = %{version}-%{release}
Obsoletes: %{_lib}xau6-devel < %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/pkgconfig/xau.pc
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.la
%{_libdir}/libXau.so
%{_mandir}/man3/Xau*

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} >= %{version}
Provides: libxau6-static-devel = %{version}-%{release}
Provides: libxau-static-devel = %{version}-%{release}
Obsoletes: %{_lib}xau6-static-devel < %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXau.a

#-----------------------------------------------------------

%prep
%setup -q -n libXau-%{version}

%patch0 -p1 -b .visibility

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libxau}
%defattr(-,root,root)
%{_libdir}/libXau.so.6
%{_libdir}/libXau.so.6.0.0


