%define major 3
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		fityk
Summary:	Non-linear curve fitting and data analysis
Version:	0.9.8
Release:	2
License:	GPLv2+
Group:		Sciences/Other
URL:		https://www.unipress.waw.pl/fityk/
Source0:	http://prdownloads.sourceforge.net/fityk/%{name}-%{version}.tar.bz2
BuildRequires:	wxgtku-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	boost-devel
BuildRequires:	xylib-devel
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

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x	--disable-3rdparty \
		--disable-xyconvert
%make

%install
%makeinstall_std

desktop-file-install	--vendor="" \
	--remove-category="Education" \
	--add-category="X-MandrivaLinux-MoreApplications-Sciences-DataVisualization" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%files
%doc README NEWS
%{_bindir}/%{name}
%{_bindir}/c%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/*.h
%{_libdir}/*.so

