%define upstream_name	 File-DesktopEntry
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    6

Summary:	Object to handle .desktop files
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::BaseDir)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
This module is used to work with .desktop files. The format of these files is
specified by the freedesktop "Desktop Entry" specification.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/File/DesktopEntry.pm


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-4mdv2012.0
+ Revision: 765238
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-2
+ Revision: 667138
- mass rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 407688
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.04-3mdv2009.1
+ Revision: 351744
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.04-2mdv2009.0
+ Revision: 223719
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Nov 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.1
+ Revision: 106564
- switch to M::B
- new version

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 0.02-3mdv2008.0
+ Revision: 64755
- rebuild


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.02-2mdv2007.0
+ Revision: 108536
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-File-DesktopEntry

* Tue Oct 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.02-1mdk
- First MDV package

