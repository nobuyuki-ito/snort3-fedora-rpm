%define version 2.2.2

Summary: Data Acquisition Library
License: GNU General Public License
Group: Libraries/Network
Name: daq
Provides: daq
Release: 1%{dist}
Source: daq-%{version}.tar.gz
URL: http://www.snort.org/
Version: %{version}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: libpcap
BuildRequires: autoconf, automake, flex, gcc, bison, libpcap-devel

%description
Data Acquisition library for Snort.

%package devel
Summary: Development tools for programs to Data Acquisition (DAQ) Library

%description devel
Development tools for programs to Data Acquisition (DAQ) Library


%prep
%setup -q

%build
%configure
%{__make}

%install
%{make_install}

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/*.so*
%{_libdir}/daq/*.so*
%doc ChangeLog
%doc COPYING
%doc README

%files devel
%attr(0755,root,root) %{_bindir}/daq-modules-config
%{_includedir}/*.h
%{_libdir}/*.{a,la}
%{_libdir}/daq/*.{a,la}

%changelog
* Sun Mar 3 2019 Nobuyuki Ito <info@2ito.com> - 2.2.2-1
- Fixed spec file for 2.2.2 and Fedora 29
