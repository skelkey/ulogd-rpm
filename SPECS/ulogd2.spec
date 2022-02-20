Name:    ulogd
Version: 2.0.7
Release: 1%{?dist}
Summary: Userspace logging daemon for netfilter/iptables
License: GPLv2 
URL:     https://www.netfilter.org

Source0:    https://www.netfilter.org/pub/ulogd2/ulogd-2.0.7.tar.bz2
Source1:   %{name}.service

BuildArch:     x86_64
BuildRequires: gcc >= 8.3
BuildRequires: libnfnetlink-devel >= 1.0.1
BuildRequires: libnetfilter_log-devel >= 1.0.1
BuildRequires: libnetfilter_conntrack-devel >= 1.0.7
BuildRequires: libmnl-devel >= 1.0.4
BuildRequires: libnetfilter_acct-devel >= 1.0.2
 
Requires: libnfnetlink >= 1.0.1
Requires: libnetfilter_log >= 1.0.1
Requires: libnetfilter_conntrack >= 1.0.7
Requires: libmnl >= 1.0.4
Requires: libnetfilter_acct >= 1.0.2

%description
This packages is intended for doing all netfilter related logging inside a
userspace process

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%license COPYING
%{_bindir}/%{name}

%doc

%changelog
* Sun Feb 20 2022 Edouard Camoin <edouard.camoin@gmail.com> 2.0.7-1
  - Initial specfile
  - Compiling ulogd
  - Install ulogd
