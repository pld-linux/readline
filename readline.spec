Summary:	Library for reading lines from a terminal
Summary(de):	Library zum Lesen von Zeilen von einem Terminal
Summary(es):	Biblioteca para lectura de líneas de un terminal
Summary(fr):	Bibliothéque pour lire des lignes depuis un terminal
Summary(ja):	readline ¥é¥¤¥Ö¥é¥ê
Summary(pl):	Biblioteki do czytania linii z terminala
Summary(pt_BR):	Biblioteca para leitura de linhas de um terminal
Summary(ru):	âÉÂÌÉÏÔÅËÁ ÄÌÑ ÞÔÅÎÉÑ ÓÔÒÏË Ó ÔÅÒÍÉÎÁÌÁ
Summary(tr):	Terminalden satýr okumak için kullanýlan bir kitaplýk
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ ÞÉÔÁÎÎÑ ÓÔÒ¦ÞÏË Ú ÔÅÒÍ¦ÎÁÌÕ
Name:		readline
Version:	4.3
Release:	5
License:	GPL
Group:		Libraries
Source0:	ftp://prep.ai.mit.edu/pub/gnu/readline/%{name}-%{version}.tar.gz
Source1:	%{name}-sys_inputrc
Patch0:		%{name}-ac25x.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-sys_inputrc.patch
Patch4:		%{name}-terminal.patch
Patch5:		%{name}-header.patch
Patch6:		%{name}-segv.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		sonameversion	4.3

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

%description -l es
La biblioteca "readline" leerá una línea del terminal y la recuperará,
permitiendo al usuario editar la línea con las teclas de edición
padrón emacs. Permite al programador dar al usuario una interface más
fácil de usar y más intuitiva.

%description -l ja
"readline" ¥é¥¤¥Ö¥é¥ê¤òÍÑ¤¤¤ë¤È¡¢Ã¼Ëö¤«¤éÆÉ¤ß¤³¤ó¤À°ì¹Ô¤ò¡¢emacs
¤ÎÉ¸½à¥­¡¼
¤ÈÆ±¥­¡¼¥Ð¥¤¥ó¥Ç¥£¥ó¥°¤ÇÊÔ½¸¤Ç¤­¤ë¤è¤¦¤Ë¤Ê¤ê¤Þ¤¹¡£¤³¤ì¤ò¥×¥í¥°¥é¥àÃæ¤Ç»È¤¦¤È¡¢
¤è¤ê»È¤¤¤ä¤¹¤¤¥¤¥ó¥¿¥Õ¥§¡¼¥¹¤ò¥æ¡¼¥¶¤ËÄó¶¡¤Ç¤­¤Þ¤¹¡£

%description -l pl
Biblioteka "readline" czyta liniê z terminala i zwraca j±, pozwalaj±c
u¿ytkownikowi edytowaæ j± za pomoc± standardowych klawiszy edycyjnych
emacsa. Pozwala programi¶cie daæ u¿ytkownikowi ³atwy do u¿ycia i
bardziej intuicyjny interfejs.

%description -l pt_BR
A biblioteca "readline" lerá uma linha do terminal e irá retorná-la,
permitindo ao usuário editar a linha com as teclas de edição padrão
emacs. Ele permite ao programador dar ao usuário uma interface mais
fácil de usar e mais intuitiva.

%description -l ru
âÉÂÌÉÏÔÅËÁ "readline" ÞÉÔÁÅÔ ÓÔÒÏËÕ Ó ÔÅÒÍÉÎÁÌÁ É ×ÏÚ×ÒÁÝÁÅÔ ÅÅ,
ÐÏÚ×ÏÌÑÑ ÐÏÌØÚÏ×ÁÔÅÌÀ ÒÅÄÁËÔÉÒÏ×ÁÔØ ÓÔÒÏËÕ ÐÒÉ ÐÏÍÏÝÉ ÓÔÁÎÄÁÒÔÎÙÈ
ËÌÁ×ÉÛ emacs. ðÏÚ×ÏÌÑÅÔ ÐÒÏÇÒÁÍÍÉÓÔÕ ÐÒÅÄÏÓÔÁ×ÉÔØ ÐÏÌØÚÏ×ÁÔÅÌÀ ÂÏÌÅÅ
ÐÒÏÓÔÏÊ É ÉÎÔÕÉÔÉ×ÎÙÊ ÉÎÔÅÒÆÅÊÓ. ðÒÁ×ÉÌØÎÏ ÒÁÂÏÔÁÅÔ Ó locale.

