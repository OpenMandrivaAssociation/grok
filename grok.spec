%define upstream_name    App-Grok
%define appli_name       grok
%define upstream_version 0.12

Name:       %{appli_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A Pod 6 backend for grok
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{appli_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IO::Interactive)
BuildRequires: perl(Perl6::Perldoc)
BuildRequires: perl(Perl6::Perldoc::To::Ansi)
BuildRequires: perl(Perl::Critic)
BuildRequires: perl(Pod::Perldoc::ToPod)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Pod::Xhtml)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Perl::Critic)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Script)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/grok
/usr/share/man/man1/grok.1.lzma

