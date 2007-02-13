#
%define		gst_major_ver	0.10
%define		_snap	200603282224
#
Summary:	GStreamer DLL loader plugin
Summary(pl.UTF-8):	Wtyczka wczytująca DLL dla GStreamera
Name: 		gstreamer-pitfdll
Version: 	0.9cvs
Release:	0.%{_snap}.3
License: 	GPL
Group:		Libraries/Multimedia
Source0:	pitfdll-%{_snap}.tar.bz2
# Source0-md5:	d591070cf7f57c557e5515b45c161a32
Patch0:		%{name}-codecs-path.patch
Patch1:		%{name}-am-prog-as.patch
URL:		http://ronald.bitfreak.net/pitfdll/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires: 	gstreamer-devel >= 0.10
BuildRequires: 	gstreamer-plugins-base >= 0.10
BuildRequires:	libtool
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         gstlibdir       %{_libdir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plug-ins.

This plugin contains a DLL loader to provide media playback for
proprietary formats.

%description -l pl.UTF-8
GStreamer to środowisko obróbki danych strumieniowych, bazujące na
grafie filtrów operujących na danych medialnych. Aplikacje używające
tej biblioteki mogą robić wszystko od przetwarzania dźwięku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego związanego z
mediami. Architektura bazująca na wtyczkach pozwala na łatwe dodawanie
nowych typów danych lub możliwości obróbki.

Ta wtyczka wczytuje biblioteki DLL do odtwarzania plików
multimedialnych o zamkniętych formatach.

%prep
%setup -q -n pitfdll
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README RELEASE TODO
%attr(755,root,root) %{gstlibdir}/libpitfdll.so
