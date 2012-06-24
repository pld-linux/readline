Summary:	Library for reading lines from a terminal
Summary(de):	Library zum Lesen von Zeilen von einem Terminal
Summary(es):	Biblioteca para lectura de l�neas de un terminal
Summary(fr):	Biblioth�que pour lire des lignes depuis un terminal
Summary(ja):	readline �饤�֥��
Summary(pl):	Biblioteki do czytania linii z terminala
Summary(pt_BR):	Biblioteca para leitura de linhas de um terminal
Summary(ru):	���������� ��� ������ ����� � ���������
Summary(tr):	Terminalden sat�r okumak i�in kullan�lan bir kitapl�k
Summary(uk):	��̦����� ��� ������� ��Ҧ��� � ���ͦ����
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
gibt sie zur�ck, so da� ein User die Zeile mit den normalen
emacs-Editiertasten �ndern kann. Sie erlaubt einem Programmierer, dem
User ein einfacher zu benutzendes und intuitiveres Interface zu
schreiben.

%description -l es
La biblioteca "readline" leer� una l�nea del terminal y la recuperar�,
permitiendo al usuario editar la l�nea con las teclas de edici�n
padr�n emacs. Permite al programador dar al usuario una interface m�s
f�cil de usar y m�s intuitiva.

%description -l ja
"readline" �饤�֥����Ѥ���ȡ�ü�������ɤߤ������Ԥ�emacs
��ɸ�७��
��Ʊ�����Х���ǥ��󥰤��Խ��Ǥ���褦�ˤʤ�ޤ��������ץ������ǻȤ��ȡ�
���Ȥ��䤹�����󥿥ե�������桼�����󶡤Ǥ��ޤ���

%description -l pl
Biblioteka "readline" czyta lini� z terminala i zwraca j�, pozwalaj�c
u�ytkownikowi edytowa� j� za pomoc� standardowych klawiszy edycyjnych
emacsa. Pozwala programi�cie da� u�ytkownikowi �atwy do u�ycia i
bardziej intuicyjny interfejs.

%description -l pt_BR
A biblioteca "readline" ler� uma linha do terminal e ir� retorn�-la,
permitindo ao usu�rio editar a linha com as teclas de edi��o padr�o
emacs. Ele permite ao programador dar ao usu�rio uma interface mais
f�cil de usar e mais intuitiva.

%description -l ru
���������� "readline" ������ ������ � ��������� � ���������� ��,
�������� ������������ ������������� ������ ��� ������ �����������
������ emacs. ��������� ������������ ������������ ������������ �����
������� � ����������� ���������. ��������� �������� � locale.

%description -l uk
��̦����� "readline" ����� ��Ҧ��� � ���ͦ���� � �������� ��,
���������� ����������� ���������� ��Ҧ��� �� ��������� �����������
���צ� emacs. ������Ѥ ������ͦ��� ����������� ¦��� ������� ��
���զ������ ��������� �����������. ��������� ������ � locale.

%package devel
Summary:	file for developing programs that use the readline library
Summary(de):	Datei zum Entwickeln von Programmen mit der readline-Library
Summary(es):	Archivo para desarrollar programas que utilicen la biblioteca para lectura de l�neas
Summary(fr):	Fichier pour d�velopper des programmes utilisant la readline
Summary(ja):	readline �饤�֥���Ȥ��ץ���ि��γ�ȯ�ѥ饤�֥��
Summary(pl):	Pakiet dla programist�w u�ywaj�cych bibliotek readline
Summary(pt_BR):	Arquivo para desenvolver programas que utilizam a readline
Summary(ru):	�����, ����������� ��� ���������� ��������, ������������ ���������� readline
Summary(tr):	readline kitapl���n� kullanan programlar yazmak i�in gerekli dosyalar
Summary(uk):	�����, ����Ȧ�Φ ��� �������� �������, �� �������������� ¦�̦����� readline
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
zur�ck. Die zur�ckgegebene Zeile hat kein newline am Ende, so da� nur
der Text der Zeile bleibt.

%description devel -l es
La biblioteca readline leer� una l�nea del terminal y la recuperar�,
usando prompt como prompt. Si prompt es nulo, ning�n prompt se ense�a.
La l�nea recuperada es alocada con malloc(3), debiendo el llamador
liberarla cuando terminar. La l�nea recuperada tiene el salto de l�nea
final quitado, de esta forma solamente el texto de la l�nea se pone a
disposici�n.

%description -l ja
"readline"
�饤�֥���ü���������ɤ�ȡ��ץ��ץȤȤȤ�ˤ�����֤�
�ޤ����֤��ͤȤʤ�Ԥ� malloc �ǳ�����Ƥ�졢��λ���ˤϤ��Υ����
�������ʤ��Ȥ����ޤ���

%description devel -l pl
Biblioteka "readline" czyta lini� z terminala i zwracaj� j�, u�ywaj�c
znaku zach�ty (prompt) jako podpowiedzi. Je�eli prompt jest zerem, nie
jest wy�wietlany. Linia zwracana jest allokowana przez malloc(3).

%description devel -l pt_BR
A biblioteca readline ler� uma linha do terminal e a retornar�, usando
prompt como prompt. Se prompt � nulo, nenhum prompt � mostrado. A
linha retornada � alocada com malloc(3), devendo o chamador liber�-la
quando terminar. A linha retornada tem o salto de linha final
removido, desta forma somente o texto da linha � disponibilizado.

%description devel -l ru
���������� "readline" ������ ������ � ��������� � ���������� ��,
��������� �������� ��������� ������������ (prompt). ���� ��� ���������
������������ ����� ������ ������, �� ����� �� �������� �������
���������. ������������ ������ �������� ������, ���������� ��������
malloc(3), ������� ���������� ��������� ������ ���������� ��� ������
�� ������ ����������. ������������ ������ �� �������� ���������������
�������� ������, �.�. ������������ ������ ����� ������.

%description devel -l uk
��̦����� "readline" ����� ��Ҧ��� � ���ͦ���� � �������� ��,
���������� �� ������� ������ �������� ���������� (prompt). ���� ��
���������� ���Ѥ ����� ������� ��Ҧ���, Φ��ϧ Ц������ �� ����� ��
���������. ��Ҧ���, �� ������������ ¦�̦������, ������ ���'���,
��Ħ���� ����æ�� malloc(3), ��� �� �������� ��� �צ������ �� ���'���
�� ����� ����������. ��Ҧ��� �� ͦ����� ���������� �������� ��Ҧ���,
�.�. ������������ Ԧ���� ����� ��Ҧ���.

%package static
Summary:	Static readline library
Summary(es):	Static libraries for readline development
Summary(pl):	Biblioteka statyczna readline
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com a readline
Summary(ru):	����������� ���������� readline
Summary(uk):	������Φ ¦�̦����� readline
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static version of readline library.

%description static -l es
Static libraries for readline development.

%description static -l pl
Pakiet ten zawiera wersj� statyczn� biblioteki readline.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com readline.

%description static -l ru
��� ����������� ���������� readline.

%description static -l uk
�� ������Φ ¦�̦����� readline.

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
