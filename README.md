# [![Build Status](https://travis-ci.org/SUSE/cf-obs-stacks.svg?branch=master)](https://travis-ci.org/SUSE/cf-obs-stacks) cf-obs-stacks

Here you can find all specs used to build our stacks and metapackages in OBS.

This repository is pulled directly from OBS, and the changes applied on master are syncronized from OBS and relevant packages are built automatically.

- `metapackages/*` - contains all the build-requires metapackages for each stack we support ([SLE12](https://build.opensuse.org/package/show/Cloud:Platform:Stack-SLE:packages/aaa_stack_build_requires), [SLE15](https://build.opensuse.org/package/show/Cloud:Platform:Stack:packages/aaa_stack_build_requires), [opensuse42](https://build.opensuse.org/package/show/Cloud:Platform:Stack-openSUSE:packages/aaa_stack_build_requires))
- `images/kiwi/*` - contains all the kiwi specfiles used to generate the stack images ([SLE12](https://build.opensuse.org/package/show/Cloud:Platform:Stack-SLE:rootfs/cf-sle12), [SLE15](https://build.opensuse.org/package/show/Cloud:Platform:Stack:rootfs/sle15), [opensuse42](https://build.opensuse.org/package/show/Cloud:Platform:Stack-openSUSE:rootfs/cf-opensuse42))

## New packages

To create new packages that are automatically triggered from the ci, first create the package and the `_service` file, then
create a new token with osc `osc token --create <PROJECT> <PACKAGE>` and specify it in the `OBS_TOKENS` env variable (also inside the Travis settings).

To test the trigger locally, you can:

	OBS_TOKENS="token1 token2" ./ci/trigger_obs_services.sh

