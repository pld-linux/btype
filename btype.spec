Summary:	.torrent file editor
Summary(pl.UTF-8):	Edytor plików .torrent
Name:		btype
Version:	0.4.1
Release:	1
License:	GPLv2
Group:		X11/Applications
Source0:	http://kde-apps.org/CONTENT/content-files/25051-%{name}-%{version}.tar.bz2
# Source0-md5:	833123eeacda38a0b585af5b35e18cc7
URL:		http://kde-apps.org/content/show.php/.torrent+file+editor?content=25051
BuildRequires:	kdelibs-devel
BuildRequires:	scons
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy-to-use program for editing torrent files. It supports
read, edit and save.

%description -l pl.UTF-8
Prosty w obsłudze program do edycji plików torrent. Wspiera
odczyt, edycję i zapisywanie.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcxxflags}"
QTDIR=%{_prefix}
export CXXFLAGS QTDIR

./configure \
	debug=0 \
	prefix=%{_prefix} \
	qtincludes=%{_includedir}/qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README
%attr(755,root,root) %{_bindir}/btype
