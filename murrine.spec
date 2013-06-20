Name: 	 	murrine
Summary: 	Murrine GTK2 cairo theme
Version: 	0.98.2
Release: 	1
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
URL:		http://www.cimitan.com/murrine/
License:	GPLv2
Group:		Graphical desktop/GNOME
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	intltool
# Incorrectly named previous package was following library packaging rules,
# but a plugin is hardly a library
Obsoletes:	%{_lib}%{name}

%description
The Murrine engine is a cairo-based GTK2 theming tool.  It's very fast compared
to clearlooks-cairo.  Murrine includes animations and a unique style.

%prep
%setup -q

%build
export LDFLAGS="-lm"
%configure2_5x --enable-animation
%make
										
%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog
%{_datadir}/gtk-engines/murrine.xml
%{_libdir}/gtk-2.0/*/engines/libmurrine.so
