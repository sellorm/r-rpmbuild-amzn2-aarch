Name:		R-3.5.2
Version:	1
Release:	9%{?dist}
Summary:	sellorm.com build or R 3.5.2
Group:		Applications/Engineering

License:	GPLv2+
Vendor:		r-project.org
Packager:	sellorm.com

Requires: gcc-c++, gcc-gfortran, tex(latex), texinfo-tex
Requires: bzip2-devel, libX11-devel, pcre-devel, zlib-devel
Requires: tcl-devel, tk-devel, pkgconfig, xz-devel
Requires: libicu-devel, java
Requires: sed, gawk, tex(latex), less, make, unzip
Requires: openssl-devel, libxml2-devel, libcurl-devel

Source0: https://cloud.r-project.org/src/base/R-3/R-3.5.2.tar.gz

BuildRequires: readline-devel, libX11-devel, libXt-devel
BuildRequires: bzip2-devel, xz-devel, pcre-devel
BuildRequires: libcurl-devel, java-1.8.0-openjdk
BuildRequires: gcc-gfortran
BuildRequires: gcc-c++, tex(latex), texinfo-tex
BuildRequires: libpng-devel, libjpeg-devel, readline-devel
BuildRequires: tcl-devel, tk-devel, ncurses-devel
BuildRequires: pcre-devel, zlib-devel, less
BuildRequires: valgrind-devel, lapack-devel, blas-devel
BuildRequires: libSM-devel, libX11-devel, libICE-devel, libXt-devel
BuildRequires: bzip2-devel, libXmu-devel, cairo-devel, libtiff-devel
BuildRequires: gcc-objc, pango-devel, xz-devel
BuildRequires: autoconf, automake, libtool, java-1.8.0-openjdk-devel

%description
Standard open source R pre-compliled by sellorm.com

%prep
tar -zxvf %{_sourcedir}/R-3.5.2.tar.gz -C %{_builddir}/

%build
cd %{_builddir}/R-3.5.2
./configure \
    --prefix=/opt/R/3.5.2 \
    --with-system-valgrind-headers \
    --with-tcltk \
    --enable-BLAS-shlib \
    --enable-R-shlib \
    --enable-prebuilt-html \
    --enable-memory-profiling \
    --with-x \
    --with-lapack \
    --with-blas
make

%install
cd %{_builddir}/R-3.5.2/
#mkdir -p ${RPM_BUILD_ROOT}/opt/R/3.5.2/
# not doing what I want it to right now
make DESTDIR=${RPM_BUILD_ROOT} install
# cp -r %{_builddir}/R-3.5.2/bin ${RPM_BUILD_ROOT}/opt/R/3.5.2/
# cp -r %{_builddir}/R-3.5.2/modules ${RPM_BUILD_ROOT}/opt/R/3.5.2/
# cp -r %{_builddir}/R-3.5.2/lib ${RPM_BUILD_ROOT}/opt/R/3.5.2/
# cp -r %{_builddir}/R-3.5.2/library ${RPM_BUILD_ROOT}/opt/R/3.5.2/
# cp -r %{_builddir}/R-3.5.2/etc ${RPM_BUILD_ROOT}/opt/R/3.5.2/

%clean
echo "Not cleaning up in this case."

%post
update-alternatives --install /usr/local/bin/R R /opt/R/3.5.2/bin/R 2
update-alternatives --install /usr/local/bin/Rscript Rscript /opt/R/3.5.2/bin/Rscript 2

%files
%defattr(-,root,root,-)
  /opt/R/3.5.2/bin/R
  /opt/R/3.5.2/bin/Rscript
  /opt/R/3.5.2/lib/R/COPYING
  /opt/R/3.5.2/lib/R/SVN-REVISION
 
%dir 
  /opt/R/3.5.2/lib/R/doc
  /opt/R/3.5.2/lib/R/etc
  /opt/R/3.5.2/lib/R/share
  /opt/R/3.5.2/lib/R/bin
  /opt/R/3.5.2/lib/R/include
  /opt/R/3.5.2/lib/R/lib
  /opt/R/3.5.2/lib/R/modules
  /opt/R/3.5.2/lib/R/library
  /opt/R/3.5.2/lib/pkgconfig
  /opt/R/3.5.2/share
  /opt/R/3.5.2/bin
