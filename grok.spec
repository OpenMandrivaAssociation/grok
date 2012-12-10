%define upstream_name    App-Grok
%define appli_name       grok
%define upstream_version 0.21

Name:       %{appli_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    A Pod 6 backend for grok
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{appli_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IO::Interactive)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Perl6::Doc)
BuildRequires: perl(Perl6::Perldoc)
BuildRequires: perl(Perl6::Perldoc::To::Ansi)
BuildRequires: perl(Perl::Critic)
BuildRequires: perl(Pod::Perldoc::ToPod)
BuildRequires: perl(Pod::Text::Ansi)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Pod::Xhtml)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Perl::Critic)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Script)
BuildRequires: perl-devel

BuildArch: noarch

%description
This class provides the main functionality needed by grok. It has some
methods you can use if you need to hook into grok.

%prep
%setup -q -n %{appli_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/grok
/usr/share/man/man1/*



%changelog
* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2011.0
+ Revision: 552263
- adding missing buildrequires:
- update to 0.21
- update to 0.19

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.1
+ Revision: 460979
- update to 0.19

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.0
+ Revision: 418405
- update to 0.19

* Mon Jul 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 400632
- update to 0.17

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 399602
- update to 0.15

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 396842
- update to 0.13

* Wed Jul 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 396377
- adding missing buildrequires:
- update to 0.12

* Sat Jul 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 394701
- adding missing buildrequires:
- import grok


* Sat Jul 11 2009 cpan2dist 0.11-1mdv
- initial mdv release, generated with cpan2dist
