Name:           game-music-emu
Version:        0.6.1
Release:        2%{?dist}
Provides:       libgme%{?_isa} = %{version}-%{release}
Summary:        Video game music file emulation/playback library
License:        LGPLv2+
URL:            https://bitbucket.org/mpyne/game-music-emu/wiki/Home
Source0:        https://bitbucket.org/mpyne/game-music-emu/downloads/%{name}-%{version}.tar.bz2

BuildRequires:  cmake
# needed to build the player
BuildRequires:  SDL-devel

%package devel
Summary:        Development files for Game_Music_Emu
Provides:       libgme-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}
Requires:       pkgconfig

%package player
Summary:        Demo player utilizing Game_Music_Emu
License:        MIT


%description
Game_Music_Emu is a collection of video game music file emulators that support
the following formats and systems:

 * AY       ZX Spectrum/Amstrad CPC
 * GBS      Nintendo Game Boy
 * GYM      Sega Genesis/Mega Drive
 * HES      NEC TurboGrafx-16/PC Engine
 * KSS      MSX Home Computer/other Z80 systems (doesn't support FM sound)
 * NSF/NSFE Nintendo NES/Famicom (with VRC 6, Namco 106, and FME-7 sound)
 * SAP      Atari systems using POKEY sound chip
 * SPC      Super Nintendo/Super Famicom
 * VGM/VGZ  Sega Master System/Mark III, Sega Genesis/Mega Drive,BBC Micro

%description devel
This package contains files needed to compile code which uses Game_Music_Emu.

%description player
This package contains the demo player for files supported by Game_Music_Emu.


%prep
%setup -q
# add install rule for the player
echo -e "\ninstall(TARGETS gme_player RUNTIME DESTINATION %{_bindir})" >> player/CMakeLists.txt


%build
%cmake
make %{?_smp_mflags}
# explicitly build the player as it has EXCLUDE_FROM_ALL set
make %{?_smp_mflags} gme_player


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
# explicitly install the player as it has EXCLUDE_FROM_ALL set
cd player
make install DESTDIR=%{buildroot}
cd ..


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc changes.txt license.txt readme.txt
%{_libdir}/libgme.so.*

%files devel
%doc design.txt gme.txt
%{_libdir}/libgme.so
%{_includedir}/gme/
%{_libdir}/pkgconfig/libgme.pc

%files player
%{_bindir}/gme_player


%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Karel Volný <kvolny@redhat.com> 0.6.1-1
- New release 0.6.1
- Fixes CVE-2016-9959 (security issues in SNES emulation)
  https://scarybeastsecurity.blogspot.cz/2016/12/redux-compromising-linux-using-snes.html
- Updated URLs - project moved
- Dropped gme-0.6.0-pc-lib-suffix.patch (accepted upstream)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 20 2013 Karel Volný <kvolny@redhat.com> 0.6.0-3
- Adjust virtual provides according to further comments on bug#1006881

* Fri Sep 13 2013 Karel Volný <kvolny@redhat.com> 0.6.0-2
- Add virtual provides libgme (bug #1006881)

* Thu Aug 22 2013 Karel Volný <kvolny@redhat.com> 0.6.0-1
- New release
- See changes.txt for list of upstream changes
- Adds pkgconfig file (+ patch to correct path)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Karel Volny <kvolny@redhat.com> 0.5.5-1
- Initial release for Fedora 15
