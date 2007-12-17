%define name	fityk
%define version 0.7.7
%define release %mkrel 1

Name:		%{name}
Summary:	Non-linear curve fitting and data analysis
Version:	%{version}
Release:	%{release}

Source0:	http://prdownloads.sourceforge.net/fityk/%{name}-%{version}.tar.bz2
Source1:	%{name}48.png
Source2:	%{name}32.png
Source3:	%{name}16.png
URL:		http://www.unipress.waw.pl/~wojdyr/fityk/
License:	GPL
Group:		Sciences/Other
BuildRequires:	wxGTK-devel readline-devel ncurses-devel
BuildRequires:  boost-devel
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

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --with-wx-config=%_bindir/wx-config-ansi
perl -p -i -e 's|mkdir|mkdir -p||g' doc/Makefile
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="Fityk" longtitle="Data analysis" section="More Applications/Sciences/Other"
EOF

#icons
install -m644 %{SOURCE1} -D $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png
install -m644 %{SOURCE2} -D $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
install -m644 %{SOURCE3} -D $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog doc/* samples NEWS
%{_bindir}/%{name}
%{_bindir}/c%{name}
%{_datadir}/%name
%{_mandir}/man1/*
%{_menudir}/%{name}
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/*
%{_datadir}/pixmaps/*


