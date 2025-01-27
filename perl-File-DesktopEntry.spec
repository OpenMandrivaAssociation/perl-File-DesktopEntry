%define modname	File-DesktopEntry
%define modver 0.22

Summary:	Object to handle .desktop files

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/File/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(File::BaseDir)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module is used to work with .desktop files. The format of these files is
specified by the freedesktop "Desktop Entry" specification.

%prep
%setup -qn %{modname}-%{modver}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
%make test

%install
%make_install

%files
%doc README.md Changes
%{perl_vendorlib}/File/DesktopEntry.pm
%{_mandir}/man3/*
