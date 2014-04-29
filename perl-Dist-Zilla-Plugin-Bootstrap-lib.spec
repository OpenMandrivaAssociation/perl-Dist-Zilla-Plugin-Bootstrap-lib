%define upstream_name    Dist-Zilla-Plugin-Bootstrap-lib
%define upstream_version 0.04000002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    A minimal boot-strapping for Dist::Zilla Plug-ins

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
BuildRequires: perl(JSON::PP)
BuildArch: noarch

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
./Build install destdir=%{buildroot}

%clean

%files
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*