%description -l uk
â¦ÂÌ¦ÏÔÅËÁ "readline" ÞÉÔÁ¤ ÓÔÒ¦ÞËÕ Ú ÔÅÒÍ¦ÎÁÌÁ ¦ ÐÏ×ÅÒÔÁ¤ §§,
ÄÏÚ×ÏÌÑÀÞÉ ËÏÒÉÓÔÕ×ÁÞÕ ÒÅÄÁÇÕ×ÁÔÉ ÓÔÒ¦ÞËÕ ÚÁ ÄÏÐÏÍÏÇÏÀ ÓÔÁÎÄÁÒÔÎÉÈ
ËÌÁ×¦Û emacs. äÏÚ×ÏÌÑ¤ ÐÒÏÇÒÁÍ¦ÓÔÕ ÚÁÂÅÚÐÅÞÉÔÉ Â¦ÌØÛ ÐÒÏÓÔÉÊ ÔÁ
¦ÎÔÕ¦ÔÉ×ÎÉÊ ¦ÎÔÅÒÆÅÊÓ ËÏÒÉÓÔÕ×ÁÞÁ. ðÒÁ×ÉÌØÎÏ ÐÒÁÃÀ¤ Ú locale.

%package devel
Summary:	file for developing programs that use the readline library
Summary(de):	Datei zum Entwickeln von Programmen mit der readline-Library
Summary(es):	Archivo para desarrollar programas que utilicen la biblioteca para lectura de líneas
Summary(fr):	Fichier pour développer des programmes utilisant la readline
Summary(ja):	readline ¥é¥¤¥Ö¥é¥ê¤ò»È¤¦¥×¥í¥°¥é¥à¤¿¤á¤Î³«È¯ÍÑ¥é¥¤¥Ö¥é¥ê
Summary(pl):	Pakiet dla programistów u¿ywaj±cych bibliotek readline
Summary(pt_BR):	Arquivo para desenvolver programas que utilizam a readline
Summary(ru):	æÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ, ÉÓÐÏÌØÚÕÀÝÉÈ ÂÉÂÌÉÏÔÅËÕ readline
Summary(tr):	readline kitaplýðýný kullanan programlar yazmak için gerekli dosyalar
Summary(uk):	æÁÊÌÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ Â¦ÂÌ¦ÏÔÅËÕ readline
Group:		Development/Libraries
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

%description devel -l es
La biblioteca readline leerá una línea del terminal y la recuperará,
usando prompt como prompt. Si prompt es nulo, ningún prompt se enseña.
La línea recuperada es alocada con malloc(3), debiendo el llamador
liberarla cuando terminar. La línea recuperada tiene el salto de línea
final quitado, de esta forma solamente el texto de la línea se pone a
disposición.

%description -l ja
"readline"
¥é¥¤¥Ö¥é¥ê¤ÏÃ¼Ëö¤«¤é°ì¹ÔÆÉ¤à¤È¡¢¥×¥í¥ó¥×¥È¤È¤È¤â¤Ë¤½¤ì¤òÊÖ¤·
¤Þ¤¹¡£ÊÖ¤êÃÍ¤È¤Ê¤ë¹Ô¤Ï malloc ¤Ç³ä¤êÅö¤Æ¤é¤ì¡¢½ªÎ»»þ¤Ë¤Ï¤½¤Î¥á¥â¥ê¤Ï
³«Êü¤·¤Ê¤¤¤È¤¤¤±¤Þ¤»¤ó¡£

%description devel -l pl
Biblioteka "readline" czyta liniê z terminala i zwracaj± j±, u¿ywaj±c
znaku zachêty (prompt) jako podpowiedzi. Je¿eli prompt jest zerem, nie
jest wy¶wietlany. Linia zwracana jest allokowana przez malloc(3).

%description devel -l pt_BR
A biblioteca readline lerá uma linha do terminal e a retornará, usando
prompt como prompt. Se prompt é nulo, nenhum prompt é mostrado. A
linha retornada é alocada com malloc(3), devendo o chamador liberá-la
quando terminar. A linha retornada tem o salto de linha final
removido, desta forma somente o texto da linha é disponibilizado.

