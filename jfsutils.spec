#
# Conditional build:
%bcond_without	fsck	# don't build fsck.jfs (as it requires pthread)
#
Summary:	IBM JFS utility programs
Summary(pl):	Programy u¿ytkowe dla IBM JFS
Name:		jfsutils
Version:	1.1.11
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://jfs.sourceforge.net/project/pub/%{name}-%{version}.tar.gz
# Source0-md5:	a741298f1d79f0ceb52f0187614e889e
URL:		http://jfs.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libuuid-devel
Obsoletes:	jfsprogs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Utilities to manage JFS filesystems.

%description -l pl
Programy do zarz±dzania systemem plików JFS.

%prep
%setup -q
%{!?with_fsck:cp Makefile.am Makefile.am.tmp}
%{!?with_fsck:sed -e 's/ fsck / /' Makefile.am.tmp > Makefile.am}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
