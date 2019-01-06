# R RPM Build for Amazon Linux 2 on ARM

There's **lots** to fix here and this is still very **experimental**.

Most of it is based on the [Fedora R spec file](https://src.fedoraproject.org/rpms/R/blob/master/f/R.spec), the [RStudio article on building R from source](https://support.rstudio.com/hc/en-us/articles/218004217-Building-R-from-source) as well as my own experiences and observations.

For a pre-built version see [builds.sellorm.com](https://builds.sellorm.com).

## Get R src

Need to get the source in the sources directory really but this is the way I was doing it before.

```
mkdir r-src && cd r-src
wget https://cloud.r-project.org/src/base/R-3/R-3.5.2.tar.gz
tar zxvf R-3.5.2.tar.gz
cd R-3.5.2/
```

## Install all the deps

This can be handled by using `yum-builddeps` on the spec file.

```
yum groupinstall -y "Development Tools"
sudo yum groupinstall -y "Development Tools"
sudo yum install readline-devel
sudo yum install -y libX11-devel
sudo yum install -y libXt-devel
sudo yum install -y bzip2-devel
sudo yum install -y xz-devel
sudo yum install -y pcre-devel
sudo yum install -y libcurl-devel
sudo yum install -y java-1.8.0-openjdk
```

## build R

Not really needed anymore as R is built as part of the R creation process.

```
./configure --prefix /opt/R/3.5.2  --enable-R-shlib --with-blas --with-lapack
make
```

## Prep the rpmbuild

Don't need most of this anymore either - just the rpmbuild bit - but I need to go through it all again and clean it up.

```
mkdir ~/rpmbuild
cd ~/rpmbuild
mkdir SPECS
cd SPECS/
vi R-3.5.2.spec
mkdir -p ../BUILDROOT/R-3.5.2-1-1.amzn2.aarch64/opt/R/3.5.2
cp -r ~/r-src/R-3.5.2/bin ../BUILDROOT/R-3.5.2-1-1.amzn2.aarch64/opt/R/3.5.2/
cp -r ~/r-src/R-3.5.2/lib ../BUILDROOT/R-3.5.2-1-1.amzn2.aarch64/opt/R/3.5.2/
cp -r ~/r-src/R-3.5.2/library ../BUILDROOT/R-3.5.2-1-1.amzn2.aarch64/opt/R/3.5.2/
cp -r ~/r-src/R-3.5.2/modules ../BUILDROOT/R-3.5.2-1-1.amzn2.aarch64/opt/R/3.5.2/
cp -r ~/r-src/R-3.5.2/etc ../BUILDROOT/R-3.5.2-1-1.amzn2.aarch64/opt/R/3.5.2/
sudo hostname builds.sellorm.com
rpmbuild -vv -bb R-3.5.2.spec 
ls ../RPMS/
rpm -qip ../RPMS/aarch64/R-3.5.2-1-1.amzn2.aarch64.rpm 
sudo yum install -y ../RPMS/aarch64/R-3.5.2-1-1.amzn2.aarch64.rpm
mv /home/ec2-user/rpmbuild/BUILDROOT/R-3.5.2-1-1.amzn2.aarch64 /home/ec2-user/rpmbuild/BUILDROOT/R-3.5.2-1-2.amzn2.aarch64
R
```