%description devel -l ru
âÉÂÌÉÏÔÅËÁ "readline" ÞÉÔÁÅÔ ÓÔÒÏËÕ Ó ÔÅÒÍÉÎÁÌÁ É ×ÏÚ×ÒÁÝÁÅÔ ÅÅ,
ÐÒÅÄ×ÁÒÑÑ ÚÁÄÁÎÎÙÍ ÓÉÓÔÅÍÎÙÍ ÐÒÉÇÌÁÛÅÎÉÅÍ (prompt). åÓÌÉ ÜÔÁ ÐÏÄÓËÁÚËÁ
ÐÒÅÄÓÔÁ×ÌÑÅÔ ÓÏÂÏÊ ÐÕÓÔÕÀ ÓÔÒÏËÕ, ÎÁ ÜËÒÁÎ ÎÅ ×ÙÄÁÅÔÓÑ ÎÉËÁËÏÊ
ÐÏÄÓËÁÚËÉ. ÷ÏÚ×ÒÁÝÁÅÍÁÑ ÓÔÒÏËÁ ÚÁÎÉÍÁÅÔ ÐÁÍÑÔØ, ×ÙÄÅÌÅÎÎÕÀ ÆÕÎËÃÉÅÊ
malloc(3), ÐÏÜÔÏÍÕ ×ÙÚÙ×ÁÀÝÁÑ ÐÒÏÇÒÁÍÍÁ ÄÏÌÖÎÁ ÏÓ×ÏÂÏÄÉÔØ ÜÔÕ ÐÁÍÑÔØ
ÄÏ Ó×ÏÅÇÏ ÚÁ×ÅÒÛÅÎÉÑ. ÷ÏÚ×ÒÁÝÁÅÍÁÑ ÓÔÒÏËÁ ÎÅ ÓÏÄÅÒÖÉÔ ÚÁËÌÀÞÉÔÅÌØÎÏÇÏ
ÐÅÒÅ×ÏÄÁ ÓÔÒÏËÉ, Ô.Å. ×ÏÚ×ÒÁÝÁÅÔÓÑ ÔÏÌØËÏ ÔÅËÓÔ ÓÔÒÏËÉ.

%description devel -l uk
â¦ÂÌ¦ÏÔÅËÁ "readline" ÞÉÔÁ¤ ÓÔÒ¦ÞËÕ Ú ÔÅÒÍ¦ÎÁÌÁ ¦ ÐÏ×ÅÒÔÁ¤ §§,
ÄÏÂÁ×ÌÑÀÞÉ ÎÁ ÐÏÞÁÔËÕ ÚÁÄÁÎÅ ÓÉÓÔÅÍÎÅ ÚÁÐÒÏÛÅÎÎÑ (prompt). ñËÝÏ ÃÅ
ÚÁÐÒÏÛÅÎÎÑ Ñ×ÌÑ¤ ÓÏÂÏÀ ÐÏÒÏÖÎÀ ÓÔÒ¦ÞËÕ, Î¦ÑËÏ§ Ð¦ÄËÁÚËÉ ÎÁ ÅËÒÁÎ ÎÅ
×ÉÄÁ¤ÔØÓÑ. óÔÒ¦ÞËÁ, ÝÏ ÐÏ×ÅÒÔÁ¤ÔØÓÑ Â¦ÂÌ¦ÏÔÅËÏÀ, ÚÁÊÍÁ¤ ÐÁÍ'ÑÔØ,
×ÉÄ¦ÌÅÎÕ ÆÕÎËÃ¦¤À malloc(3), ÔÁË ÝÏ ÐÒÏÇÒÁÍÁ ÍÁ¤ Ú×¦ÌØÎÉÔÉ ÃÀ ÐÁÍ'ÑÔØ
ÄÏ Ó×ÏÇÏ ÚÁ×ÅÒÛÅÎÎÑ. óÔÒ¦ÞËÁ îå Í¦ÓÔÉÔØ ÚÁËÌÀÞÎÏÇÏ ÐÅÒÅ×ÏÄÕ ÓÔÒ¦ÞËÉ,
Ô.Þ. ÐÏ×ÅÒÔÁ¤ÔØÓÑ Ô¦ÌØËÉ ÔÅËÓÔ ÓÔÒ¦ÞËÉ.

%package static
Summary:	Static readline library
Summary(es):	Static libraries for readline development
Summary(pl):	Biblioteka statyczna readline
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com a readline
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ readline
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ readline
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static version of readline library.

%description static -l es
Static libraries for readline development.

%description static -l pl
Pakiet ten zawiera wersjê statyczn± biblioteki readline.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com readline.

%description static -l ru
üÔÏ ÓÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ readline.

%description static -l uk
ãÅ ÓÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ readline.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
mv -f aclocal.m4 acinclude.m4
%{__aclocal}
%{__autoconf}
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

rm -f $RPM_BUILD_ROOT%{_libdir}/*old

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* $RPM_BUILD_ROOT/lib

ln -sf /lib/libreadline.so.%{sonameversion} $RPM_BUILD_ROOT%{_libdir}/libreadline.so
ln -sf /lib/libhistory.so.%{sonameversion} $RPM_BUILD_ROOT%{_libdir}/libhistory.so

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
