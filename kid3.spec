Summary:	ID3 tag editor
Summary(pl.UTF-8):	Edytor etykiet ID3
Name:		kid3
Version:	1.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/kid3/%{name}-%{version}.tar.gz
# Source0-md5:	fd2b741a9a5145f813dd2b32ed04c818
URL:		http://kid3.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	flac-c++-devel
BuildRequires:	id3lib-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libtunepimp-devel
BuildRequires:	taglib-devel
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
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/apps/kid3
%dir %{_datadir}/apps/kid3/kid3ui.rc
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svgz
%{_desktopdir}/kde4/%{name}.desktop
%{_datadir}/dbus-1/interfaces/net.sourceforge.Kid3.xml
