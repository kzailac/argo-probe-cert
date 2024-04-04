%define dir /usr/libexec/argo/probes/cert

Summary: ARGO probe for checking X509 certificate lifetime.
Name: argo-probe-cert
Version: 2.0.1
Release: 1%{?dist}
License: ASL 2.0
Group: Network/Monitoring
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{dir}
install --mode 755 ./CertLifetime-probe  ${RPM_BUILD_ROOT}%{dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{dir}/CertLifetime-probe

%changelog
* Thu Apr 4 2024 Katarina Zailac <kzailac@srce.hr> - 2.0.1-1%{?dist}
- AO-924 Create Rocky 9 rpm for argo-probe-cert
* Mon Sep 5 2022 Katarina Zailac <kzailac@srce.hr> - 2.0.0-1%{?dist}
- AO-651 Harmonize EGI probes
* Thu Dec 15 2016 Emir Imamagic <eimamagi@srce.hr> - 1.0.0-1%{?dist}
- Initial version
