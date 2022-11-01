# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-ansible-lint
Epoch: 100
Version: 6.8.4
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
Requires: black >= 22.1.0
Requires: python3
Requires: python3-ansible-compat >= 2.2.1
Requires: python3-filelock
Requires: python3-jsonschema >= 4.9.0
Requires: python3-packaging
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
