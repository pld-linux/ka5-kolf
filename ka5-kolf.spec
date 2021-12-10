%define		kdeappsver	21.12.0
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kolf
Summary:	kolf
Name:		ka5-%{kaname}
Version:	21.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	02acfbdbf325beeeb469e44b8fb27a0c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kolf is a miniature golf game. The game is played from an overhead
view, with a short bar representing the golf club. Kolf features many
different types of objects, such water hazards, slopes, sand traps,
and black holes (warps), among others.

%description -l pl.UTF-8
Kolf jest miniaturową grą w golfa. Gra jest pokazywana z z góry,
z małą poprzeczką reprezentującą klub golfowy. Kolf zawiera
wiele różnych typów obiektów, takich jak pułapki wodne, zbocza,
pułapki piaskowe i czarne dziury.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolf
%{_desktopdir}/org.kde.kolf.desktop
%{_iconsdir}/hicolor/128x128/apps/kolf.png
%{_iconsdir}/hicolor/16x16/apps/kolf.png
%{_iconsdir}/hicolor/22x22/apps/kolf.png
%{_iconsdir}/hicolor/32x32/apps/kolf.png
%{_iconsdir}/hicolor/48x48/apps/kolf.png
%{_iconsdir}/hicolor/64x64/apps/kolf.png
%{_iconsdir}/hicolor/scalable/apps/kolf.svgz
%{_datadir}/kolf
%{_datadir}/kxmlgui5/kolf
%{_datadir}/metainfo/org.kde.kolf.appdata.xml
