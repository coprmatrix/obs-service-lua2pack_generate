%define service lua2pack_generate
Name:           obs-service-lua2pack_generate
Version:        0.0.1
Release:        0
Summary:        Obs service that will run lua2pack generate command
License:        GPL-3.0-or-later
URL:            https://github.com/huakim-tyk/%{name}
Group:          Development/Tools/Building
BuildArch:      noarch
BuildRequires:  rpm_macro(_obs_service_dir)
Requires:       python3-lua2pack >= 1.0.4
Source0:        %{service}
Source1:        %{service}.service
%description
%{summary}.

%install
%define file %{_obs_service_dir}/%{service}
%define script %{buildroot}%{file}

install -Dm755 %{SOURCE0} %{script}
install -Dm644 %{SOURCE1} %{script}.service

%post
%postun

%files
%{file}
%{file}.service

%changelog
