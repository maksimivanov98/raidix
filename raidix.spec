Name:           raidix
Version:        1.1
Release:        1%{?dist}
Summary:        Program for Raidix
License:        GNU General Public License
URL:            https://github.com/maksimivanov98/raidix
BuildRequires:  gcc


%description
Simple software for company Raidix


%prep
%{__cp} $OLDPWD/Makefile %{_builddir}
%{__cp} $OLDPWD/raidix.c %{_builddir}


%build
make build


%install
make install


%files
/usr/bin/raidix


%changelog
* Tue May 31 2022 root
-
