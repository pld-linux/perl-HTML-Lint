#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Lint
Summary:	Test::HTML::Lint - Test::More-style wrapper around HTML::Lint
#Summary(pl):	
Name:		perl-HTML-Lint
Version:	2.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/P/PE/PETDANCE/HTML-Lint-2.02.tar.gz
# Source0-md5:	f08241fbe2473d7542be5ef660ced6e3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTML::Parser) >= 3.20
BuildRequires:	perl(HTML::Tagset) >= 3.03
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a few convenience methods for testing exception
based code. It is built with Test::Builder and plays happily with
Test::More and friends.

If you are not already familiar with Test::More now would be the time
to go take a look.

# %description -l pl
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/*.pm
%{perl_vendorlib}/HTML/Lint
%{perl_vendorlib}/Test/HTML/Lint.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_bindir}/weblint
