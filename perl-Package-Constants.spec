#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Package
%define	pnam	Constants
Summary:	Package::Constants - List all constants declared in a package
#Summary(pl.UTF-8):	
Name:		perl-Package-Constants
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Package/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4027c258b0163322f8f220f253e81142
# generic URL, check or change before uncommenting
URL:		http://search.cpan.org/dist/Package-Constants/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package::Constants lists all the constants defined in a certain 
package. This can be useful for, among others, setting up an 
autogenerated @EXPORT/@EXPORT_OK for a Constants.pm file.


# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Package/*.pm
#%%{perl_vendorlib}/Package/Constants
%{_mandir}/man3/*
