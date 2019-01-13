%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kolf
Summary:	kolf
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2123a7267b77e38b6882955115f0c4be
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-kcompletion-devel >= 5.30.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdelibs4support-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kio-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
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

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
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
%attr(755,root,root) %{_libdir}/libkolfprivate.so.5.*.*
%{_desktopdir}/org.kde.kolf.desktop
%{_iconsdir}/hicolor/128x128/apps/kolf.png
%{_iconsdir}/hicolor/16x16/apps/kolf.png
%{_iconsdir}/hicolor/22x22/apps/kolf.png
%{_iconsdir}/hicolor/32x32/apps/kolf.png
%{_iconsdir}/hicolor/48x48/apps/kolf.png
%{_iconsdir}/hicolor/64x64/apps/kolf.png
%{_datadir}/kolf
%{_datadir}/kxmlgui5/kolf
%{_datadir}/metainfo/org.kde.kolf.appdata.xml
