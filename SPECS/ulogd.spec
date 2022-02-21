Name:    ulogd
Version: 2.0.7
Release: 1%{?dist}
Summary: Userspace logging daemon for netfilter/iptables
License: GPLv2 
URL:     https://www.netfilter.org

Source0: https://www.netfilter.org/pub/ulogd2/ulogd-2.0.7.tar.bz2
Source1: %{name}.service
Source2: %{name}.conf

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
%{__install} -d -m 0755 %{buildroot}%{_unitdir}
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
%{__install} -m 0600 %{_builddir}/%{name}-%{version}/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

%pre
/usr/bin/getent group %{name} > /dev/null || /usr/sbin/groupadd -r %{name}
/usr/bin/getent passwd %{name} > /dev/null || /usr/sbin/useradd -r -d /var/lib/%{name} -s /sbin/nologin -g %{name} %{name}

%files
%license COPYING
%doc COPYING AUTHORS README
%defattr(-,%{name},%{name},-)
%attr(-,root,root) %{_sbindir}/%{name}
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_HWHDR.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_HWHDR.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IFINDEX.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IFINDEX.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IP2BIN.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IP2BIN.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IP2HBIN.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IP2HBIN.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IP2STR.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IP2STR.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_MARK.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_MARK.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_PRINTFLOW.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_PRINTFLOW.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_PRINTPKT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_PRINTPKT.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_PWSNIFF.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_PWSNIFF.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inpflow_NFACCT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inpflow_NFACCT.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inpflow_NFCT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inpflow_NFCT.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inppkt_NFLOG.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inppkt_NFLOG.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inppkt_ULOG.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inppkt_ULOG.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inppkt_UNIXSOCK.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inppkt_UNIXSOCK.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_GPRINT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_GPRINT.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_GRAPHITE.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_GRAPHITE.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_LOGEMU.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_LOGEMU.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_NACCT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_NACCT.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_OPRINT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_OPRINT.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_SYSLOG.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_SYSLOG.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_XML.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_XML.la
%attr(-,root,root) %{_libdir}/%{name}/ulogd_raw2packet_BASE.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_raw2packet_BASE.la
%attr(-,root,root) %{_mandir}/man8/ulogd.8.gz
%attr(-,root,root) %{_unitdir}/%{name}.service
%{_sysconfdir}/%{name}/%{name}.conf

%changelog
* Sun Feb 20 2022 Edouard Camoin <edouard.camoin@gmail.com> 2.0.7-1
  - Initial specfile
  - Compiling ulogd
  - Install ulogd
