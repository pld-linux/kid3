Summary:	ID3 tag editor
Summary(pl.UTF-8):	Edytor etykiet ID3
Name:		kid3
Version:	3.4.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/kid3/%{name}-%{version}.tar.gz
# Source0-md5:	48c9dc602d26dd139c477d8cd90e78b6
URL:		http://kid3.sourceforge.net/
BuildRequires:	appstream-glib
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	flac-c++-devel
BuildRequires:	flac-devel
BuildRequires:	gettext
BuildRequires:	gstreamer-devel
BuildRequires:	id3lib-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libchromaprint-devel
BuildRequires:	libtunepimp-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mp4v2-devel
BuildRequires:	qt4-linguist
BuildRequires:	readline-devel
BuildRequires:	taglib-devel >= 1.4
Suggests:	xdg-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kid3 is an application to edit the ID3v1 and ID3v2 tags in MP3 files
in an efficient way. Also tags in Ogg/Vorbis, FLAC, MPC, MP4/AAC, MP2,
Speex, TrueAudio and WavPack files are supported. It is easy to set
tags of multiple files to the same values (e.g. album, artist, year
and genre in all files of the same album) and generate the tags from
the file name or vice versa.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DWITH_NO_MANCOMPRESS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/kid3
%attr(755,root,root) %{_bindir}/kid3-cli
%attr(755,root,root) %{_bindir}/kid3-qt
%{_mandir}/man1/kid3*.1*
%lang(de) %{_mandir}/de/man1/kid3*.1*
%dir %{_datadir}/apps/kid3
%dir %{_datadir}/apps/kid3/kid3ui.rc
%{_libdir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}-qt.png
%{_iconsdir}/hicolor/*/apps/%{name}.svgz
%{_iconsdir}/hicolor/*/apps/%{name}-qt.svg
%{_desktopdir}/kde4/%{name}.desktop
%{_desktopdir}/%{name}-qt.desktop
%{_datadir}/dbus-1/interfaces/net.sourceforge.Kid3.xml
%{_datadir}/appdata/kid3.appdata.xml
%{_datadir}/appdata/kid3-qt.appdata.xml
%{_datadir}/%{name}
