# conditional build
#  --without fsck -- don't build fsck.jfs (as it requires pthread)
Summary:	IBM JFS utility programs
Summary(pl):	Programy u¿ytkowe dla IBM JFS
Name:		jfsutils
Version:	1.0.17
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/%{name}-%{version}.tar.gz
URL:		http://oss.software.ibm.com/jfs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	jfsprogs

%define		_sbindir	/sbin

%description
Utilities to manage JFS filesystems.

%description -l pl
Programy do zarz±dzania systemem plików JFS.

%prep
%setup -q
%{?_without_fsck:cp Makefile.am Makefile.am.tmp}
%{?_without_fsck:sed -e 's/ fsck / /' Makefile.am.tmp > Makefile.am}

%build
rm -f missing
aclocal
%{__autoconf}
autoheader
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
