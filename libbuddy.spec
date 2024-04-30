Name:     libbuddy
Version:  2.4
Release:  %autorelease
Summary:  Binary Decision Diagram library
License:  MIT
URL:      https://sourceforge.net/projects/buddy/
Source:   https://downloads.sourceforge.net/project/buddy/buddy/BuDDy%20%{version}/buddy-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  bash
BuildRequires:  flex
BuildRequires:  bison

%description
A Binary Decision Diagram library, with
many highly efficient vectorized BDD operations,
dynamic variable reordering,
automated garbage collection,
a C++ interface with automatic reference counting,
and much more.

%prep
%setup -q -n buddy-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%{_includedir}/bdd.h
%{_includedir}/bvec.h
%{_includedir}/fdd.h
%{_libdir}/libbdd.a
%{_libdir}/libbdd.so
%{_libdir}/libbdd.so.0
%{_libdir}/libbdd.so.0.0.0

%license README
%doc README AUTHORS ChangeLog NEWS

%changelog
%autochangelog
