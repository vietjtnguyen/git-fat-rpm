Name:           git-fat
Version:        0.85_g83ab2b7

BuildArch:      noarch

Release:        1%{?dist}
Summary:        Simple way to handle fat files without committing them to git, supports synchronization using rsync

License:        BSD-2-Clause
URL:            https://github.com/jedbrown/git-fat
Source0:        https://raw.githubusercontent.com/jedbrown/git-fat/master/git-fat
Source1:        https://raw.githubusercontent.com/jedbrown/git-fat/master/LICENSE

Requires:       git
Requires:       python

%description
Checking large binary files into a source repository (Git or otherwise) is a bad idea because repository size quickly becomes unreasonable. Even if the instantaneous working tree stays manageable, preserving repository integrity requires all binary files in the entire project history, which given the typically poor compression of binary diffs, implies that the repository size will become impractically large. Some people recommend checking binaries into different repositories or even not versioning them at all, but these are not satisfying solutions for most workflows.

%prep
cd %{_builddir}
rm -rf %{name}-%{version}
cp %{_sourcedir}/* %{_builddir}/
#chown -R root.root .
chmod a+x %{_builddir}/git-fat
chmod -R a+rX,g-w,o-w .

%build

%install
mkdir -p %{buildroot}/%{_bindir}
cp %{_builddir}/git-fat %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_datarootdir}/%{name}
cp LICENSE %{buildroot}/%{_datarootdir}/%{name}/

%files
%{_bindir}/*
%doc %{_datarootdir}

%changelog
* Fri Mar 02 2017 Viet The Nguyen <vietjtnguyen@gmail.com> - 0.85_g83ab2b7-1
- Initial packaging
