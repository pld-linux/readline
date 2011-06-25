%define	ver		6.2
%define	patchlevel	1
Summary:	Library for reading lines from a terminal
Summary(de.UTF-8):	Library zum Lesen von Zeilen von einem Terminal
Summary(es.UTF-8):	Biblioteca para lectura de líneas de un terminal
Summary(fr.UTF-8):	Bibliothéque pour lire des lignes depuis un terminal
Summary(ja.UTF-8):	readline ライブラリ
Summary(ko.UTF-8):	터미널에서 한줄씩 읽을때 사용하는 라이브러리
Summary(pl.UTF-8):	Biblioteki do czytania linii z terminala
Summary(pt_BR.UTF-8):	Biblioteca para leitura de linhas de um terminal
Summary(ru.UTF-8):	Библиотека для чтения строк с терминала
Summary(tr.UTF-8):	Terminalden satır okumak için kullanılan bir kitaplık
Summary(uk.UTF-8):	Бібліотека для читання стрічок з терміналу
Name:		readline
Version:	%{ver}%{?patchlevel:.%{patchlevel}}
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/readline/%{name}-%{ver}.tar.gz
# Source0-md5:	67948acb2ca081f23359d0256e9a271c
Source1:	%{name}-sys_inputrc
Patch0:		%{name}-shared.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-header.patch
Patch3:		%{name}-lfs.patch
Patch4:		%{name}-tinfo.patch
%{?patchlevel:%patchset_source -f http://ftp.gnu.org/gnu/readline/readline-6.2-patches/readline62-%03g 1 %{patchlevel}}
URL:		http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
# libtinfow.so.* must be on /
Requires:	ncurses >= 5.7-18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "readline" library will read a line from the terminal and return
it, allowing the user to edit the line with the standard emacs editing
keys. It allows the programmer to give the user an easier-to-use and
more intuitive interface.

%description -l de.UTF-8
Die "readline"-Library liest eine Zeile von einem Terminal ein, und
gibt sie zurück, so daß ein User die Zeile mit den normalen
emacs-Editiertasten ändern kann. Sie erlaubt einem Programmierer, dem
User ein einfacher zu benutzendes und intuitiveres Interface zu
schreiben.

%description -l es.UTF-8
La biblioteca "readline" leerá una línea del terminal y la recuperará,
permitiendo al usuario editar la línea con las teclas de edición
padrón emacs. Permite al programador dar al usuario una interface más
fácil de usar y más intuitiva.

%description -l ja.UTF-8
"readline" ライブラリを用いると、端末から読みこんだ一行を、emacs
の標準キー
と同キーバインディングで編集できるようになります。これをプログラム中で使うと、
より使いやすいインタフェースをユーザに提供できます。

%description -l pl.UTF-8
Biblioteka "readline" czyta linię z terminala i zwraca ją, pozwalając
użytkownikowi modyfikować ją za pomocą standardowych klawiszy
edycyjnych emacsa. Pozwala programiście dać użytkownikowi łatwy do
użycia i bardziej intuicyjny interfejs.

%description -l pt_BR.UTF-8
A biblioteca "readline" lerá uma linha do terminal e irá retorná-la,
permitindo ao usuário editar a linha com as teclas de edição padrão
emacs. Ele permite ao programador dar ao usuário uma interface mais
fácil de usar e mais intuitiva.

%description -l ru.UTF-8
Библиотека "readline" читает строку с терминала и возвращает ее,
позволяя пользователю редактировать строку при помощи стандартных
клавиш emacs. Позволяет программисту предоставить пользователю более
простой и интуитивный интерфейс. Правильно работает с locale.

%description -l uk.UTF-8
Бібліотека "readline" читає стрічку з термінала і повертає її,
дозволяючи користувачу редагувати стрічку за допомогою стандартних
клавіш emacs. Дозволяє програмісту забезпечити більш простий та
інтуітивний інтерфейс користувача. Правильно працює з locale.

%package devel
Summary:	file for developing programs that use the readline library
Summary(de.UTF-8):	Datei zum Entwickeln von Programmen mit der readline-Library
Summary(es.UTF-8):	Archivo para desarrollar programas que utilicen la biblioteca para lectura de líneas
Summary(fr.UTF-8):	Fichier pour développer des programmes utilisant la readline
Summary(ja.UTF-8):	readline ライブラリを使うプログラムための開発用ライブラリ
Summary(ko.UTF-8):	readline 라이브러리를 사용하는 프로그램을 만들때 사용하는 파일들
Summary(pl.UTF-8):	Pakiet dla programistów używających bibliotek readline
Summary(pt_BR.UTF-8):	Arquivo para desenvolver programas que utilizam a readline
Summary(ru.UTF-8):	Файлы, необходимые для разработки программ, использующих библиотеку readline
Summary(tr.UTF-8):	readline kitaplığını kullanan programlar yazmak için gerekli dosyalar
Summary(uk.UTF-8):	Файли, необхідні для розробки програм, що використовують бібліотеку readline
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ncurses-devel >= 5.0

%description devel
The "readline" library will read a line from the terminal and return
it, using prompt as a prompt. If prompt is null, no prompt is issued.
The line returned is allocated with malloc(3), so the caller must free
it when finished. The line returned has the final newline removed, so
only the text of the line remains.

%description devel -l de.UTF-8
Die "readline"-Library liest eine Zeile vom Terminal ein und gibt sie
zurück. Die zurückgegebene Zeile hat kein newline am Ende, so daß nur
der Text der Zeile bleibt.

%description devel -l es.UTF-8
La biblioteca readline leerá una línea del terminal y la recuperará,
usando prompt como prompt. Si prompt es nulo, ningún prompt se enseña.
La línea recuperada es alocada con malloc(3), debiendo el llamador
liberarla cuando terminar. La línea recuperada tiene el salto de línea
final quitado, de esta forma solamente el texto de la línea se pone a
disposición.

%description devel -l ja.UTF-8
"readline"
ライブラリは端末から一行読むと、プロンプトとともにそれを返し
ます。返り値となる行は malloc で割り当てられ、終了時にはそのメモリは
開放しないといけません。

%description devel -l pl.UTF-8
Biblioteka "readline" czyta linię z terminala i zwracają ją, używając
znaku zachęty (prompt) jako podpowiedzi. Jeżeli prompt jest zerem, nie
jest wyświetlany. Linia zwracana jest allokowana przez malloc(3).

%description devel -l pt_BR.UTF-8
A biblioteca readline lerá uma linha do terminal e a retornará, usando
prompt como prompt. Se prompt é nulo, nenhum prompt é mostrado. A
linha retornada é alocada com malloc(3), devendo o chamador liberá-la
quando terminar. A linha retornada tem o salto de linha final
removido, desta forma somente o texto da linha é disponibilizado.

%description devel -l ru.UTF-8
Библиотека "readline" читает строку с терминала и возвращает ее,
предваряя заданным системным приглашением (prompt). Если эта подсказка
представляет собой пустую строку, на экран не выдается никакой
подсказки. Возвращаемая строка занимает память, выделенную функцией
malloc(3), поэтому вызывающая программа должна освободить эту память
до своего завершения. Возвращаемая строка не содержит заключительного
перевода строки, т.е. возвращается только текст строки.

%description devel -l uk.UTF-8
Бібліотека "readline" читає стрічку з термінала і повертає її,
добавляючи на початку задане системне запрошення (prompt). Якщо це
запрошення являє собою порожню стрічку, ніякої підказки на екран не
видається. Стрічка, що повертається бібліотекою, займає пам'ять,
виділену функцією malloc(3), так що програма має звільнити цю пам'ять
до свого завершення. Стрічка НЕ містить заключного переводу стрічки,
т.ч. повертається тільки текст стрічки.

%package static
Summary:	Static readline library
Summary(es.UTF-8):	Static libraries for readline development
Summary(pl.UTF-8):	Biblioteka statyczna readline
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com a readline
Summary(ru.UTF-8):	Статические библиотеки readline
Summary(uk.UTF-8):	Статичні бібліотеки readline
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of readline library.

%description static -l es.UTF-8
Static libraries for readline development.

%description static -l pl.UTF-8
Pakiet ten zawiera wersję statyczną biblioteki readline.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com readline.

%description static -l ru.UTF-8
Это статические библиотеки readline.

%description static -l uk.UTF-8
Це статичні бібліотеки readline.

%prep
%setup -q -n %{name}-%{ver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1

%build
cp -f /usr/share/automake/config.sub support
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
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/%{_lib}}

%{__make} install install-shared \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/inputrc

rm -f $RPM_BUILD_ROOT%{_libdir}/*old

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.* $RPM_BUILD_ROOT/%{_lib}

ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libreadline.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libreadline.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libhistory.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libhistory.so

# help rpm to find deps
chmod +x $RPM_BUILD_ROOT/%{_lib}/lib*.so*

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/inputrc
%attr(755,root,root) /%{_lib}/libhistory.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libhistory.so.6
%attr(755,root,root) /%{_lib}/libreadline.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libreadline.so.6
%{_infodir}/history.info*
%{_infodir}/readline.info*
%{_infodir}/rluserman.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhistory.so
%attr(755,root,root) %{_libdir}/libreadline.so
%{_includedir}/readline
%{_mandir}/man3/history.3*
%{_mandir}/man3/readline.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libhistory.a
%{_libdir}/libreadline.a
