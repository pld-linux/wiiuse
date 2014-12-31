Summary:	Wiiuse - library for several Nintendo Wii controllers
Summary(pl.UTF-8):	Wiiuse - biblioteka do kilku kontrolerów Nintendo Wii
Name:		wiiuse
Version:	0.12
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/wiiuse/%{name}_v%{version}_src.tar.gz
# Source0-md5:	29b555096f79dbd3fbc9b96b8d443083
URL:		http://sourceforge.net/projects/wiiuse/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	SDL-devel
BuildRequires:	bluez-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wiiuse is a library written in C that connects with several Nintendo
Wii remotes. Supports motion sensing, IR tracking, nunchuk, classic
controller, and the Guitar Hero 3 controller. Single threaded and
nonblocking makes a light weight and clean API.

%description -l pl.UTF-8
Wiiuse to napisana w C biblioteka komunikująca się z kilkoma zdalnymi
kontrolerami Nintendo Wii. Obsługuje czujnik ruchu, śledzenie
podczerwienią, nunchuk, kontroler klasyczny oraz kontroler Guitar Hero
3. Jest jednowątkowa i nieblokująca, dzięki czemu API jest lekkie i
czyste.

%package devel
Summary:	Header files for wiiuse library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wiiuse
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bluez-libs-devel

%description devel
Header files for wiiuse library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wiiuse.

%prep
%setup -q -n %{name}_v%{version}

%build
%{__make} -j1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -pipe -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

# make install doesn't support DESTDIR nor proper libdir
install src/release-*/libwiiuse.so $RPM_BUILD_ROOT%{_libdir}
cp -p src/wiiuse.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_libdir}/libwiiuse.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/wiiuse.h
