Summary:	Library for reading lines from a terminal
Summary(de):	Library zum Lesen von Zeilen von einem Terminal
Summary(fr):	Bibliothéque pour lire des lignes depuis un terminal.
Summary(pl):	Biblioteki do czytania lini z terminala
Summary(tr):	Terminalden satýr okumak için kullanýlan bir kitaplýk
Name:		readline
Version:	4.0
Release:	5
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

%package	devel
Summary:	file for developing programs that use the readline library
Summary(de):	Datei zum Entwickeln von Programmen mit der readline-Library
Summary(fr):	Fichier pour développer des programmes utilisant la readline
Summary(pl):	Pakiet dla programistów u¿ywaj±cych bibliotek readline
Summary(tr):	readline kitaplýðýný kullanan programlar yazmak için gerekli \
Summary(tr):	dosyalar
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

%package	static
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
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=%{_prefix} \
	--with-curses \
	%{_target_platform}

make static shared

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib

make install install-shared \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    mandir=$RPM_BUILD_ROOT%{_mandir} \
    infodir=$RPM_BUILD_ROOT%{_infodir}

mv $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* $RPM_BUILD_ROOT/lib 
chmod 755 $RPM_BUILD_ROOT/lib/*.so.* 

ln -sf ../../lib/libreadline.so.4.0 $RPM_BUILD_ROOT%{_libdir}/libreadline.so
ln -sf ../../lib/libhistory.so.4.0 $RPM_BUILD_ROOT%{_libdir}/libhistory.so

strip --strip-unneeded $RPM_BUILD_ROOT/lib/lib*.so.*.*

gzip -nf9 $RPM_BUILD_ROOT{%{_infodir}/*info*,%{_mandir}/man3/*}

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
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Fri May 21 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.0-5]
- based on RH spec,
- pl translation by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>,
- spec rewrited by me and Wojtek ¦lusarczyk <wojtek@shadow.eu.org>.
