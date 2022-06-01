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
%{__cp} /root/sobes666/Makefile %{_builddir}
%{__cp} /root/sobes666/raidix.c %{_builddir}


%build
make build


%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 raidix %{buildroot}/usr/bin/raidix
#make install


%files
/usr/bin/raidix


%changelog
* Tue May 31 2022 root
-
