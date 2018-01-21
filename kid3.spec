#
# Conditional build:
%bcond_without	kde		# build without KDE4
%bcond_without	qt		# build without Qt
%bcond_without	cli		# build without CLI

Summary:	ID3 tag editor
Summary(pl.UTF-8):	Edytor etykiet ID3
Name:		kid3
Version:	3.5.1
Release:	0.2
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/kid3/%{name}-%{version}.tar.gz
# Source0-md5:	48c9dc602d26dd139c477d8cd90e78b6
URL:		https://kid3.sourceforge.io/
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtDeclarative-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtXml-devel
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	docbook-style-xsl
BuildRequires:	flac-c++-devel
BuildRequires:	flac-devel
BuildRequires:	id3lib-devel
BuildRequires:	libchromaprint-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxslt-progs
BuildRequires:	mp4v2-devel
BuildRequires:	phonon-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake
BuildRequires:	readline-devel
BuildRequires:	taglib-devel >= 1.4
%if %{with kde}
BuildRequires:	automoc4
BuildRequires:	gettext-tools
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	qcommandline-devel
%endif
%if %{with qt} || %{with kde}
BuildRequires:	appstream-glib
%endif
Suggests:	xdg-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kid3 is an application to edit the ID3v1 and ID3v2 tags in MP3 files
in an efficient way. Also tags in Ogg/Vorbis, FLAC, MPC, MP4/AAC, MP2,
Speex, TrueAudio and WavPack files are supported. It is easy to set
tags of multiple files to the same values (e.g. album, artist, year
and genre in all files of the same album) and generate the tags from
the file name or vice versa.

%package cli
Summary:	Efficient Qt ID3 tag editor
Requires:	%{name} = %{version}-%{release}

%description cli
Efficient Qt ID3 tag editor.

%package qt
Summary:	Efficient Qt ID3 tag editor
Requires:	%{name} = %{version}-%{release}

%description qt
Efficient Qt ID3 tag editor.

%package kde
Summary:	Efficient Qt ID3 tag editor
Requires:	%{name} = %{version}-%{release}

%description kde
Efficient Qt ID3 tag editor.

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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/imports
%dir %{_libdir}/%{name}/plugins/imports/Kid3
%attr(755,root,root) %{_libdir}/%{name}/libkid3-core.so*
%attr(755,root,root) %{_libdir}/%{name}/libkid3-gui.so*
%{_libdir}/%{name}/plugins/imports/Kid3/Kid3Script.qml
%attr(755,root,root) %{_libdir}/%{name}/plugins/imports/Kid3/libkid3qml.so
%{_libdir}/%{name}/plugins/imports/Kid3/qmldir
%attr(755,root,root) %{_libdir}/%{name}/plugins/libacoustidimport.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libamazonimport.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libdiscogsimport.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libfreedbimport.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libid3libmetadata.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libmp4v2metadata.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libmusicbrainzimport.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/liboggflacmetadata.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libqmlcommand.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libtaglibmetadata.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/qml
%dir %{_datadir}/%{name}/qml/script
%{_datadir}/%{name}/qml/script/EmbedAlbumArt.qml
%{_datadir}/%{name}/qml/script/EmbedLyrics.qml
%{_datadir}/%{name}/qml/script/ExportCsv.qml
%{_datadir}/%{name}/qml/script/ExportHtmlPlayer.qml
%{_datadir}/%{name}/qml/script/ExtractAlbumArt.qml
%{_datadir}/%{name}/qml/script/ImportCsv.qml
%{_datadir}/%{name}/qml/script/QmlConsole.qml
%{_datadir}/%{name}/qml/script/ReplayGain2SoundCheck.qml
%{_datadir}/%{name}/qml/script/ResizeAlbumArt.qml
%{_datadir}/%{name}/qml/script/ShowTextEncodingV1.qml

%if %{with cli}
%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kid3-cli
%{_mandir}/man1/kid3-cli.1
%lang(de) %{_mandir}/de/man1/kid3-cli.1
%endif

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%doc %dir %{_docdir}/kid3-qt
%doc %lang(de) %{_docdir}/kid3-qt/kid3_de.html
%doc %{_docdir}/kid3-qt/kid3_en.html
%attr(755,root,root) %{_bindir}/kid3-qt
%{_mandir}/man1/kid3-qt.1
%lang(de) %{_mandir}/de/man1/kid3-qt.1
%{_iconsdir}/hicolor/*/apps/%{name}-qt.png
%{_iconsdir}/hicolor/*/apps/%{name}-qt.svg
%{_desktopdir}/%{name}-qt.desktop
%{_datadir}/metainfo/kid3-qt.appdata.xml
%endif

%if %{with kde}
%files kde -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kid3
%{_mandir}/man1/kid3.1*
%lang(de) %{_mandir}/de/man1/kid3.1*
%{_iconsdir}/hicolor/*/apps/%{name}.svgz
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_desktopdir}/kde4/%{name}.desktop
%{_datadir}/metainfo/kid3.appdata.xml
%{_datadir}/dbus-1/interfaces/net.sourceforge.Kid3.xml
%dir %{_datadir}/apps/kid3
%dir %{_datadir}/apps/kid3/kid3ui.rc
%endif
