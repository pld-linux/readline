Summary:     Library for reading lines from a terminal
Summary(de): Library zum Lesen von Zeilen von einem Terminal
Summary(fr): Biblioth�que pour lire des lignes depuis un terminal.
Summary(pl): Biblioteki do czytania lini z terminala
Summary(tr): Terminalden sat�r okumak i�in kullan�lan bir kitapl�k
Name:        readline
Version:     2.2.1
Release:     3
Copyright:   GPL
Group:       Libraries
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:      readline-2.2.1-shared.patch
Prereq:      /sbin/install-info
Buildroot:   /tmp/%{name}-%{version}-root

%description
The "readline" library will read a line from the terminal and return it,
allowing the user to edit the line with the standard emacs editing keys.
It allows the programmer to give the user an easier-to-use and more
intuitive interface.

%package devel
Summary:     file for developing programs that use the readline library
Summary(de): Datei zum Entwickeln von Programmen mit der readline-Library
Summary(fr): Fichier pour d�velopper des programmes utilisant la librairie readline.
Summary(pl): Pakiet dla programist�w u�ywaj�cych bibliotek readline'a
Summary(tr): readline kitapl���n� kullanan programlar yazmak i�in gerekli dosyalar
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
The "readline" library will read a line from the terminal and return it,
using prompt as a prompt.  If prompt is null, no prompt is issued.  The
line returned is allocated with malloc(3), so the caller must free it when
finished.  The line returned has the final newline removed, so only the
text of the line remains.

%description -l pl devel

Biblioteka readline czyta linie z terminala i zwracaj� j�, u�ywaj�c znaku
zach�ty (prompt) jako podpowiedzi. Je�eli prompt jest zerem, nie jest
w�wczas wynikiowy.  Linia zwracana jest allokowana przez malloc(3).

%package static
Summary:     Static readline library
Summary(pl): Biblioteka statyczna readline
Group:       Development/Libraries
Requires:    %{name}-devel = %{version}

%description static
This package contains sattic version readline library.

%description -l pl static
Pakiet ten zawiera wersj� statyczn� biblioteki readline.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr
make static shared

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib

make install install-shared prefix=$RPM_BUILD_ROOT/usr

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

gzip -nf9 $RPM_BUILD_ROOT/usr/info/*info*

mv $RPM_BUILD_ROOT/usr/lib/lib*.so.*.* $RPM_BUILD_ROOT/lib 
ln -sf ../../lib/libreadline.so.3.0 $RPM_BUILD_ROOT/usr/lib/libreadline.so
ln -sf ../../lib/libhistory.so.3.0 $RPM_BUILD_ROOT/usr/lib/libhistory.so

%post
/sbin/ldconfig
/sbin/install-info /usr/info/history.info.gz /usr/info/dir --entry="* history: (readline).                   The GNU history (from readline)."
/sbin/install-info /usr/info/readline.info.gz /usr/info/dir --entry="* readline: (readline).                   The GNU readline."

%postun -p /sbin/ldconfig

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete /usr/info/history.info.gz /usr/info/dir --entry="* history: (history).                   The GNU history (from readline)."
   /sbin/install-info --delete /usr/info/readline.info.gz /usr/info/dir --entry=" * readline: (readline).                   The GNU readline."
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /lib/lib*.so.*.*
%attr(644, root, root) /usr/info/*info*

%files devel
%defattr(644, root, root, 755)
/usr/include/readline
/usr/lib/lib*.so
%attr(644, root, man) /usr/man/man3/*

%files static
%attr(644, root, root) /usr/lib/lib*.a

%changelog
* Tue Oct  6 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.2.1-3]
- shared libs moved to /lib (neccesary for bash).

* Mon Aug  10 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.2.1-2]
- added -q %setup parameter,
- rlibreadline linked with libslang,
- added striping shared library,
- changed way passing $RPM_OPT_)FLAGS (as configure enviroment variable),
- addes static subpackage.

* Sun Aug 02 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.2.1-2]
- updated to readline-2.2.1,
- added pl translation,

* Mon Jun  8 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- replaced linking with libtermcap instead libslang,
- man3 pages moved to devel,
- added -q %setup parameter,
- added stripig shared libs,
- added %[def]attr macros in %files.
* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- don't package /usr/info/dir

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
