Name:    ulogd
Version: 2.0.7
Release: 1%{?dist}
Summary: Userspace logging daemon for netfilter/iptables
License: GPLv2 
URL:     https://www.netfilter.org

Source0: https://www.netfilter.org/pub/ulogd2/ulogd-2.0.7.tar.bz2
Source1: %{name}.service
Source2: %{name}.conf
Source3: ulogd2.te

BuildArch:     x86_64
BuildRequires: gcc >= 8.3
BuildRequires: make >= 4.2.1
BuildRequires: libnfnetlink-devel >= 1.0.1
BuildRequires: libnetfilter_log-devel >= 1.0.1
BuildRequires: libnetfilter_conntrack-devel >= 1.0.7
BuildRequires: libmnl-devel >= 1.0.4
BuildRequires: libnetfilter_acct-devel >= 1.0.2
BuildRequires: community-mysql-devel >= 5.7.25
BuildRequires: postgresql-devel >= 10.7
BuildRequires: libdbi-devel >= 0.9.0
BuildRequires: libdbi >= 0.9.0
BuildRequires: libpcap-devel >= 1.9.0
BuildRequires: selinux-policy-targeted >= 3.14
BuildRequires: selinux-policy-devel >= 3.14
BuildRequires: checkpolicy >= 2.7
 
Requires: libnfnetlink >= 1.0.1
Requires: libnetfilter_log >= 1.0.1
Requires: libnetfilter_conntrack >= 1.0.7
Requires: libmnl >= 1.0.4
Requires: libnetfilter_acct >= 1.0.2
Requires: libdbi >= 0.9.0

%define _unpackaged_files_terminate_build 0 

%description
This packages is intended for doing all netfilter related logging inside a
userspace process

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}
make -f %{_datadir}/selinux/devel/Makefile -C %{_sourcedir} ulogd2%{?dist}.pp 

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__install} -d -m 0755 %{buildroot}%{_unitdir}
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
%{__install} -m 0600 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
%{__install} -d -m 0755 %{buildroot}%{_datadir}/ulogd/policy/selinux
%{__install} -m 0644 %{_sourcedir}/ulogd2%{?dist}.pp %{buildroot}%{_datadir}/ulogd/policy/selinux/ulogd2.pp

%pre
/usr/bin/getent group %{name} > /dev/null || /usr/sbin/groupadd -r %{name}
/usr/bin/getent passwd %{name} > /dev/null || /usr/sbin/useradd -r -d /var/lib/%{name} -s /sbin/nologin -g %{name} %{name}

%post
semodule -i %{_datadir}/ulogd/policy/selinux/ulogd2.pp

%postun
/usr/bin/getent group %{name} > /dev/null && /usr/sbin/groupdel %{name}
/usr/bin/getent passwd %{name} > /dev/null && /usr/sbin/userdel %{name}
semodule -r %{name}

%files
%license COPYING
%doc COPYING AUTHORS README
%defattr(-,%{name},%{name},-)
%attr(-,root,root) %{_sbindir}/%{name}
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_HWHDR.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IFINDEX.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IP2BIN.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IP2HBIN.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_IP2STR.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_MARK.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_PRINTFLOW.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_PRINTPKT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_filter_PWSNIFF.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inpflow_NFACCT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inpflow_NFCT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inppkt_NFLOG.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inppkt_ULOG.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_inppkt_UNIXSOCK.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_GPRINT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_GRAPHITE.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_LOGEMU.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_NACCT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_OPRINT.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_SYSLOG.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_XML.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_MYSQL.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_PCAP.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_output_PGSQL.so
%attr(-,root,root) %{_libdir}/%{name}/ulogd_raw2packet_BASE.so
%attr(-,root,root) %{_mandir}/man8/ulogd.8.gz
%attr(-,root,root) %{_unitdir}/%{name}.service
%attr(- root,root) %{_datadir}/ulogd/policy/selinux/ulogd2.pp
%{_sysconfdir}/%{name}/%{name}.conf

%changelog
* Sun Mar 13 2022 Edouard Camoin <edouard.camoin@gmail.com> 2.0.7-1
  - Differentiate SELinux module by Fedora version

* Wed Mar 9 2022 Edouard Camoin <edouard.camoin@gmail.com> 2.0.7-1
  - Adding SELinux module for ulogd

* Sun Feb 20 2022 Edouard Camoin <edouard.camoin@gmail.com> 2.0.7-1
  - Initial specfile
  - Compiling ulogd
  - Install ulogd
