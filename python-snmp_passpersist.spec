%define 	module	snmp_passpersist
Summary:	Python implementation a pass_persist backend for Net-SNMP
Name:		python-%{module}
Version:	1.2.2
Release:	2
License:	GPL v3
Group:		Development/Languages/Python
Source0:	https://github.com/nagius/snmp_passpersist/archive/v%{version}.tar.gz
# Source0-md5:	b57210dbac1c94c0926ecb9481840276
URL:		http://github.com/nagius/snmp_passpersist
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a SNMP passpersist backend for Net-SNMP.

The snmp_passpersist.PassPersist class present a convenient way to
creare a MIB subtree and expose it to snmp via it's passpersist
protocol.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*.py*
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/*.egg-info
%endif
