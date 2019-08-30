#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-plexus-languages
Version  : 0.9.2
Release  : 3
URL      : https://github.com/codehaus-plexus/plexus-languages/archive/plexus-languages-0.9.2.tar.gz
Source0  : https://github.com/codehaus-plexus/plexus-languages/archive/plexus-languages-0.9.2.tar.gz
Source1  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-java/0.9.10/plexus-java-0.9.10.jar
Source2  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-java/0.9.10/plexus-java-0.9.10.pom
Source3  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-java/0.9.2/plexus-java-0.9.2.jar
Source4  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-java/0.9.2/plexus-java-0.9.2.pom
Source5  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-java/0.9.3/plexus-java-0.9.3.jar
Source6  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-java/0.9.3/plexus-java-0.9.3.pom
Source7  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-java/0.9.8/plexus-java-0.9.8.jar
Source8  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-java/0.9.8/plexus-java-0.9.8.pom
Source9  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-languages/0.9.10/plexus-languages-0.9.10.pom
Source10  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-languages/0.9.2/plexus-languages-0.9.2.pom
Source11  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-languages/0.9.3/plexus-languages-0.9.3.pom
Source12  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-languages/0.9.8/plexus-languages-0.9.8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-plexus-languages-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-plexus-languages package.
Group: Data

%description data
data components for the mvn-plexus-languages package.


%prep
%setup -q -n plexus-languages-plexus-languages-0.9.2

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.10/plexus-java-0.9.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.10
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.10/plexus-java-0.9.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.2/plexus-java-0.9.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.2/plexus-java-0.9.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.3
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.3/plexus-java-0.9.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.3
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.3/plexus-java-0.9.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.8
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.8/plexus-java-0.9.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.8
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.8/plexus-java-0.9.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.10
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.10/plexus-languages-0.9.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.2
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.2/plexus-languages-0.9.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.3
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.3/plexus-languages-0.9.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.8
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.8/plexus-languages-0.9.8.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.10/plexus-java-0.9.10.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.10/plexus-java-0.9.10.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.2/plexus-java-0.9.2.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.2/plexus-java-0.9.2.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.3/plexus-java-0.9.3.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.3/plexus-java-0.9.3.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.8/plexus-java-0.9.8.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-java/0.9.8/plexus-java-0.9.8.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.10/plexus-languages-0.9.10.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.2/plexus-languages-0.9.2.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.3/plexus-languages-0.9.3.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-languages/0.9.8/plexus-languages-0.9.8.pom
