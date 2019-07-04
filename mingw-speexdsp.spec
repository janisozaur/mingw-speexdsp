%{?mingw_package_header}

%global pkgname speexdsp

Name:           mingw-%{pkgname}
Version:        1.2.0
Release:        1%{?dist}
Summary:        A voice compression format (DSP)
Group:          Development/Libraries
License:        BSD
URL:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc


%description
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the DSP package, see the speex package for the codec part.


%package -n mingw32-%{pkgname}
Summary:        A voice compression format (DSP)

%description -n mingw32-%{pkgname}
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the DSP package, see the speex package for the codec part.


%package -n mingw64-%{pkgname}
Summary:        A voice compression format (DSP)

%description -n mingw64-%{pkgname}
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the DSP package, see the speex package for the codec part.


%{?mingw_debug_package}


%prep
%setup -q -n %{pkgname}-%{version}


%build
%{mingw_configure} --disable-static
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libspeexdsp-1.dll
%{mingw32_libdir}/libspeexdsp.dll.a
%{mingw32_libdir}/libspeexdsp.la
%{mingw32_libdir}/pkgconfig/speexdsp.pc
%{mingw32_libdir}/libspeexdsp.dll.a
%{mingw32_includedir}/speex/speex_echo.h
%{mingw32_includedir}/speex/speex_jitter.h
%{mingw32_includedir}/speex/speex_preprocess.h
%{mingw32_includedir}/speex/speex_resampler.h
%{mingw32_includedir}/speex/speexdsp_config_types.h
%{mingw32_includedir}/speex/speexdsp_types.h
%{mingw32_docdir}/speexdsp/manual.pdf

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libspeexdsp-1.dll
%{mingw64_libdir}/libspeexdsp.dll.a
%{mingw64_libdir}/libspeexdsp.la
%{mingw64_libdir}/pkgconfig/speexdsp.pc
%{mingw64_libdir}/libspeexdsp.dll.a
%{mingw64_includedir}/speex/speex_echo.h
%{mingw64_includedir}/speex/speex_jitter.h
%{mingw64_includedir}/speex/speex_preprocess.h
%{mingw64_includedir}/speex/speex_resampler.h
%{mingw64_includedir}/speex/speexdsp_config_types.h
%{mingw64_includedir}/speex/speexdsp_types.h
%{mingw64_docdir}/speexdsp/manual.pdf

# See https://fedoraproject.org/wiki/Packaging:MinGW

%changelog
* Thu Jul 04 2019 Michał Janiszewski <janisozaur+speexdspfedoramingw@gmail.com> - 1.2.0-1
- Initial MinGW packaging
