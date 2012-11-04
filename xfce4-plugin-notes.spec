%define		org_name	xfce4-notes-plugin
#
Summary:	Sticky notes plugin
Name:		xfce4-plugin-notes
Version:	1.7.7
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-notes-plugin/1.7/%{org_name}-%{version}.tar.bz2
# Source0-md5:	42b924b23f2fec6a1099e9b7a87db4a3
Patch0:		%{name}-xfce4ui.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/%{org_name}
BuildRequires:	Thunar-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkg-config
BuildRequires:	xfce4-dev-tools
BuildRequires:	xfce4-panel-devel
BuildRequires:	xfconf-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel
Requires:	xfconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The notes plugin provides you a quick way to write down
a todo list, to paste a piece of code, to leave a note
to your friend, or whatever else you had like to do.

%prep
%setup -qn %{org_name}-%{version}
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{org_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{org_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/xfce4-notes
%attr(755,root,root) %{_bindir}/xfce4-notes-settings
%attr(755,root,root) %{_bindir}/xfce4-popup-notes
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libnotes*
%{_datadir}/xfce4-notes-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-notes-plugin-47.desktop
%{_desktopdir}/xfce4-notes.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_sysconfdir}/xdg/autostart/xfce4-notes-autostart.desktop

