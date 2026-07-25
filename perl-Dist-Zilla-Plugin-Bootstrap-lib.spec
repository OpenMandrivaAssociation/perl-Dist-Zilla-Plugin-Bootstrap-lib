%define upstream_name    Dist-Zilla-Plugin-Bootstrap-lib
%define upstream_version 1.001002

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    1

Summary:    A minimal boot-strapping for Dist::Zilla Plug-ins
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://github.com/kentnl/Dist-Zilla-Plugin-Bootstrap-lib
Source0:    https://cpan.metacpan.org/authors/id/K/KE/KENTNL/Dist-Zilla-Plugin-Bootstrap-lib-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module does the very simple task of injecting the distributions 'lib'
directory into @INC at the point of its inclusion, so that you can use
plug-ins you're writing for Dist::Zilla, to release the plug-in itself.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.10.0.30-2mdv2011.0
+ Revision: 653565
- rebuild for updated spec-helper

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0.30-1mdv2011.0
+ Revision: 572815
- import perl-Dist-Zilla-Plugin-Bootstrap-lib

