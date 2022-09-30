Name:		jemalloc
Version:	5.3.0
Release:	1%{?dist}_netxms
Summary:	General-purpose scalable concurrent malloc implementation	

License:	BSD
URL:		https://github.com/jemalloc/jemalloc
Source0:	https://github.com/jemalloc/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	gcc
BuildRequires:	make

%description
General-purpose scalable concurrent malloc(3) implementation.
This distribution is built specifically for NetXMS packaging.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%ifarch %ix86 %arm x86_64
%define lg_page --with-lg-page=12
%endif

%ifarch ppc64 ppc64le aarch64
%define lg_page --with-lg-page=16
%endif

%build
%configure %{?lg_page}
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_datadir}/doc/%{name}/jemalloc.html

%files
%{_libdir}/libjemalloc.so.*
%{_bindir}/jemalloc.sh
%doc COPYING README VERSION

%files devel
%{_includedir}/jemalloc
%{_bindir}/jemalloc-config
%{_libdir}/pkgconfig/jemalloc.pc
%{_bindir}/jeprof
%{_libdir}/libjemalloc.so
%{_libdir}/libjemalloc.a
%{_libdir}/libjemalloc_pic.a
%{_mandir}/man3/jemalloc.3*

%ldconfig_scriptlets

%changelog
