#
# spec file for package aaa_stack_build_requires
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Group:          Cloud/Platform/cap
Url:            https://www.suse.com/
Requires: ca-certificates
Requires: ca-certificates-mozilla
Requires: coreutils
Requires: suse-build-key
Requires: krb5
Requires: netcfg
Requires: kubic-locale-archive
Requires: tack
Requires: sudo

# Is part of cflinuxfs3 but separate package in SUSE distributions
Requires: which

# Is part of https://github.com/cloudfoundry/cflinuxfs3/blob/master/cflinuxfs3/cflinuxfs3_receipt but not of the definition so adding manually
Requires: libexpat-devel
Requires: libpng-devel
Requires: postgresql-devel
Requires: gcc-c++
Requires: libcairo2
Requires: tar
Requires: bzip2
Requires: mawk

# CF packages - https://github.com/cloudfoundry/cflinuxfs3/blob/master/packages/cflinuxfs3
Requires: autoconf
Requires: bison
Requires: bzr
Requires: ca-certificates
Requires: cmake
Requires: cron
Requires: curl
Requires: bind-utils
Requires: fakeroot
Requires: file
Requires: flex
Requires: gdb
Requires: git-core
Requires: gpg2
Requires: ghostscript-fonts
Requires: iproute2
Requires: arping2
Requires: ImageMagick
Requires: jq
Requires: krb5
Requires: libaio1
Requires: perl-Archive-Extract
Requires: libargon2-1
Requires: libatm1
Requires: libaudiofile1
Requires: libavcodec57
Requires: libblas3
Requires: libcurl-devel
Requires: libestr0
Requires: libffi-devel
Requires: libfl-devel
Requires: libfribidi0
Requires: libgcrypt-devel
Requires: gdk-pixbuf-devel
Requires: gmp-devel
Requires: libgnutls-devel
Requires: libgnutlsxx-devel
Requires: libgnutlsxx28
Requires: libgpg-error-devel
Requires: libicu-devel
Requires: libidn-devel
Requires: libjson-glib-1_0-0
Requires: krb5-devel
Requires: lapack-devel
Requires: openldap2-devel
Requires: libLLVM5
Requires: libmagic1
Requires: libMagick++-devel
Requires: libmariadb-devel
Requires: libmariadb-devel
Requires: perl-Module-Pluggable
Requires: ncurses-devel
Requires: liborc-0_4-0
Requires: libp11-devel
Requires: pam_cap
Requires: libpango-1_0-0
Requires: libpqxx-devel
Requires: libproxy1
Requires: readline-devel
Requires: cyrus-sasl-devel
Requires: cyrus-sasl-crammd5
Requires: cyrus-sasl-digestmd5
Requires: cyrus-sasl-plain
Requires: cyrus-sasl-ntlm
Requires: cyrus-sasl-gssapi
Requires: cyrus-sasl-gs2
Requires: cyrus-sasl-scram
Requires: libselinux-devel
Requires: sqlite3-devel
Requires: libopenssl-devel
Requires: sysfsutils
Requires: libtasn1-devel
Requires: perl-Term-UI
Requires: libustr-1_0-1
Requires: libxslt-devel
Requires: libyaml-devel
Requires: logrotate
Requires: lsof
Requires: xz
Requires: man
Requires: mercurial
Requires: net-tools
Requires: openssh
Requires: libopenssl1_0_0
Requires: psmisc
Requires: quota
Requires: rsync
Requires: ruby
Requires: sshfs
Requires: strace
Requires: subversion
Requires: sysstat
Requires: tcpdump
Requires: traceroute
Requires: dejavu-fonts
Requires: unzip
Requires: uuid-devel
Requires: wget
Requires: zip

%description

%prep

%build

%install

%post
%postun

%files

%changelog

