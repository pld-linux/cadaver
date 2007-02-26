Summary:	A command-line WebDAV client
Summary(pl):	Klient WebDav (dzia³aj±cy z linii poleceñ)
Name:		cadaver
Version:	0.22.5
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz
# Source0-md5:	e9fade983dd7b18d33230967051fcfe0
URL:		http://www.webdav.org/cadaver/
BuildRequires:	automake
BuildRequires:	neon-devel >= 0.24.6
BuildRequires:	readline-devel
Requires:	neon >= 0.24.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cadaver is a command-line WebDAV client for Unix. It supports file
upload, download, on-screen display, namespace operations (move/copy),
collection creation and deletion, and locking operations.

%description -l pl
cadaver to klient WebDAV dzia³aj±cy z linii poleceñ. Obs³uguje on
wgrywanie plików, pobieranie, wy¶wietlanie zawarto¶ci na ekranie,
operacje dotycz±ce przestrzeni nazw (przenoszenie/kopiowanie),
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
