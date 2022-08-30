# libxau is used by wine and steam -- 32bit compat libraries needed
%define major 6
%define libxau %mklibname xau %{major}
%define devname %mklibname xau -d
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif
%if %{with compat32}
%define lib32xau libxau%{major}
%define dev32name libxau-devel
%endif

Summary:	X authorization file management library
Name:		libxau
Version:	1.0.10
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXau-%{version}.tar.xz
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

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32xau}
Summary:	X authorization file management library (32-bit)
Group:		Development/X11
BuildRequires:	libc6

%description -n %{lib32xau}
X authorization file management library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32xau} = %{EVRD}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXau-%{version} -p1
export CONFIGURE_TOP=$(pwd)
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libxau}
%{_libdir}/libXau.so.%{major}*

%files -n %{devname}
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.so
%{_libdir}/pkgconfig/xau.pc
%doc %{_mandir}/man3/Xau*

%if %{with compat32}
%files -n %{lib32xau}
%{_prefix}/lib/libXau.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXau.so
%{_prefix}/lib/pkgconfig/*.pc
%endif
