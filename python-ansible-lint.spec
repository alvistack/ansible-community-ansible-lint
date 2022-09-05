%global debug_package %{nil}

Name: python-ansible-lint
Epoch: 100
Version: 6.4.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Best practices checker for Ansible
License: GPL-3.0-or-later
URL: https://github.com/ansible-community/ansible-lint/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Checks playbooks for practices and behavior that could potentially be
improved.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%package -n ansible-lint
Summary: Best practices checker for Ansible
Requires: ansible-core >= 2.12.0
Requires: python3
Requires: python3-ansible-compat >= 2.2.0
Requires: python3-enrich >= 1.2.6
Requires: python3-jsonschema >= 4.8.0
Requires: python3-packaging
Requires: python3-pytest
Requires: python3-pyyaml
Requires: python3-rich >= 9.5.1
Requires: python3-ruamel-yaml >= 0.15.34
Requires: python3-wcmatch >= 7.0
Requires: python3-yamllint >= 1.25.0
Provides: python3-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-lint) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-lint) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-lint) = %{epoch}:%{version}-%{release}

%description -n ansible-lint
Checks playbooks for practices and behavior that could potentially be
improved.

%files -n ansible-lint
%license COPYING
%{_bindir}/*
%{python3_sitelib}/*

%changelog
