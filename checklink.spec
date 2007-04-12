%define name checklink

%define realname W3C-LinkChecker

%define version 4.2.1
%define release %mkrel 2

Summary: A tools to check link on website
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.cpan.org/authors/id/S/SC/SCOP/W3C-LinkChecker-%{version}.tar.bz2
License: W3C License
Group: Networking/WWW
Url: http://validator.w3.org/docs/checklink.html
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Provides: W3C-LinkChecker = %version-%release
# To follow perl module policy naming:
Provides: perl-W3C-LinkChecker = %version-%release
BuildRequires: perl(CGI)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTML::Parser) >= 3.00
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(LWP::RobotUA)
BuildRequires: perl(Net::IP)
BuildRequires: perl(Net::hostent)
BuildRequires: perl(Socket)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(URI)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(URI::file)

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
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

mkdir -p %buildroot%_var/www/cgi-bin/

cp %buildroot%_bindir/%name %buildroot%_var/www/cgi-bin/%{name}.cgi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/%name
%_var/www/cgi-bin/%{name}.cgi
%_mandir/man*/%{name}*
%doc docs/*
%doc README ChangeLog


