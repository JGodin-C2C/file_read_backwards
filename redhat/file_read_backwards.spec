%global __python python3
%global srcname file_read_backwards

Name:           python3-%{srcname}
Version:        3.0.0
Release:        1%{?dist}
Summary:        Memory efficient way of reading files line-by-line from the end of file

License:        MIT
URL:            https://github.com/RobinNil/file_read_backwards
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:     noarch

BuildRequires:  python3-devel

%global _description %{expand:
This package is for reading file backward line by line as unicode in a memory efficient manner for both Python 2.7 and Python 3. }

%description %_description

%prep
%autosetup -c -n %{srcname}-%{version}

%build
pushd %{_builddir}/%{srcname}-%{version}/%{srcname}-%{version}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd

%install
pushd %{_builddir}/%{srcname}-%{version}/%{srcname}-%{version}
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd

%files
%{python3_sitelib}/*

%changelog
* Mon Dec 11 2023 Julien Godin <julien.godin@camptocamp.com>
-
