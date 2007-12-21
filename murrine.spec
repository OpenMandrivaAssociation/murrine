%define name	murrine
%define version	0.53.1
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Murrine GTK2 cairo theme
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://cimi.netsons.org/pages/murrine.php
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk2-devel

%description
The Murrine engine is a cairo-based GTK2 theming tool.  It's very fast compared
to clearlooks-cairo.  Murrine includes animations and a unique style.

%prep
%setup -q

%build
%configure2_5x --enable-animation
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING CREDITS ChangeLog NEWS README
%{_libdir}/gtk-2.0/*/engines/libmurrine.so
%{_libdir}/gtk-2.0/*/engines/libmurrine.la

