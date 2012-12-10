%define name checklink

%define realname W3C-LinkChecker

%define version 4.81
%define rel 1

%if %{mdvver} < 201100
%define release %mkrel %{rel}
%else
%define release %{rel}
%endif

Summary:	A tools to check link on website
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SC/SCOP/%{realname}-%{version}.tar.gz
License:	W3C License
Group:		Networking/WWW
Url:		http://search.cpan.org/dist/W3C-LinkChecker/
BuildArch:	noarch
Provides:	%{realname} = %version-%release
# To follow perl module policy naming:
Provides:	perl-W3C-LinkChecker = %version-%release
BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(HTML::Parser) >= 3.00
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(LWP::RobotUA)
BuildRequires:	perl(Net::IP)
BuildRequires:	perl(Net::hostent)
BuildRequires:	perl(Socket)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(URI)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(URI::file)
BuildRequires:	perl(WWW::RobotRules)
BuildRequires:	perl(CSS::DOM)
BuildRequires:	perl(Config::General)
BuildRequires:	perl(Term::ReadKey)

%description
The link checker reads an HTML or XHTML document and extracts a list of anchors
and links.

It checks that no anchor is defined twice. 

It then checks that all the links are dereferenceable, including the fragments.
It warns about HTTP redirects, including directory redirects. 

It can check recursively a part of a Web site. 

There is a command line version and a CGI version. They both support HTTP basic
authentication. This is achieved in the CGI version by passing through the
authorization information from the user browser to the site tested. 

%prep
%setup -q -n %realname-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

mkdir -p %buildroot%_var/www/cgi-bin/

cp %buildroot%_bindir/%name %buildroot%_var/www/cgi-bin/%{name}.cgi

%files
%defattr(-,root,root)
%_bindir/%name
%{perl_vendorlib}/W3C/LinkChecker.pm
%_var/www/cgi-bin/%{name}.cgi
%_mandir/man*/%{name}*
%doc docs/*
%doc README NEWS


%changelog
* Wed Apr 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 4.81-1
+ Revision: 789171
- fix BR
- update to 4.81

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 4.2.1-7mdv2011.0
+ Revision: 616997
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 4.2.1-6mdv2010.0
+ Revision: 424824
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 4.2.1-5mdv2009.0
+ Revision: 240522
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Sep 11 2007 Emmanuel Andry <eandry@mandriva.org> 4.2.1-3mdv2008.0
+ Revision: 84540
- rebuild


* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 21:52:46 (53014)
- rebuild
- test in %%check

* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 21:49:59 (53011)
Import checklink

* Mon Apr 17 2006 Olivier Thauvin <nanardon@mandriva.org> 4.2.1-1mdk
- 4.2.1

* Tue Apr 05 2005 Olivier Thauvin <nanardon@zarb.org> 4.1-1mdk
- 4.1

* Fri Jul 30 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.0-1mdk
- 4.0
- rework build process (now it a CPAN module)

* Wed Apr 07 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.6.2.26-2mdk
- fix cgi path

* Thu Apr 01 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.6.2.26-1mdk
- make a spec file

