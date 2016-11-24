Name:           kio-gdrive
Version:        1.0.4
Release:        1%{?dist}
Summary:        KIO Google Drive

License:        GPLv2+
URL:            https://phabricator.kde.org/source/kio-gdrive/
Source0:        http://download.kde.org/stable/kio-gdrive/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake(KF5GAPI)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils

Requires:       application(org.kde.dolphin.desktop)

%description
Google Drive for KDE

%prep
%autosetup


%build
mkdir build
pushd build
    %cmake_kf5 ..
    %make_build
popd

%install
pushd build
    rm -rf $RPM_BUILD_ROOT
    %make_install
popd
%find_lang kio5_gdrive

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f kio5_gdrive.lang
%license COPYING
%doc HACKING README.md
%{_qt5_plugindir}/kf5/kio/*
%{_datadir}/applications/*

%changelog
* Wed Nov 23 2016 vascom <vascom2@gmail.com> - 1.0.4-1
- Initial release
