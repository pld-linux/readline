Summary:	Library for reading lines from a terminal
Summary(de):	Library zum Lesen von Zeilen von einem Terminal
Summary(fr):	Bibliothéque pour lire des lignes depuis un terminal
Summary(pl):	Biblioteki do czytania linii z terminala
Summary(tr):	Terminalden satýr okumak için kullanýlan bir kitaplýk
Name:		readline
Version:	4.2
Release:	6
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://prep.ai.mit.edu/pub/gnu/readline/%{name}-%{version}.tar.gz
Source1:	%{name}-sys_inputrc
Patch0:		%{name}-shared.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-sys_inputrc.patch
Patch4:		%{name}-terminal.patch
Patch5:		%{name}-guard.patch
Patch6:		%{name}-header.patch
Prereq:		/sbin/ldconfig
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "readline" library will read a line from the terminal and return
it, allowing the user to edit the line with the standard emacs editing
keys. It allows the programmer to give the user an easier-to-use and
more intuitive interface.

%description -l de
Die "readline"-Library liest eine Zeile von einem Terminal ein, und
gibt sie zurück, so daß ein User die Zeile mit den normalen
emacs-Editiertasten ändern kann. Sie erlaubt einem Programmierer, dem
User ein einfacher zu benutzendes und intuitiveres Interface zu
schreiben.

%description -l pl
Biblioteka "readline" czyta liniê z terminala i zwraca j±, pozwalaj±c
u¿ytkownikowi edytowaæ j± za pomoc± standardowych klawiszy edycyjnych
emacsa. Pozwala programi¶cie daæ u¿ytkownikowi ³atwy do u¿ycia i
bardziej intuicyjny interfejs.

%package devel
Summary:	file for developing programs that use the readline library
Summary(de):	Datei zum Entwickeln von Programmen mit der readline-Library
Summary(fr):	Fichier pour développer des programmes utilisant la readline
Summary(pl):	Pakiet dla programistów u¿ywaj±cych bibliotek readline
Summary(tr):	readline kitaplýðýný kullanan programlar yazmak için gerekli dosyalar
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	ncurses-devel

%description devel
The "readline" library will read a line from the terminal and return
it, using prompt as a prompt. If prompt is null, no prompt is issued.
The line returned is allocated with malloc(3), so the caller must free
it when finished. The line returned has the final newline removed, so
only the text of the line remains.

%description devel -l de
Die "readline"-Library liest eine Zeile vom Terminal ein und gibt sie
zurück. Die zurückgegebene Zeile hat kein newline am Ende, so daß nur
der Text der Zeile bleibt.

%description devel -l pl
Biblioteka "readline" czyta liniê z terminala i zwracaj± j±, u¿ywaj±c
znaku zachêty (prompt) jako podpowiedzi. Je¿eli prompt jest zerem, nie
jest wy¶wietlany. Linia zwracana jest allokowana przez malloc(3).

%package static
Summary:	Static readline library
Summary(pl):	Biblioteka statyczna readline
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package contains static version of readline library.

%description static -l pl
Pakiet ten zawiera wersjê statycznê biblioteki readline.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
autoconf
%configure \
	--with-curses

%{__make} static shared

rm -f doc/*.info
%{__make} -C doc info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,lib}

%{__make} install install-shared DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/inputrc

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* $RPM_BUILD_ROOT/lib

ln_s -f ../../lib/libreadline.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libreadline.so
ln_s -f ../../lib/libhistory.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libhistory.so

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ !  -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/inputrc
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
