Name:		elementary-gnome-icon-theme		
Version:	0.1.1
Release:	1%{?dist}
Summary:	Icons from the elementary project, improved for GNOME

License:	GPLv3
URL:		https://github.com/embik/elementary-gnome-icons
Source0:	https://github.com/embik/elementary-gnome-icons/archive/v%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake

BuildArch:	noarch

%description
This package contains the elementary icon theme, improved for usage with the GNOME desktop.

%prep
%setup -q -n elementary-gnome-icons-%{version}


%build
[ -x autogen.sh ] && NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags}


%install
%make_install

touch $RPM_BUILD_ROOT%{_datadir}/icons/elementary-gnome/icon-theme.cache

%post
touch --no-create %{_datadir}/icons/elementary-gnome &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
	touch --no-create %{_datadir}/icons/elementary-gnome &>/dev/null
	gtk-update-icon-cache %{_datadir}/icons/elementary-gnome &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/elementary-gnome &>/dev/null || :

%files
%doc README.md AUTHORS CONTRIBUTORS
%license COPYING*
%{_datadir}/icons/elementary-gnome/*
%ghost %{_datadir}/icons/elementary-gnome/icon-theme.cache

%changelog
* Sat Feb 20 2016 Marvin Beckers <mail@embik.me> - 0.1.1-1
- Merge upstream revisions (minor improvements)
* Sun Dec 27 2015 Marvin Beckers <beckersmarvin@gmail.com> - 0.1.0-1
- Initial RPM release for Fedora

