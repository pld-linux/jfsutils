Summary:	IBM JFS utility programs
Summary:	Programy u¿ytkowe dla IBM JFS
Name:		jfsutils
Version:	1.0.6
Release:	1
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/%{name}-%{version}.tar.gz
URL:		http://oss.software.ibm.com/jfs
License:	GPL
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Utilities to manage JFS filesystems.

%description -l pl
Pragramy do zarz±dzania systemem plików JFS.

%prep
%setup -q -n %{name}

%build
%{__make} CFLAGS="%{rpmcflags} -Wall -c"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install output/* $RPM_BUILD_ROOT/%{_sbindir}
install */*.8 $RPM_BUILD_ROOT/%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
