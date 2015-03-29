Name:		helloserver
Version:	master
Release:	1%{?dist}
Summary:	the awesome hello command

Group:		Eugen Cuckoo Memorial Committee
License:	ASF 2.0
URL:		https://www.apache.org/licenses/LICENSE-2.0.html
Source0:	https://github.com/K0zka/helloserver/archive/master.tar.gz

BuildRequires:	make
BuildRequires:	gcc
Requires:	glibc

%description
hello helps greeting just anyone as long as the greeting is hello

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc
/usr/sbin/hello


%changelog

