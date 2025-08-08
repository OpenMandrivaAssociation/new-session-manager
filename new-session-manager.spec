%define	oname	nsm

Summary:	Music production session manager
Name:		new-session-manager
Version:	1.6.1
Release:	1
License:	GPLv3+
Group:		Sound
Url:		https://github.com/linuxaudio/new-session-manager
Source0:	https://github.com/linuxaudio/new-session-manager/archive/v%{version}/%{name}-%{version}.tar.gz
#BuildRequires:	desktop-file-utils
BuildRequires:	meson
BuildRequires:	fltk-fluid
BuildRequires:	ninja
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(xpm)
Requires:	jackit
Requires:	hicolor-icon-theme
Provides:	nsm = %{EVRD}

%description
New Session Manager (NSM) is a tool to assist music production by grouping
standalone programs into sessions. You can create a session, or project, add
programs to it and then use commands to save, start/stop, hide/show all
programs at once, or individually. At a later date you can then re-open the
session and continue where you left off. All files belonging to the session
will be saved in the same directory.
It's a drop-in replacement for the non-session-manager daemon nsmd and related
tools (e.g. jackpatch) and has the goal of be upwards and downwards compatible
with the original nsmd.

%files
%license COPYING
%doc CHANGELOG README.md
%doc docs/index.html docs/api/api-index.html
%{_bindir}/nsmd
%{_bindir}/jackpatch
%{_bindir}/non-session-manager
%{_bindir}/%{oname}-legacy-gui
%{_bindir}/%{oname}-proxy
%{_bindir}/%{oname}-proxy-gui
%{_datadir}/applications/org.jackaudio.%{oname}-legacy-gui.desktop
%{_datadir}/applications/org.jackaudio.%{oname}-proxy.desktop
%{_datadir}/applications/org.jackaudio.jackpatch.desktop
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_mandir}/man1/*.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

# Rename doc file to avoid conflicts
cp docs/api/index.html docs/api/api-index.html


%build
%meson
%meson_build


%install
%meson_install

rm -rf %{buildroot}%{_docdir}/%{name}/*
