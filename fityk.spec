%define name	fityk
%define version 0.8.2
%define release %mkrel 1

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		%{name}
Summary:	Non-linear curve fitting and data analysis
Version:	%{version}
Release:	%{release}

Source0:	http://prdownloads.sourceforge.net/fityk/%{name}-%{version}.tar.bz2
URL:		http://www.unipress.waw.pl/~wojdyr/fityk/
License:	GPL
Group:		Sciences/Other
BuildRequires:	wxGTK-devel readline-devel ncurses-devel
BuildRequires:  boost-devel
BuildRequires:	desktop-file-utils
Requires:	gnuplot

%description
Fityk is nonlinear curve-fitting and data analysis software. It allows data
visualization, separation of overlapping peaks, and least squares fitting
using standard Levenberg-Marquardt algorithm, a genetic algorithm, or
Nelder-Mead simplex method. It only knows about common bell-shaped functions
(Gaussian, Loretzian, Pearson 7, Voigt, Pseudo-Voigt) and polynomials, but
more sophisticated formulae can be easily added if necessary. It also
enables background substracting, data calibration and task automation with a
simple script language. It is being developed to analyze powder diffraction
patterns, but it can be used to fit analytical functions to any kind of data.

%package -n     %{libname}
Summary:        Main library for %name 
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %name.

%package -n     %{develname}
Summary:        Headers for developing programs that will use %name
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %name.

%prep
%setup -q
perl -pi -e 's|.png|||g' fityk.desktop

%build
%configure2_5x
perl -p -i -e 's|mkdir|mkdir -p||g' doc/Makefile
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Sciences-Mathematics;Science;Math;" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc README samples NEWS
%{_bindir}/%{name}
%{_bindir}/c%{name}
%{_datadir}/%name
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*

%files -n %{libname}
%{_libdir}/lib*.so.*

%files -n %{develname}
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.la
