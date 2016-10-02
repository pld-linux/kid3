#
# Conditional build:
%bcond_without	kde		# build without KDE4
%bcond_without	qt		# build without Qt
%bcond_without	cli		# build without CLI

Summary:	ID3 tag editor
Summary(pl.UTF-8):	Edytor etykiet ID3
Name:		kid3
Version:	3.4.2
Release:	0.3
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/kid3/%{name}-%{version}.tar.gz
# Source0-md5:	48c9dc602d26dd139c477d8cd90e78b6
URL:		http://kid3.sourceforge.net/
BuildRequires:	appstream-glib
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8
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
BuildRequires:	qcommandline-devel
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
	-DBUILD_SHARED_LIBS=ON \
	-DWITH_NO_MANCOMPRESS=ON \
	-DWITH_APPS="%{?with_qt:Qt;}%{?with_cli:CLI;}%{?with_kde:KDE;}" \
	-DWITH_CHROMAPRINT=ON \
	-DWITH_FFMPEG=ON \
	-DWITH_FLAC=ON \
	-DWITH_ID3LIB=ON \
	-DWITH_MP4V2=ON \
	-DWITH_PHONON=ON \
	-DWITH_QT4=ON \
	-DWITH_QT5=OFF \
	-DWITH_READLINE=ON \
	-DWITH_TAGLIB=ON \
	-DWITH_VORBIS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \

%if %{with kde}
%find_lang %{name}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files %{?with_kde:-f %{name}.lang}
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_libdir}/%{name}
%{_datadir}/%{name}

%if %{with cli}
%attr(755,root,root) %{_bindir}/kid3-cli
%{_mandir}/man1/kid3-cli.1
%lang(de) %{_mandir}/de/man1/kid3-cli.1
%endif

%if %{with qt}
%doc %lang(de) %{_docdir}/kid3-qt/kid3_de.html
%doc %{_docdir}/kid3-qt/kid3_en.html
%attr(755,root,root) %{_bindir}/kid3-qt
%{_mandir}/man1/kid3-qt.1
%lang(de) %{_mandir}/de/man1/kid3-qt.1
%{_iconsdir}/hicolor/*/apps/%{name}-qt.png
%{_iconsdir}/hicolor/*/apps/%{name}-qt.svg
%{_desktopdir}/%{name}-qt.desktop
%{_datadir}/appdata/kid3-qt.appdata.xml
%endif

%if %{with kde}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kid3
%{_mandir}/man1/kid3.1*
%lang(de) %{_mandir}/de/man1/kid3.1*
%{_iconsdir}/hicolor/*/apps/%{name}.svgz
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_desktopdir}/kde4/%{name}.desktop
%{_datadir}/appdata/kid3.appdata.xml
%{_datadir}/dbus-1/interfaces/net.sourceforge.Kid3.xml
%dir %{_datadir}/apps/kid3
%dir %{_datadir}/apps/kid3/kid3ui.rc
%endif
