%global packname  TSP
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.7
Release:          2
Summary:          Traveling Salesperson Problem (TSP)
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/TSP_1.0-7.tar.gz
Requires:         R-maps R-sp R-maptools 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-maps R-sp R-maptools 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Basic infrastructure and some algorithms for the traveling salesperson
problem (also traveling salesman problem; TSP). The package provides some
simple algorithms and an interface to Concorde, the currently fastest TSP
solver. Concorde itself is not included in the package and has to be
obtained separately.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
