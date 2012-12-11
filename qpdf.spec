%define major 8
%define libname %mklibname qpdf %{major}
%define develname %mklibname qpdf -d

Name:		qpdf
Summary:	Inspect and manipulate PDF files
Version:	3.0.2
Release:	1
Group:		Office
License:	Artistic
URL:		http://sourceforge.net/projects/qpdf/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	zlib-devel
BuildRequires:	pcre-devel

%description
QPDF is a C++ library and set of programs that inspect and manipulate
the structure of PDF files. It can encrypt and linearize files, expose
the internals of a PDF file, and do many other operations useful to end
users and PDF developers.

%package -n	%{libname}
Summary:	Inspect and manipulate PDF files library
Group:		System/Libraries

%description -n %{libname}
QPDF is a C++ library and set of programs that inspect and manipulate
the structure of PDF files. It can encrypt and linearize files, expose
the internals of a PDF file, and do many other operations useful to end
users and PDF developers.

%package -n	%{develname}
Summary:	Static library and header files for the qpdf library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Provides:	qpdf-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Devel package for %{name}

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc Artistic-2.0 ChangeLog README* TODO
%{_bindir}/fix-qdf
%{_bindir}/%{name}
%{_bindir}/zlib-flate
%{_mandir}/man1/fix-qdf.1.*
%{_mandir}/man1/qpdf.1.*
%{_mandir}/man1/zlib-flate.1.*

%files -n %{develname}
%{_includedir}/%{name}/*.h
%{_includedir}/%{name}/*.hh
%{_libdir}/libqpdf.so
%{_libdir}/pkgconfig/libqpdf.pc

%files -n %{libname}
%{_libdir}/libqpdf.so.%{major}*

