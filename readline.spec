Summary:	Library for reading lines from a terminal
Summary(de):	Library zum Lesen von Zeilen von einem Terminal
Summary(fr):	Biblioth�que pour lire des lignes depuis un terminal
Summary(pl):	Biblioteki do czytania lini z terminala
Summary(tr):	Terminalden sat�r okumak i�in kullan�lan bir kitapl�k
Name:		readline
Version:	4.2
Release:	4
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
Prereq:		/sbin/ldconfig
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "readline" library will read a line from the terminal and return
it, allowing the user to edit the line with the standard emacs editing
keys. It allows the programmer to give the user an easier-to-use and
more intuitive interface.

%description -l de
Die "readline"-Library liest eine Zeile von einem Terminal ein, und
gibt sie zur�ck, so da� ein User die Zeile mit den normalen
emacs-Editiertasten �ndern kann. Sie erlaubt einem Programmierer, dem
User ein einfacher zu benutzendes und intuitiveres Interface zu
schreiben.

%package devel
Summary:	file for developing programs that use the readline library
Summary(de):	Datei zum Entwickeln von Programmen mit der readline-Library
Summary(fr):	Fichier pour d�velopper des programmes utilisant la readline
Summary(pl):	Pakiet dla programist�w u�ywaj�cych bibliotek readline
Summary(tr):	readline kitapl���n� kullanan programlar yazmak i�in gerekli dosyalar
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The "readline" library will read a line from the terminal and return
it, using prompt as a prompt. If prompt is null, no prompt is issued.
The line returned is allocated with malloc(3), so the caller must free
it when finished. The line returned has the final newline removed, so
only the text of the line remains.

%description -l de devel
Die "readline"-Library liest eine Zeile vom Terminal ein und gibt sie
zur�ck. Die zur�ckgegebene Zeile hat kein newline am Ende, so da� nur
der Text der Zeile bleibt.

%description -l pl devel
Biblioteka readline czyta linie z terminala i zwracaj� j�, u�ywaj�c
znaku zach�ty (prompt) jako podpowiedzi. Je�eli prompt jest zerem, nie
jest w�wczas wynikiowy. Linia zwracana jest allokowana przez
malloc(3).

%package static
Summary:	Static readline library
Summary(pl):	Biblioteka statyczna readline
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package contains sattic version readline library.

%description -l pl static
Pakiet ten zawiera wersj� statyczn� biblioteki readline.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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

ln -sf ../../lib/libreadline.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libreadline.so
ln -sf ../../lib/libhistory.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libhistory.so

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
%config(noreplace) %{_sysconfdir}/inputrc
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
