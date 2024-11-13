Name:           bluetooth-suspend-fix
Version:        0.0.0
Release:        0%{?dist}
License:        MIT
Summary:        Installs a script in /usr/bin/say that calls espeak        
Url:            https://github.com/dkolb/%{name}
Source0:        %{name}-%{version}.tar.gz

#BuildRequires:
Requires:       systemd
Requires:       rfkill

%description
Installs a script to rfkill your bluetooth on suspend and then
unkill it on wake

%prep
%autosetup

%install 
install -d %{buildroot}/usr/lib/systemd/system-sleep
install bluetooth %{buildroot}/usr/lib/systemd/system-sleep/bluetooth

%files
%license LICENSE
/usr/lib/systemd/system-sleep/bluetooth
%doc README.md AUTHORS

%changelog
