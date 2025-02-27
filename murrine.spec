Summary:	GTK2 cairo theme
Name:		murrine
Version:	0.98.2
Release:	13
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		https://www.cimitan.com/murrine/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
Patch0:		https://src.fedoraproject.org/rpms/gtk-murrine-engine/raw/rawhide/f/gtk-murrine-engine_possible-wnck-applet-crash.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)
# Incorrectly named previous package was following library packaging rules,
# but a plugin is hardly a library
Obsoletes:	%{_lib}%{name} < 0.98.2-12

%description
The Murrine engine is a cairo-based GTK2 theming tool.  It's very fast compared
to clearlooks-cairo.  Murrine includes animations and a unique style.

%prep
%autosetup -p1

%build
export LDFLAGS="-lm"
%configure \
	--enable-animation \
	--enable-animationrtl

%make_build
										
%install
%make_install
 
#remove .la files
find %{buildroot} -name *.la | xargs rm -f || true
#fix permission
find %{buildroot}%{_datadir}/themes -type f | xargs chmod 0644 || true

%files
%doc AUTHORS ChangeLog
%{_datadir}/gtk-engines/murrine.xml
%{_libdir}/gtk-2.0/*/engines/libmurrine.so
