%define module	File-DesktopEntry
%define name	perl-%{module}
%define version 0.04
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Object to handle .desktop files
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.gz
BuildRequires:	perl(File::BaseDir)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module is used to work with .desktop files. The format of these files is
specified by the freedesktop "Desktop Entry" specification.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/File/DesktopEntry.pm


