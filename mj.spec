Summary:	The original Mah-Jong game
Name:		mj
Version:	1.10
Release:	1
License:	GPL
Group:		Applications
Source0:	http://mahjong.julianbradfield.org/Source/%{name}-%{version}-src.tar.gz
# Source0-md5:	f9bacf9fd6743d5e3a2fd86863607ce2
Source1:	%{name}.desktop
Patch0:		%{name}-man.patch
URL:		http://mahjong.julianbradfield.org/
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of programs to play the original Mah-Jong game: one
server, one client for a human player and one client for an AI player.
Hence the game can be played by 1 to 4 human players.

You should keep in mind that the original Mah-Jong game has nothing to
do with the well-known solitaire game. (It merely uses the same set of
tiles.)

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1

%build
%{__make} \
	 CCOPTIONS="%{rpmcflags}" \
	 EXTRA_LDOPTIONS="%{rpmldflags}" \
	 TILESETPATH="\"%{_datadir}/mah-jong\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/mah-jong,%{_desktopdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}/

cp -a fallbacktiles tiles-numbered tiles-small tiles-v1 \
	$RPM_BUILD_ROOT%{_datadir}/mah-jong

install %SOURCE1 $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES ChangeLog README rules.txt use.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mah-jong
%{_desktopdir}/mj.desktop
%{_mandir}/man6/*.6*
