Summary:	A command-line WebDAV client
Summary(pl):	Klient WebDav (dzia�aj�cy z linii polece�)
Name:		cadaver
Version:	0.22.3
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz
# Source0-md5:	0c5268286e732a8d5d94361cf93de412
URL:		http://www.webdav.org/cadaver/
BuildRequires:	neon-devel >= 0.24.6
BuildRequires:	readline-devel
Requires:	neon >= 0.24.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cadaver is a command-line WebDAV client for Unix. It supports file
upload, download, on-screen display, namespace operations (move/copy),
collection creation and deletion, and locking operations.

%description -l pl
cadaver to klient WebDAV dzia�aj�cy z linii polece�. Obs�uguje on
wgrywanie plik�w, pobieranie, wy�wietlanie zawarto�ci na ekranie,
operacje dotycz�ce przestrzeni nazw (przenoszenie/kopiowanie),
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
%doc BUGS ChangeLog FAQ INTEROP NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
