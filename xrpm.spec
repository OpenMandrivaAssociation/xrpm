%define name xrpm
%define version 2.2
%define release 14

Summary: 	An alternative package manager for RPMS
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
License: 	GPL
URL:		http://www.gmsys.com/xrpm.html
Group: System/Configuration/Packaging
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

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=/usr/bin/xrpm
Name=Xrpm
Comment=Tool for manipulating software packages
Icon=other_archiving
Categories=Settings;PackageManager;
EOF
 
%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus} 
%endif

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
%{_datadir}/applications/mandriva-*.desktop


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.2-13mdv2010.0
+ Revision: 435274
- rebuild

* Sat Aug 09 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.2-12mdv2009.0
+ Revision: 269843
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun May 11 2008 Funda Wang <fundawang@mandriva.org> 2.2-11mdv2009.0
+ Revision: 205515
- should not be noarch

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.2-10mdv2008.1
+ Revision: 135567
- auto-convert XDG menu entry
- fix menudir on x86_64
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import xrpm


* Sun Mar 20 2005 Michael Scherer <misc@mandrake.org> 2.2-10mdk
- fix 14407
- rpmlint warning

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.2-9mdk
- rebuild

* Thu Jan 30 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2-8mdk
- fix group
- fix hardcoded-library-path

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.2-7mdk
- rebuild

* Sun Jan 20 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-6mdk
- Fix menu entry

* Fri Aug 24 2001 Etienne Faure <etienne@mandrakesoft.com> 2.2-5mdk
- rebuild

* Wed Feb 21 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.2-4mdk
- rebuild

* Thu Sep 21 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2-3mdk
- rebuild

* Thu Aug 03 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2-2mdk
- BM

* Wed Jun 21 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2-1mdk
- new in contribs
