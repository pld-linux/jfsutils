Summary:	IBM JFS utility programs
Summary(pl):	Programy uøytkowe dla IBM JFS
Name:		jfsutils
Version:	1.0.11
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/%{name}-%{version}.tar.gz
URL:		http://oss.software.ibm.com/jfs/
BuildRequires:	autoconf
BuildRequires:	automake
%{?BOOT:BuildRequires:	uClibc-devel-BOOT}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Utilities to manage JFS filesystems.

%description -l pl
Programy do zarz±dzania systemem plikÛw JFS.

%if %{?BOOT:1}%{!?BOOT:0}
%package BOOT
Summary:	jfsutils for bootdisk (compiled against uClibc headers)
Summary(pl):	jfsutils dla bootkietki (skompilowane z uClibc)
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…

%description BOOT
jfsutils for bootdisk (compiled against uClibc headers).

%description BOOT -l pl
jfsutils dla bootkietki (skompilowane z uClibc).
%endif

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
autoheader
automake -a -c
%if %{?BOOT:1}%{!?BOOT:0}
# BOOT version
CFLAGS="%{rpmcflags} -Os -c -I%{_libdir}/bootdisk/usr/include"
%configure

%{__make} -C libfs
%{__make} -C mkfs CFLAGS="$BOOTCFLAGS" \
	LIBS="-nostdlib %{_libdir}/bootdisk/usr/lib/crt0.o %{_libdir}/bootdisk/usr/lib/libc.a -lgcc" \
	CC=%{__cc}

mv -f mkfs/mkfs.jfs mkfs.jfs-BOOT
%{__make} clean
%endif

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{?BOOT:1}%{!?BOOT:0}
# BOOT version
install -d $RPM_BUILD_ROOT/usr/lib/bootdisk/sbin
install mkfs.jfs-BOOT $RPM_BUILD_ROOT/usr/lib/bootdisk/sbin/mkfs.jfs
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/bootdisk/sbin/*
%endif
