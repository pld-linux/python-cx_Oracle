%define module cx_Oracle
Summary:	Python interface to Oracle
Name:		python-%{module}
Version:	2.5a
Release:	0.1
Source0:	http://www.computronix.com/download/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Libraries
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Vendor:		Anthony Tuininga <anthony@computronix.com>
Url:		http://www.computronix.com/utilities.html

%description
Python interface to Oracle conforming to the Python DB API 2.0
specification. See
http://www.python.org/topics/database/DatabaseAPI-2.0.html.

%prep
%setup -q -n %{module}-%{version}

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt HISTORY.txt
