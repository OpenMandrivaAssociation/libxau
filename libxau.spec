%define major 6
%define libxau %mklibname xau %{major}
%define develname %mklibname xau -d

Name:		libxau
Summary:	X authorization file management library
Version:	1.0.8
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXau-%{version}.tar.bz2
Patch0:		libxau-visibility.patch

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
X authorization file management library.

%package -n %{libxau}
Summary:	X authorization file management library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libxau}
X authorization file management library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxau} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}xau6-devel < 1.0.7
Obsoletes:	%{_lib}xau-static-devel < 1.0.7
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}.

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
%makeinstall_std

%files -n %{libxau}
%{_libdir}/libXau.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/xau.pc
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.so
%{_mandir}/man3/Xau*

%changelog
* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.7-2
+ Revision: 783347
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Wed Mar 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.7-1
+ Revision: 783200
- version update 1.0.7

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.6-5
+ Revision: 745498
- rebuild
- disabled static build
- removed .la files
- employed major macro
- cleaned up spec

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-4
+ Revision: 662420
- mass rebuild

* Tue Mar 15 2011 Funda Wang <fwang@mandriva.org> 1.0.6-3
+ Revision: 644853
- correct obsoletes

* Thu Feb 17 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.6-2
+ Revision: 638102
- dropped the the major from the devel and static pkg
- added proper obsoletes for old pkgs

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 1.0.6-1mdv2011.0
+ Revision: 556460
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2mdv2010.1
+ Revision: 520958
- rebuilt for 2010.1

* Mon Aug 31 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2010.0
+ Revision: 422875
- new release

* Wed Aug 27 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2009.0
+ Revision: 276516
- new release

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-6mdv2009.0
+ Revision: 264970
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 02 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-5mdv2009.0
+ Revision: 214365
- Rebuild to match corrections in xtrans.
- Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-4mdv2008.1
+ Revision: 151457
- Update BuildRequires and rebuild.
- Err, use "noop" the patch.
- This is a "noop" patch. But it can be considered a list of the functions,
  code from X Server uses from libXau, at a later stage, this library can be
  changed to make available only the public symbols.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Fri Feb 16 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-1mdv2007.0
+ Revision: 121716
- new release

* Thu Aug 03 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-1mdv2007.0
+ Revision: 42984
- new upstream release(1.0.2):
  * Minor cleanup release - added hooks for checking code with lint & sparse,
  and cleaned up several warnings from each.
- rebuild to fix cooker uploading
- X11R7.1
- increment release
- fixed more dependencies
- Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

