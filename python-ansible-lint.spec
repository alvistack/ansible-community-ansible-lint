%global debug_package %{nil}

Name: python-ansible-lint
Epoch: 100
Version: 5.3.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Best practices checker for Ansible
License: MIT
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
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-ansible-lint
Summary: Best practices checker for Ansible
Requires: python3
Requires: python3-enrich >= 1.2.6
Requires: python3-packaging
Requires: python3-PyYAML
Requires: python3-rich >= 9.5.1
Requires: python3-ruamel.yaml >= 0.15.34
Requires: python3-tenacity
Requires: python3-typing-extensions
Requires: python3-wcmatch >= 7.0
Provides: python3-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-lint) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-lint) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-lint) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-ansible-lint
Checks playbooks for practices and behavior that could potentially be
improved.

%files -n python%{python3_version_nodots}-ansible-lint
%license LICENSE
%{_bindir}/ansible-lint*
%{python3_sitelib}/ansible_lint*
%{python3_sitelib}/ansiblelint*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-ansible-lint
Summary: Best practices checker for Ansible
Requires: python3
Requires: python3-enrich >= 1.2.6
Requires: python3-packaging
Requires: python3-PyYAML
Requires: python3-rich >= 9.5.1
Requires: python3-ruamel.yaml >= 0.15.34
Requires: python3-tenacity
Requires: python3-typing-extensions
Requires: python3-wcmatch >= 7.0
Provides: python3-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-lint) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-lint) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-lint) = %{epoch}:%{version}-%{release}

%description -n python3-ansible-lint
Checks playbooks for practices and behavior that could potentially be
improved.

%files -n python3-ansible-lint
%license LICENSE
%{_bindir}/ansible-lint*
%{python3_sitelib}/ansible_lint*
%{python3_sitelib}/ansiblelint*
%endif

%if 0%{?centos_version} == 700
%package -n ansible-lint
Summary: Best practices checker for Ansible
Requires: python3
Requires: python3-enrich >= 1.2.6
Requires: python3-packaging
Requires: python3-pyyaml
Requires: python3-rich >= 9.5.1
Requires: python3-ruamel-yaml >= 0.15.34
Requires: python3-tenacity
Requires: python3-typing-extensions
Requires: python3-wcmatch >= 7.0
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
%license LICENSE
%{_bindir}/ansible-lint*
%{python3_sitelib}/ansible_lint*
%{python3_sitelib}/ansiblelint*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000) && !(0%{?centos_version} == 700)
%package -n python3-ansible-lint
Summary: Best practices checker for Ansible
Requires: python3
Requires: python3-enrich >= 1.2.6
Requires: python3-packaging
Requires: python3-pyyaml
Requires: python3-rich >= 9.5.1
Requires: python3-ruamel-yaml >= 0.15.34
Requires: python3-tenacity
Requires: python3-typing-extensions
Requires: python3-wcmatch >= 7.0
Provides: python3-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-lint) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-lint) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-lint = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-lint) = %{epoch}:%{version}-%{release}

%description -n python3-ansible-lint
Checks playbooks for practices and behavior that could potentially be
improved.

%files -n python3-ansible-lint
%license LICENSE
%{_bindir}/ansible-lint*
%{python3_sitelib}/ansible_lint*
%{python3_sitelib}/ansiblelint*
%endif

%changelog
