Summary:	IBM JFS utility programs
Summary:	Programy u¿ytkowe dla IBM JFS
Name:		jfsutils
Version:	1.0.8
Release:	2
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/%{name}-%{version}.tar.gz
Patch0:		jfsutils-BOOT.patch
URL:		http://oss.software.ibm.com/jfs
License:	GPL
%{?BOOT:BuildRequires:	uClibc-devel-BOOT}
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Utilities to manage JFS filesystems.

%description -l pl
Pragramy do zarz±dzania systemem plików JFS.

%if %{?BOOT:1}%{!?BOOT:0}
%package BOOT
Summary:	jfsutils for bootdisk (compiled against uClibc headers)
Group:		Development/Libraries
%description BOOT
jfsutils for bootdisk (compiled against uClibc headers).
%endif

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%if %{?BOOT:1}%{!?BOOT:0}
# BOOT version
BOOTCFLAGS="%{rpmcflags} -Os -c -I%{_libdir}/bootdisk/usr/include"
BOOTCFLAGS="$BOOTCFLAGS -D_PATH_MNTTAB=\\\"/etc/mtab\\\""
%{__make} -C libfs CFLAGS="$BOOTCFLAGS"
%{__make} -C mkfs CFLAGS="$BOOTCFLAGS" \
	LIBS="-nostdlib %{_libdir}/bootdisk/usr/lib/crt0.o %{_libdir}/bootdisk/usr/lib/libc.a -lgcc"
mv mkfs/mkfs.jfs mkfs.jfs-BOOT
%{__make} clean
%endif

%{__make} CFLAGS="%{rpmcflags} -Wall -c"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install output/* $RPM_BUILD_ROOT/%{_sbindir}
install */*.8 $RPM_BUILD_ROOT/%{_mandir}/man8

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
