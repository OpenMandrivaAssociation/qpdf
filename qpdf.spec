%define major 29
%define libname %mklibname qpdf
%define devname %mklibname qpdf -d

Summary:	Inspect and manipulate PDF files
Name:		qpdf
Version:	11.6.4
Release:	1
Group:		Office
License:	Artistic
Url:		http://sourceforge.net/projects/qpdf/
Source0:	http://sourceforge.net/projects/qpdf/files/qpdf/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	cmake ninja

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

%package -n	%{devname}
Summary:	Development library and header files for the qpdf library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Devel package for %{name}

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%doc Artistic-2.0 ChangeLog README*
%{_bindir}/fix-qdf
%{_bindir}/%{name}
%{_bindir}/zlib-flate
%{_mandir}/man1/fix-qdf.1.*
%{_mandir}/man1/qpdf.1.*
%{_mandir}/man1/zlib-flate.1.*

%files -n %{libname}
%{_libdir}/libqpdf.so.%{major}*

%files -n %{devname}
%doc %{_docdir}/qpdf
%{_includedir}/%{name}/*.h
%{_includedir}/%{name}/*.hh
%{_libdir}/libqpdf.so
%{_libdir}/pkgconfig/libqpdf.pc
%{_libdir}/cmake/qpdf
