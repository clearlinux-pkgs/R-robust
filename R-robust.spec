#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-robust
Version  : 0.6.1
Release  : 33
URL      : https://cran.r-project.org/src/contrib/robust_0.6-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/robust_0.6-1.tar.gz
Summary  : Port of the S+ "Robust Library"
Group    : Development/Tools
License  : GPL-2.0
Requires: R-robust-lib = %{version}-%{release}
Requires: R-fit.models
Requires: R-robustbase
Requires: R-rrcov
BuildRequires : R-fit.models
BuildRequires : R-robustbase
BuildRequires : R-rrcov
BuildRequires : buildreq-R

%description
2000s, notably for robust regression and robust multivariate analysis.

%package lib
Summary: lib components for the R-robust package.
Group: Libraries

%description lib
lib components for the R-robust package.


%prep
%setup -q -c -n robust
cd %{_builddir}/robust

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637113372

%install
export SOURCE_DATE_EPOCH=1637113372
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library robust
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library robust
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library robust
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc robust || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/robust/COPYRIGHTS
/usr/lib64/R/library/robust/DESCRIPTION
/usr/lib64/R/library/robust/INDEX
/usr/lib64/R/library/robust/Meta/Rd.rds
/usr/lib64/R/library/robust/Meta/data.rds
/usr/lib64/R/library/robust/Meta/features.rds
/usr/lib64/R/library/robust/Meta/hsearch.rds
/usr/lib64/R/library/robust/Meta/links.rds
/usr/lib64/R/library/robust/Meta/nsInfo.rds
/usr/lib64/R/library/robust/Meta/package.rds
/usr/lib64/R/library/robust/NAMESPACE
/usr/lib64/R/library/robust/R/robust
/usr/lib64/R/library/robust/R/robust.rdb
/usr/lib64/R/library/robust/R/robust.rdx
/usr/lib64/R/library/robust/data/breslow.dat.txt.gz
/usr/lib64/R/library/robust/data/leuk.dat.txt.gz
/usr/lib64/R/library/robust/data/mallows.dat.txt.gz
/usr/lib64/R/library/robust/data/stack.dat.txt.gz
/usr/lib64/R/library/robust/data/woodmod.dat.txt.gz
/usr/lib64/R/library/robust/datasets/lawson.tab
/usr/lib64/R/library/robust/datasets/wagner.q
/usr/lib64/R/library/robust/help/AnIndex
/usr/lib64/R/library/robust/help/aliases.rds
/usr/lib64/R/library/robust/help/paths.rds
/usr/lib64/R/library/robust/help/robust.rdb
/usr/lib64/R/library/robust/help/robust.rdx
/usr/lib64/R/library/robust/html/00Index.html
/usr/lib64/R/library/robust/html/R.css
/usr/lib64/R/library/robust/tests/Examples/robust-Ex.Rout.save
/usr/lib64/R/library/robust/tests/Run-tests.R
/usr/lib64/R/library/robust/tests/weight-tst.R
/usr/lib64/R/library/robust/tests_S/asymmetric.t
/usr/lib64/R/library/robust/tests_S/covm.t
/usr/lib64/R/library/robust/tests_S/discrob.t
/usr/lib64/R/library/robust/tests_S/glmrob.t
/usr/lib64/R/library/robust/tests_S/lmrob.t
/usr/lib64/R/library/robust/tests_S/plots.aovrob.t
/usr/lib64/R/library/robust/tests_S/plots.covrob.t
/usr/lib64/R/library/robust/tests_S/plots.glmrob.t
/usr/lib64/R/library/robust/tests_S/plots.lmrob.t
/usr/lib64/R/library/robust/tests_S/plots.princomprob.t
/usr/lib64/R/library/robust/tests_S/plots.wblrob.t
/usr/lib64/R/library/robust/tests_S/princomprob.t

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/robust/libs/robust.so
/usr/lib64/R/library/robust/libs/robust.so.avx2
/usr/lib64/R/library/robust/libs/robust.so.avx512
