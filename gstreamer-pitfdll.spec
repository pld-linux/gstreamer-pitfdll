#
%define		gst_major_ver	0.10
%define		_snap	200603282224
#
Summary:	GStreamer DLL loader plugin
Summary(pl):	Wtyczka wczytuj±ca DLL dla GStreamera
Name: 		gstreamer-pitfdll
Version: 	0.9cvs
Release:	0.%{_snap}.1
License: 	GPL
Group: 		Libraries/Multimedia
Source0:	pitfdll-%{_snap}.tar.bz2
# Source0-md5:	d591070cf7f57c557e5515b45c161a32
URL:		http://ronald.bitfreak.net/pitfdll/
BuildRequires: 	gstreamer-devel >= 0.10
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

%description -l pl
GStreamer to ¶rodowisko obróbki danych strumieniowych, bazuj±ce na
grafie filtrów operuj±cych na danych medialnych. Aplikacje u¿ywaj±ce
tej biblioteki mog± robiæ wszystko od przetwarzania d¼wiêku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego zwi±zanego z
mediami. Architektura bazuj±ca na wtyczkach pozwala na ³atwe dodawanie
nowych typów danych lub mo¿liwo¶ci obróbki.

Ta wtyczka wczytuje biblioteki DLL do odtwarzania plików
multimedialnych o zamkniêtych formatach.

%prep
%setup -q -n pitfdll

%build
%{__aclocal} -I m4
%{__autoheader}
%{__libtoolize}
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
