Summary:	A command-line WebDAV client
Summary(pl.UTF-8):	Klient WebDav (działający z linii poleceń)
Name:		cadaver
Version:	0.23.2
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz
# Source0-md5:	5ac79e41f3b7b4f68bf4003beed5dc26
URL:		http://www.webdav.org/cadaver/
BuildRequires:	automake
BuildRequires:	neon-devel >= 0.28.0
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

%build
install %{_datadir}/automake/config.* .
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
