# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       org.harbour.advancedcamera

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Advanced camera
Version:    0.9.8
Release:    1
Group:      Qt/Qt
License:    GPLv2
URL:        http://github.com/piggz/harbour-advanced-camera
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-advanced-camera.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  qt5-qttools-linguist
BuildRequires:  ssu-sysinfo-devel
BuildRequires:  libexif-devel
BuildRequires:  desktop-file-utils

%description
Advanced Camera (aka piggz-o-vision) is a community camera application for sailfish devices which utilises the latest features in 3.0.2 to query/set parameters supported by the device.

Allows full control over:
    Effects
    Exposure/scene modes
    Focus mode
    Resolution
    White Balance
    Flash mode
    ISO

Currently selected parameters are displayed on the buttons where possible.

Tapping the screen sets the focus circle when in Auto/Macro/Continuous

Hold the shutter button to focus and take an image when in Auto/Macro/Continuous focus mode, other modes take an instant image.

Exposure mode will typically provide a HDR mode for taking HDR images.

%if "%{?vendor}" == "chum"
PackageName: Advanced Camera
Type: desktop-application
DeveloperName: Adam Pigg
Categories:
 - Media
 - Video
Custom:
  Repo: https://github.com/piggz/harbour-advanced-camera
Icon: https://raw.githubusercontent.com/piggz/harbour-advanced-camera/master/harbour-advanced-camera.svg
Screenshots:
 - https://github.com/piggz/harbour-advanced-camera/raw/master/screenshots/screenshot4.png
 - https://github.com/piggz/harbour-advanced-camera/raw/master/screenshots/screenshot5.png
 - https://github.com/piggz/harbour-advanced-camera/raw/master/screenshots/screenshot6.png
Url:
  Homepage: https://github.com/piggz/harbour-advanced-camera
  Help: https://github.com/piggz/harbour-advanced-camera/discussions
  Bugtracker: https://github.com/piggz/harbour-advanced-camera/issues
  Donation: https://www.paypal.me/piggz
%endif

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
