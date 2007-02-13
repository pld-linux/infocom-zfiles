%define		_name		zfiles
Summary:	Infocom game list
Summary(pl.UTF-8):	Lista tekstówek Infocomu
Name:		infocom-zfiles
Version:	980519
Release:	2
License:	free
Group:		Applications/Games
Source0:	ftp://ftp.ifarchive.org/if-archive/games/zcode/%{_name}.z8
# Source0-md5:	8780769d82ea581b186089feb478c17a
URL:		http://www.ifarchive.org/
Requires:	zcode-wrapper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This is a list of all English Z-code files that are legally available.
Therefore, it includes mainly files compiled by Graham Nelson's
Inform, but Activision has released some old Infocom games into the
public.

Please understand that due to the majority of English games,
"minorities" like German and Spanish games cannot be supported.

%description -l pl.UTF-8
Jest to pełna lista wszystkich legalnie dostępnych angielskich plików
Z-cyferka. Zatem zawiera ona głównie pliki skompilowane przez Inform
Grahama Nelsona, jednakże Activision udostępniło publicznie niektóre
stare gry Infocoma.

Proszę zrozumieć, że ze względu na przewagę gier angielskich,
"mniejszości", takie jak gry niemiecki czy hiszpańskie, nie mogą być
wspierane.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/zcode}

cp %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/games/zcode
ln -s %{_datadir}/games/zcode/wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/zcode/*.z8
