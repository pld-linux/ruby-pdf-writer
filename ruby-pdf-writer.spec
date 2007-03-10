Summary:	PDF generator for Ruby
Name:		ruby-pdf-writer
Version:	1.1.3
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/5991/pdf-writer-%{version}.tar.gz
# Source0-md5:	5e184fd01c3929b0d0d5269279472d4b
#Patch0: %{name}-nogems.patch
URL:		http://ruby-pdf.rubyforge.org/pdf-writer/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
#BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-color-tools
Requires:	ruby-transaction-simple
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDF::Writer for Ruby provides the ability to create PDF documents
using only native Ruby libraries. There are several demo programs
available in the demo/ directory. The canonical documentation for
PDF::Writer is the 95-page manual, manual.pdf, generated using
bin/techbook (just techbook for RubyGem users) and the manual file
manual.pwd.

%prep
%setup -q -n pdf-writer-%{version}
#%patch0 -p1
#cp %{_datadir}/setup.rb .

%build
rm pre-setup.rb
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
