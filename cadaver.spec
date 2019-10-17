Summary:	A command-line WebDAV client
Summary(pl.UTF-8):	Klient WebDav (działający z linii poleceń)
Name:		cadaver
Version:	0.23.3
Release:	6
License:	GPL
Group:		Applications/Networking
Source0:	http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz
# Source0-md5:	502ecd601e467f8b16056d2acca39a6f
Patch0:		cadaver-0.23.3-neon030.patch
Patch1:		%{name}-configure.patch
URL:		http://www.webdav.org/cadaver/
BuildRequires:	automake
BuildRequires:	neon-devel >= 0.28.0
BuildRequires:	pakchois-devel >= 0.4
BuildRequires:	readline-devel
Requires:	neon >= 0.27.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cadaver is a command-line WebDAV client for Unix. It supports file
upload, download, on-screen display, namespace operations (move/copy),
collection creation and deletion, and locking operations.

%description -l pl.UTF-8
cadaver to klient WebDAV działający z linii poleceń. Obsługuje on
wgrywanie plików, pobieranie, wyświetlanie zawartości na ekranie,
operacje dotyczące przestrzeni nazw (przenoszenie/kopiowanie),
tworzenie i usuwanie kolekcji oraz operacje blokowania.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4 -I m4/neon
%{__autoconf}
%{__autoheader}
%configure \
	--with-neon=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS ChangeLog FAQ INTEROP NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
