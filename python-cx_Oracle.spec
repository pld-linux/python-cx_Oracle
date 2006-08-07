%define	module	cx_Oracle
Summary:	Python interface to Oracle
Summary(pl):	Interfejs Pythona do Oracle'a
Name:		python-%{module}
Version:	4.2
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/cx-oracle/%{module}-%{version}.tar.gz
# Source0-md5:	fe878a70d3695cea2bb5533044f8f833
URL:		http://www.cxtools.net/default.aspx?nav=cxorlb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to Oracle conforming to the Python DB API 2.0
specification. See
http://www.python.org/topics/database/DatabaseAPI-2.0.html.

%description -l pl
Interfejs Pythona do Oracle, zgodny ze specyfikacj± Python DB API 2.0.
Wiêcej informacji pod adresem
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
