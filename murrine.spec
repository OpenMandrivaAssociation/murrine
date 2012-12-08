%define name	murrine
%define version	0.98.2
%define release 1
%define libname %{_lib}%{name}

Name: 	 	%{name}
Summary: 	Murrine GTK2 cairo theme
Version: 	%{version}
Release: 	%{release}

Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
URL:		http://www.cimitan.com/murrine/
License:	GPLv2
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk2-devel
BuildRequires:	intltool
Requires:	%{libname}

%description
The Murrine engine is a cairo-based GTK2 theming tool.  It's very fast compared
to clearlooks-cairo.  Murrine includes animations and a unique style.

%package -n %{libname}
Summary:	Murrine GTK2 cairo theme
Group:		System/Libraries
Conflicts:	murrine < 0.53.1-2
Requires:	%name >= %version

%description -n %{libname}
The Murrine engine is a cairo-based GTK2 theming tool.  It's very fast compared
to clearlooks-cairo.  Murrine includes animations and a unique style.
This package contains the Murrine GTK+ engine itself.

%prep
%setup -q

%build
%configure2_5x --enable-animation
%make
										
%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%_datadir/gtk-engines/murrine.xml

%files -n %{libname}
%{_libdir}/gtk-2.0/*/engines/libmurrine.so



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.98.1.1-2mdv2011.0
+ Revision: 666501
- mass rebuild

* Mon Oct 04 2010 Götz Waschk <waschk@mandriva.org> 0.98.1.1-1mdv2011.0
+ Revision: 582995
- update to new version 0.98.1.1

* Fri Oct 01 2010 Götz Waschk <waschk@mandriva.org> 0.98.1-1mdv2011.0
+ Revision: 582367
- update to new version 0.98.1

* Wed Sep 22 2010 Götz Waschk <waschk@mandriva.org> 0.98.0-1mdv2011.0
+ Revision: 580562
- new version
- fix build

* Thu May 14 2009 Jérôme Brenier <incubusss@mandriva.org> 0.90.3-1mdv2010.0
+ Revision: 375606
- update to new version 0.90.3

* Thu Mar 19 2009 Götz Waschk <waschk@mandriva.org> 0.90.2-1mdv2009.1
+ Revision: 357661
- update to new version 0.90.2

* Wed Mar 18 2009 Götz Waschk <waschk@mandriva.org> 0.90.1-1mdv2009.1
+ Revision: 357274
- update to new version 0.90.1

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 0.90.0-1mdv2009.1
+ Revision: 355634
- fix build deps
- new version
- update file list
- update deps
- update source URL

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.53.1-5mdv2009.0
+ Revision: 253367
- rebuild

* Wed Mar 26 2008 Emmanuel Andry <eandry@mandriva.org> 0.53.1-3mdv2008.1
+ Revision: 190545
- Fix lib group

* Sat Feb 23 2008 Frederik Himpe <fhimpe@mandriva.org> 0.53.1-2mdv2008.1
+ Revision: 174080
- Libify in order to fix bug #35470 (32 and 64 bit versions cannot be
  installed together because of conflicts)
- New URL
- New license policy
- Remove some uninteresting doc files

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 28 2007 Austin Acton <austin@mandriva.org> 0.53.1-1mdv2008.0
+ Revision: 72879
- Import murrine

