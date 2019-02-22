#
# spec file for package aaa_stack_build_requires_meta_package
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           aaa_stack_build_requires
Version:        1.0
Release:        0
Summary:        Meta package to require all stack packages during build time
License:        GPL-3.0-or-later
Group:          Cloud/Platform/scf
Url:            https://www.suse.com/
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
Requires:       coreutils
Requires:       iputils
Requires:       suse-build-key
Requires:       ncurses
Requires:       ncurses-utils
Requires:       tack
Requires:       autoconf
Requires:       bind
Requires:       bison
Requires:       make
Requires:       gcc
Requires:       glibc-devel
Requires:       gcc-c++
Requires:       bzr
Requires:       ca-certificates
Requires:       cmake
Requires:       cron
Requires:       curl
Requires:       dmidecode
Requires:       bind-utils
Requires:       fakeroot
Requires:       flex
Requires:       fontconfig
Requires:       gdb
Requires:       git-core
Requires:       ImageMagick
Requires:       iproute2
Requires:       arping2
Requires:       jq
Requires:       less
Requires:       libaio1
Requires:       libatk-1_0-0
Requires:       libatm1
Requires:       libavahi-client3
Requires:       libavahi-common3
Requires:       libbz2-devel
Requires:       libcairo2
Requires:       libcap-progs
Requires:       perl-Class-Accessor
Requires:       libcurl4
Requires:       libcurl-devel
Requires:       libdatrie1
Requires:       libdirectfb-1_7-1
Requires:       libdjvulibre-devel
Requires:       libdjvulibre21
Requires:       libdrm_intel1
Requires:       libdrm_nouveau2
Requires:       libdrm_radeon1
Requires:       fuse-devel
Requires:       libfuse2
Requires:       gmp-devel
Requires:       gpm
Requires:       graphviz-devel
Requires:       libgtk-3-0
Requires:       gtk3
Requires:       libicu-devel
Requires:       ilmbase-devel
Requires:       libIlmThread-2_1-11
Requires:       libHalf11
Requires:       libIex-2_1-11
Requires:       libImath-2_1-11
Requires:       perl-IO-String
Requires:       lapack-devel
Requires:       ncurses-devel
Requires:       libnl3-200
Requires:       openblas-devel
Requires:       openexr-devel
Requires:       libpango-1_0-0
Requires:       libpixman-1-0
Requires:       libipq-devel
Requires:       readline-devel
Requires:       cyrus-sasl-devel
Requires:       libsigc++2
Requires:       sqlite2-devel
Requires:       sqlite3-devel
Requires:       perl-Sub-Name
Requires:       sysfsutils
Requires:       libthai-data
Requires:       libthai
Requires:       xapian-core
Requires:       libxcb-render-util0
Requires:       libxcb-render0
Requires:       libXcomposite1
Requires:       libXcursor1
Requires:       libXdamage1
Requires:       libXfixes3
Requires:       libXft2
Requires:       libXi6
Requires:       libXinerama1
Requires:       libxml2
Requires:       libxml2-devel
Requires:       libXrandr2
Requires:       libXrender1
Requires:       libxslt-devel
Requires:       libxslt
Requires:       libXt-devel
Requires:       libXt6
Requires:       libyaml-devel
Requires:       lsof
Requires:       xz
Requires:       mercurial
Requires:       openssh
Requires:       openssl
Requires:       psmisc
Requires:       python
Requires:       quota
Requires:       rsync
Requires:       shared-mime-info
Requires:       sshfs
Requires:       strace
Requires:       subversion
Requires:       sysstat
Requires:       tcpdump
Requires:       traceroute
Requires:       dejavu-fonts
Requires:       unzip
Requires:       uuid-devel
Requires:       wget
Requires:       zip
Requires:       ruby2.3
Requires:       ruby2.3-rubygem-gem2rpm
Requires:       ruby2.3-rubygem-bundler
Requires:       sudo
Requires:       aws-cli
Requires:       libopenssl-devel
Requires:       openldap2-devel
Requires:       pcre-devel
Requires:       aspell-devel
Requires:       libc-client2007e_suse
Requires:       libexpat-devel
Requires:       gdbm-devel
Requires:       gmp-devel
Requires:       openldap2-devel
Requires:       libldb-devel
Requires:       libmcrypt-devel
Requires:       libpng12-devel
Requires:       libpng12-compat-devel
Requires:       libpspell15
Requires:       readline-devel
Requires:       sqlite3-devel
Requires:       libopenssl-devel
Requires:       libxml2-devel
Requires:       libzip-devel
Requires:       automake
Requires:       freetype2-devel
Requires:       libxslt-devel
Requires:       libGeoIP-devel
Requires:       ImageMagick-devel
Requires:       cyrus-sasl-devel
Requires:       imap-devel
Requires:       krb5-devel
Requires:       net-snmp-devel
Requires:       libuv-devel
Requires:       freetds-devel
Requires:       postgresql-devel
Requires:       libmemcached11
Requires:       util-linux-systemd
Requires:       netcat-openbsd
Requires:       which
Requires:       libmysqlclient-devel
Requires:       libgearman-devel
Requires:       libmemcachedutil2

# Required by libgdiplus:
# needs updated version of glib2, while 
# the other deps are in the cflinux stack
Requires:       glib2-devel
Requires:       libjbig-devel
Requires:       libjbig2
Requires:       libexif12
Requires:       libexif-devel
Requires:       cairo-devel
Requires:       libtiff-devel

%description

%prep

%build

%install

%files

%changelog

