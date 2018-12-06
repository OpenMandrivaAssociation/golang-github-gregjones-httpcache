# Run tests in check section
%bcond_without check

%global goipath         github.com/gregjones/httpcache
%global commit          9cad4c3443a7200dd6400aef47183728de563a38

%global common_description %{expand:
Package httpcache provides a http.RoundTripper implementation that works 
as a mostly RFC 7234 compliant cache for http responses.}

%gometa 

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        A Transport for http.Client that will cache responses according to the HTTP RFC
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/bradfitz/gomemcache/memcache)
BuildRequires: golang(github.com/garyburd/redigo/redis)
BuildRequires: golang(github.com/peterbourgon/diskv)
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git9cad4c3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180417git9cad4c3
- First package for Fedora

