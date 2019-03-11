%global debug_package %{nil}

Summary: Cisco OpenAppId
License: GNU General Public License
Group: Libraries/Network
Name: snort-openappid
Version: 308
Release: 1%{dist}
Source: snort-openappid.tar.gz
# Download from https://snort.org/downloads/openappid/9552
URL: http://www.snort.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: snort

%description
OpenAppId is an open, application-focused detection language and processing module for Snort that enables users to create, share, and implement application and service detection.

%prep
%setup -q -n odp

%build

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/snort/apps/odp
%{__mv} appid.conf appMapping.data version.conf libs lua port $RPM_BUILD_ROOT%{_sysconfdir}/snort/apps/odp/

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0644,root,root) %config %{_sysconfdir}/snort/apps/odp/appid.conf
%{_sysconfdir}/snort/apps/odp/appMapping.data
%{_sysconfdir}/snort/apps/odp/version.conf
%{_sysconfdir}/snort/apps/odp/libs
%{_sysconfdir}/snort/apps/odp/lua
%dir %{_sysconfdir}/snort/apps/odp/port
%doc AUTHORS
%doc LICENSE
%doc README

%changelog
* Mon Mar 11 2019 Nobuyuki Ito <info@2ito.com> - 308-1
- Initial release
