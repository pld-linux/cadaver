Summary:	A command-line WebDAV client
Summary(pl.UTF-8):	Klient WebDav (działający z linii poleceń)
Name:		cadaver
Version:	0.28
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	https://notroj.github.io/cadaver/%{name}-%{version}.tar.gz
# Source0-md5:	6e207420e668985c97eb47862f8ca089
URL:		https://notroj.github.io/cadaver/
BuildRequires:	neon-devel >= 0.29.0
BuildRequires:	pakchois-devel >= 0.4
BuildRequires:	readline-devel
Requires:	neon >= 0.29.0
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
%doc COPYING FAQ NEWS README.md THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
