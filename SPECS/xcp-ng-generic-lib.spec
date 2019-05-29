# handle debuginfo ourselves to keep the symbols in the main RPM
# we need this for good stacktraces in production
%global debug_package %{nil}

Name:           xcp-ng-generic-lib
Version:        1.1.0
Release:        3%{?dist}
Summary:        A library of algorithms, I/O and networking functions
License:        GPLv3
URL:            https://github.com/xcp-ng/xcp-ng-generic-lib
Source0:        https://github.com/xcp-ng/xcp-ng-generic-lib/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  binutils-devel

%description
A library of algorithms, I/O and networking functions... used by XCP-ng tools or daemons.

%prep
%autosetup -p1

%build
mkdir build
cd build
%cmake3 ..
make

%install
cd build
%make_install

%files
%license LICENSE
%{_libdir}/libxcp-ng-generic.so.1
%{_libdir}/libxcp-ng-generic.so.%{version}

%package devel
Summary:        Development headers for xcp-ng-generic-lib
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
A library of algorithms, I/O and networking functions... used by XCP-ng tools or daemons.

This package provides documentation and development headers for xcp-ng-generic-lib.

%files devel
%{_includedir}/xcp-ng/generic.h
%{_includedir}/xcp-ng/generic/algorithm.h
%{_includedir}/xcp-ng/generic/file.h
%{_includedir}/xcp-ng/generic/global.h
%{_includedir}/xcp-ng/generic/io.h
%{_includedir}/xcp-ng/generic/network.h
%{_includedir}/xcp-ng/generic/stacktrace.h
%{_includedir}/xcp-ng/generic/string.h
%{_libdir}/cmake/XcpNgGeneric/XcpNgGenericConfig.cmake
%{_libdir}/cmake/XcpNgGeneric/XcpNgGenericConfigVersion.cmake
%{_libdir}/cmake/XcpNgGeneric/XcpNgGenericTargets-noconfig.cmake
%{_libdir}/cmake/XcpNgGeneric/XcpNgGenericTargets.cmake
%{_libdir}/libxcp-ng-generic.so

%changelog
* Wed May 29 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.0-3
- Do not require the debuginfo package anymore
- Do not produce the debuginfo package at all for now

* Tue May 28 2019 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.1.0-1
- Update to 1.1.0

* Thu May 16 2019 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.0.0-1
- Initial package
