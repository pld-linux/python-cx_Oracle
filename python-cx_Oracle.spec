%define	module	cx_Oracle
Summary:	Python interface to Oracle
Summary(pl.UTF-8):	Interfejs Pythona do Oracle'a
Name:		python-%{module}
Version:	5.1
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/cx-oracle/%{module}-%{version}.tar.gz
# Source0-md5:	d2697493a40c9d46c9b7c1c210b61671
Patch0:		%{name}-instantclient.patch
URL:		http://www.cxtools.net/default.aspx?nav=cxorlb
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _preserve_env %_preserve_env_base ORACLE_HOME

%description
Python interface to Oracle conforming to the Python DB API 2.0
specification. See
http://www.python.org/topics/database/DatabaseAPI-2.0.html.

%description -l pl.UTF-8
Interfejs Pythona do Oracle, zgodny ze specyfikacją Python DB API 2.0.
Więcej informacji pod adresem
http://www.python.org/topics/database/DatabaseAPI-2.0.html.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
env CFLAGS="%{rpmcflags}" %py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt HISTORY.txt
