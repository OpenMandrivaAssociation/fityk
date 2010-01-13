%define name	fityk
%define version 0.9.0
%define release %mkrel 1

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		%{name}
Summary:	Non-linear curve fitting and data analysis
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Sciences/Other
URL:		http://www.unipress.waw.pl/fityk/
Source0:	http://prdownloads.sourceforge.net/fityk/%{name}-%{version}.tar.bz2
Patch0:		fityk-0.9.0-fix-format-errors.patch
BuildRequires:	wxGTK-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:  boost-devel
BuildRequires:	xylib-devel
BuildRequires:	desktop-file-utils
Requires:	gnuplot
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%patch0 -p 1 -b .strfmt

%build
%configure2_5x	--disable-3rdparty \
		--disable-xyconvert \
		--with-samples
%make
										
%install
rm -rf %{buildroot}
%makeinstall

desktop-file-install --vendor="" \
 --remove-category="Education" \
 --add-category="X-MandrivaLinux-MoreApplications-Sciences-DataVisualization" \
 --dir %{buildroot}%{_datadir}/applications \
 %{buildroot}%{_datadir}/applications/*

%find_lang %name

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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
