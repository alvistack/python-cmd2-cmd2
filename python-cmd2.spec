# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
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

%global source_date_epoch_from_changelog 0

Name: python-cmd2
Epoch: 100
Version: 2.5.7
Release: 1%{?dist}
BuildArch: noarch
Summary: Tool for building interactive command line apps
License: MIT
URL: https://github.com/python-cmd2/cmd2/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
cmd2 is a tool for building interactive command line applications in
Python. Its goal is to make it quick and easy for developers to build
feature-rich and user-friendly interactive command line applications. It
provides a simple API which is an extension of Python's built-in cmd
module. cmd2 provides a wealth of features on top of cmd to make your
life easier and eliminates much of the boilerplate code which would be
necessary when using cmd.

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

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-cmd2
Summary: Tool for building interactive command line apps
Requires: python3
Requires: python3-attrs >= 16.3.0
Requires: python3-importlib-metadata >= 1.6.0
Requires: python3-pyperclip >= 1.6
Requires: python3-typing-extensions
Requires: python3-wcwidth >= 0.1.7
Provides: python3-cmd2 = %{epoch}:%{version}-%{release}
Provides: python3dist(cmd2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cmd2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cmd2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cmd2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cmd2) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-cmd2
cmd2 is a tool for building interactive command line applications in
Python. Its goal is to make it quick and easy for developers to build
feature-rich and user-friendly interactive command line applications. It
provides a simple API which is an extension of Python's built-in cmd
module. cmd2 provides a wealth of features on top of cmd to make your
life easier and eliminates much of the boilerplate code which would be
necessary when using cmd.

%files -n python%{python3_version_nodots}-cmd2
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-cmd2
Summary: Tool for building interactive command line apps
Requires: python3
Requires: python3-attrs >= 16.3.0
Requires: python3-importlib-metadata >= 1.6.0
Requires: python3-pyperclip >= 1.6
Requires: python3-typing-extensions
Requires: python3-wcwidth >= 0.1.7
Provides: python3-cmd2 = %{epoch}:%{version}-%{release}
Provides: python3dist(cmd2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cmd2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cmd2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cmd2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cmd2) = %{epoch}:%{version}-%{release}

%description -n python3-cmd2
cmd2 is a tool for building interactive command line applications in
Python. Its goal is to make it quick and easy for developers to build
feature-rich and user-friendly interactive command line applications. It
provides a simple API which is an extension of Python's built-in cmd
module. cmd2 provides a wealth of features on top of cmd to make your
life easier and eliminates much of the boilerplate code which would be
necessary when using cmd.

%files -n python3-cmd2
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
