%define name xrpm
%define version 2.2
%define release 10mdk

Summary: 	An alternative package manager for RPMS
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
License: 	GPL
URL:		http://www.gmsys.com/xrpm.html
Group: System/Configuration/Packaging
BuildArch:  noarch
Requires: tix tkinter

%description
XRPM-2.2 is an alternative tool for manipulating software packages built
with RedHat's RPM package management tool. XRPM will allow you to list
and install packages from directories and FTP sites.

%prep

%setup
perl -pi -e 's/UseTUseLog/UseTkman/' xrpm.conf

%install
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT%_libdir/xrpm
cp ftp-sites $RPM_BUILD_ROOT/etc
cp xrpm.conf $RPM_BUILD_ROOT/etc
cp xrpm $RPM_BUILD_ROOT/usr/bin
cp file.gif $RPM_BUILD_ROOT%_libdir/xrpm
cp findrpm.py $RPM_BUILD_ROOT%_libdir/xrpm
cp ftputil.py $RPM_BUILD_ROOT%_libdir/xrpm
cp gmsgui.py $RPM_BUILD_ROOT%_libdir/xrpm
cp gmsutil.py $RPM_BUILD_ROOT%_libdir/xrpm
cp gui.py $RPM_BUILD_ROOT%_libdir/xrpm
cp help.py $RPM_BUILD_ROOT%_libdir/xrpm
cp info.gif $RPM_BUILD_ROOT%_libdir/xrpm
cp install.gif $RPM_BUILD_ROOT%_libdir/xrpm
cp license $RPM_BUILD_ROOT%_libdir/xrpm
cp manual $RPM_BUILD_ROOT%_libdir/xrpm
cp menu.py $RPM_BUILD_ROOT%_libdir/xrpm
cp quit.gif $RPM_BUILD_ROOT%_libdir/xrpm
cp remove.gif $RPM_BUILD_ROOT%_libdir/xrpm
cp rpm.py $RPM_BUILD_ROOT%_libdir/xrpm
cp xrpm.py $RPM_BUILD_ROOT%_libdir/xrpm

(cd $RPM_BUILD_ROOT
mkdir -p .%_libdir/menu
cat > .%_libdir/menu/%{name} <<EOF
?package(%{name}):\
command="/usr/bin/xrpm"\
title="Xrpm"\
longtitle="Tool for manipulating software packages"\
needs="x11"\
icon="other_archiving.png"\
section="Configuration/Packaging"
EOF
)
 
%post
%{update_menus}
 
%postun
%{clean_menus} 

%clean
rm -rf $RPM_BUILD_ROOT/

%files
%defattr(-,root,root)
%doc CHANGES LICENSE NEWS todo
%config(noreplace) /etc/ftp-sites
%config(noreplace) /etc/xrpm.conf
/usr/bin/xrpm
%_libdir/xrpm/file.gif
%_libdir/xrpm/findrpm.py
%_libdir/xrpm/ftputil.py
%_libdir/xrpm/gmsgui.py
%_libdir/xrpm/gmsutil.py
%_libdir/xrpm/gui.py
%_libdir/xrpm/help.py
%_libdir/xrpm/info.gif
%_libdir/xrpm/install.gif
%_libdir/xrpm/license
%_libdir/xrpm/manual
%_libdir/xrpm/menu.py
%_libdir/xrpm/quit.gif
%_libdir/xrpm/remove.gif
%_libdir/xrpm/rpm.py
%_libdir/xrpm/xrpm.py
%{_menudir}/*

