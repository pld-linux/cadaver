Summary:	A command-line WebDAV client
Summary(pl):	Klient WebDav (z linii poleceñ)
Name:		cadaver
Version:	0.20.5
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz
URL:		http://www.webdav.org/cadaver/
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	libxml2-devel
BuildRequires:	neon-devel >= 0.21.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cadaver is a command-line WebDAV client for Unix. It supports file
upload, download, on-screen display, namespace operations (move/copy),
collection creation and deletion, and locking operations.

%description -l pl
cadaver to klient WebDAV z linii poleceñ. Wspiera on wgrywanie plików,
pobieranie, wy¶wietlanie zawarto¶ci na ekranie, operacje dotycz±ce
przestrzeni nazw (przenoszenie/kopiowanie), tworzenie i usuwanie
kolekcji oraz operacje blokowania.

%prep
%setup -q

%build
%configure \
	--with-ssl \
	--with-force-ssl \
	--with-libxml2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog FAQ INTEROP NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
