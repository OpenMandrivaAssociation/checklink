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
