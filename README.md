# cf-obs-stacks

Here you can find all specs used to build our stacks and metapackages in OBS.

This repository is pulled directly from OBS, and the changes applied on master are syncronized from OBS and relevant packages are built automatically.

- `metapackages/*` - contains all the build-requires metapackages for each stack we support ([SLE12](https://build.opensuse.org/package/show/Cloud:Platform:Stack-SLE:packages/aaa_stack_build_requires), [SLE15](https://build.opensuse.org/package/show/Cloud:Platform:Stack:packages/aaa_stack_build_requires), [opensuse42](https://build.opensuse.org/package/show/Cloud:Platform:Stack-openSUSE:packages/aaa_stack_build_requires))
- `images/kiwi/*` - contains all the kiwi specfiles used to generate the stack images ([SLE12](https://build.opensuse.org/package/show/Cloud:Platform:Stack-SLE:rootfs/cf-sle12), [SLE15](https://build.opensuse.org/package/show/Cloud:Platform:Stack:rootfs/sle15), [opensuse42](https://build.opensuse.org/package/show/Cloud:Platform:Stack-openSUSE:rootfs/cf-opensuse42))


