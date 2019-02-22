#!/bin/bash
#================
# FILE          : config.sh
#----------------
# PROJECT       : OpenSuSE KIWI Image System
# COPYRIGHT     : (c) 2013 SUSE LLC
#               :
# AUTHOR        : Robert Schweikert <rjschwei@suse.com>
#               :
# BELONGS TO    : Operating System images
#               :
# DESCRIPTION   : configuration script for SUSE based
#               : operating systems
#               :
#               :
# STATUS        : BETA
#----------------
#======================================
# Functions...
#--------------------------------------
test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

set -e -x
# Prepare CF root filesystem
# bash configure-locale-timezone.sh
# bash install-packages.sh
# bash build/generate-all-locales.sh
# bash install-ruby.sh 2.3.3
# bash configure-firstboot.sh

set +e +x

# Configure core dump directory
mkdir -p /var/vcap/sys/cores
chmod ugo+rwx /var/vcap/sys/cores
# create the vcap for garden and warden
useradd -u 2000 -mU -s /bin/bash vcap
mkdir /home/vcap/app
chown vcap /home/vcap/app
ln -s /home/vcap/app /app

# configure Ruby to use version 2.3 instead of the default 2.1
rm /usr/bin/ruby
update-alternatives --force --install /usr/bin/ruby ruby /usr/bin/ruby.ruby2.3  10
update-alternatives --force --install /usr/bin/gem gem /usr/bin/gem.ruby2.3  10
update-alternatives --force --install /usr/bin/erb erb /usr/bin/erb.ruby2.3  10

# Fix the shebang line of installed gems to use '/usr/bin/env ruby' instead of the versioned ruby
echo "custom_shebang: /usr/bin/env ruby" >> /etc/gemrc

# Add our packages repo
rpm --import repo_key.asc
sudo zypper --non-interactive ar --no-check --type rpm-md https://download.opensuse.org/repositories/Cloud:/Platform:/Stack-openSUSE:/packages/openSUSE_Leap_42.3/ packages

#======================================
# Setup baseproduct link
#--------------------------------------
suseSetupProduct

#======================================
# SuSEconfig
#--------------------------------------
suseConfig

#======================================
# Import repositories' keys
#--------------------------------------
suseImportBuildKey

#======================================
# Umount kernel filesystems
#--------------------------------------
baseCleanMount

#======================================
# Disable recommends
#--------------------------------------
sed -i 's/.*installRecommends.*/installRecommends = no/g' /etc/zypp/zypper.conf

#======================================
# Remove locale files
#--------------------------------------
(cd /usr/share/locale && find -name '*.mo' | xargs rm)

exit 0
