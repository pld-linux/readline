Summary:	Library for reading lines from a terminal
Summary(de):	Library zum Lesen von Zeilen von einem Terminal
Summary(fr):	Bibliothéque pour lire des lignes depuis un terminal.
Summary(pl):	Biblioteki do czytania lini z terminala
Summary(tr):	Terminalden satýr okumak için kullanýlan bir kitaplýk
Name:		readline
Version:	4.0
Release:	3
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		readline-shared.patch
Patch1:		readline-info.patch
Prereq:		/sbin/install-info
Requires:	ncurses >= 4.2-12
Buildprereq:	ncurses-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
The "readline" library will read a line from the terminal and return it,
allowing the user to edit the line with the standard emacs editing keys.
It allows the programmer to give the user an easier-to-use and more
intuitive interface.

%package devel
Summary:	file for developing programs that use the readline library
Summary(de):	Datei zum Entwickeln von Programmen mit der readline-Library
Summary(fr):	Fichier pour développer des programmes utilisant la librairie readline.
Summary(pl):	Pakiet dla programistów u¿ywaj±cych bibliotek readline'a
Summary(tr):	readline kitaplýðýný kullanan programlar yazmak için gerekli dosyalar
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The "readline" library will read a line from the terminal and return it,
using prompt as a prompt.  If prompt is null, no prompt is issued.  The
line returned is allocated with malloc(3), so the caller must free it when
finished.  The line returned has the final newline removed, so only the
text of the line remains.

%description -l pl devel

Biblioteka readline czyta linie z terminala i zwracaj± j±, u¿ywaj±c znaku
zachêty (prompt) jako podpowiedzi. Je¿eli prompt jest zerem, nie jest
wówczas wynikiowy.  Linia zwracana jest allokowana przez malloc(3).

%package static
Summary:	Static readline library
Summary(pl):	Biblioteka statyczna readline
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package contains sattic version readline library.

%description -l pl static
Pakiet ten zawiera wersjê statycznê biblioteki readline.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr \
	--with-curses

make static shared

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib

make install install-shared prefix=$RPM_BUILD_ROOT/usr

mv $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* $RPM_BUILD_ROOT/lib 
ln -sf ../../lib/libreadline.so.4.0 $RPM_BUILD_ROOT%{_libdir}/libreadline.so
ln -sf ../../lib/libhistory.so.4.0 $RPM_BUILD_ROOT%{_libdir}/libhistory.so

strip $RPM_BUILD_ROOT/lib/lib*.so.*.*

gzip -nf9 $RPM_BUILD_ROOT/usr/{info/*info*,man/man3/*}

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/history.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/readline.info.gz /etc/info-dir

%postun -p /sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/history.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/readline.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /lib/lib*.so.*.*
%{_infodir}/*info*

%files devel
%defattr(644,root,root,755)
%{_includedir}/readline
%{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Tue Apr 20 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.0-3]
- removed "Conflicts: glibc <= 2.0.7" (not neccessary now),
- added Buildprereq: ncurses-devel,
- recompiles on new rpm.

* Sat Feb 27 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.0-2]
- added "Requires: ncurses >= 4.2-12" and "Conflicts: glibc <= 2.0.7"
  for prevent installing readline with proper versions glibc a ncurses.

* Mon Feb 22 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.0-1]
- removed man group from man pages,
- standarized {un}registering info pages (added readline-info.patch),
- added LDFLAGS="-s" to ./configure enviroment, 
- added Group(pl),
- added gzipping man pages.

* Tue Oct  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.2.1-3]
- shared libs moved to /lib (neccesary for bash).

* Mon Aug  10 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.2.1-2]
- added -q %setup parameter,
- libreadline linked with ncurses,
- added stripping shared library,
- changed way passing $RPM_OPT_FLAGS (as configure enviroment variable),
- addes static subpackage.

* Sun Aug 02 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.2.1-2]
- updated to readline-2.2.1,
- added pl translation,

* Mon Jun  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- replaced linking with libtermcap instead libslang,
- man3 pages moved to devel,
- added -q %setup parameter,
- added stripig shared libs,
- added %[def]attr macros in %files.
* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- don't package %{_infodir}/dir

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel package moved to Development/Libraries

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.2

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- added proper sonames

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- updated to readline 2.1

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc
