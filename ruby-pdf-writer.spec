Summary:	PDF generator for Ruby
Summary(pl.UTF-8):	Generator PDF dla Ruby
Name:		ruby-pdf-writer
Version:	1.1.8
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/33973/pdf-writer.%{version}.tar.bz2
# Source0-md5:	84c0e3045c99ca0bb27dfa728d4479e3
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
using only native Ruby libraries.

%description -l pl.UTF-8
PDF::Writer dla Ruby dostarcza możliwość tworzenia dokumentów PDF przy
użyciu jedynie natywnych bibliotek Ruby.

%prep
%setup -q -n pdf_writer-%{version}
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
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}/images}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
sed -i -e 's|../images|./images|g' demo/chunkybacon.rb
cp demo/*.rb $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r images/chunkybacon.* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
%{_examplesdir}/%{name}-%{version}
