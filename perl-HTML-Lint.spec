#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Lint
Summary:	HTML::Lint - check for HTML errors in a string or file
Summary(pl.UTF-8):	HTML::Lint - sprawdzanie łańcucha lub pliku HTML pod kątem błędów
Name:		perl-HTML-Lint
Version:	2.06
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	60bd27c6ff0bb291a9fead0cd474b75f
URL:		http://search.cpan.org/dist/HTML-Lint/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Parser >= 3.20
BuildRequires:	perl-HTML-Tagset >= 3.03
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Lint checks a string or file for HTML errors. It comes with
Test::More-style wrapper, Test::HTML::Lint.

%description -l pl.UTF-8
HTML::Lint sprawdza łańcuch znaków lub plik HTML pod kątem błędów.
Pakiet zawiera też moduł Test::HTML::Lint - wrapper w stylu
Test::More.

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
%attr(755,root,root) %{_bindir}/weblint
%{perl_vendorlib}/HTML/*.pm
%{perl_vendorlib}/HTML/Lint
%dir %{perl_vendorlib}/Test/HTML
%{perl_vendorlib}/Test/HTML/Lint.pm
%{_mandir}/man3/*
