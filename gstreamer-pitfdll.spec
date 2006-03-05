#
%define		gst_major_ver	0.8
#
Summary:	GStreamer DLL loader plugin
Name: 		gstreamer-pitfdll
Version: 	0.8.2
Release:	1
License: 	GPL
Group: 		Libraries/Multimedia
Source0:	http://dl.sourceforge.net/pitfdll/pitfdll-%{version}.tar.bz2
# Source0-md5:	7de1810082c55b8433190ac75b9456a9
URL:		http://ronald.bitfreak.net/pitfdll/
BuildRequires: 	gstreamer-devel >= 0.7.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         gstlibdir       %{_libdir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related. Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This plugin contains a DLL loader to provide media playback for proprietary
formats.

%prep
%setup -q -n pitfdll-%{version}

%build
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
%doc AUTHORS COPYING README
%attr(755,root,root) %{gstlibdir}/libpitfdll.so
