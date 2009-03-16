%define name	murrine
%define version	0.53.1
%define release %mkrel 5
%define libname %{_lib}%{name}

Name: 	 	%{name}
Summary: 	Murrine GTK2 cairo theme
Version: 	%{version}
Release: 	%{release}

Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
URL:		http://www.cimitan.com/murrine/
License:	GPLv2
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk2-devel
Requires:	%{libname}

%description
The Murrine engine is a cairo-based GTK2 theming tool.  It's very fast compared
to clearlooks-cairo.  Murrine includes animations and a unique style.

%package -n %{libname}
Summary:	Murrine GTK2 cairo theme
Group:		System/Libraries
Conflicts:	murrine < 0.53.1-2

%description -n %{libname}
The Murrine engine is a cairo-based GTK2 theming tool.  It's very fast compared
to clearlooks-cairo.  Murrine includes animations and a unique style.
This package contains the Murrine GTK+ engine itself.

%prep
%setup -q

%build
%configure --enable-animation
%make
										
%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS CREDITS ChangeLog

%files -n %{libname}
%{_libdir}/gtk-2.0/*/engines/libmurrine.so
%{_libdir}/gtk-2.0/*/engines/libmurrine.la

