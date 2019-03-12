# [![Build Status](https://travis-ci.org/SUSE/cf-obs-stacks.svg?branch=master)](https://travis-ci.org/SUSE/cf-obs-stacks) cf-obs-stacks

Here you can find all specs used to build our stacks and metapackages in OBS.

This repository is pulled directly from OBS, and the changes applied on master are synchronized from OBS and relevant packages are built automatically.

- `metapackages/*` - contains all the build-requires metapackages for each stack we support ([SLE12](https://build.opensuse.org/package/show/Cloud:Platform:Stack-SLE:packages/aaa_stack_build_requires), [SLE15](https://build.opensuse.org/package/show/Cloud:Platform:Stack:packages/aaa_stack_build_requires)
- `images/kiwi/*` - contains all the kiwi specfiles used to generate the stack images ([SLE12](https://build.opensuse.org/package/show/Cloud:Platform:Stack-SLE:rootfs/cf-sle12), [SLE15](https://build.opensuse.org/package/show/Cloud:Platform:Stack:rootfs/sle15)

## New packages

To create new packages that are automatically triggered from the ci, first create the package and add a `_service` file of this form:

```
<services>
  <service name="obs_scm">
    <param name="extract">images/kiwi/sle12/cf-sle12.kiwi</param>
    <param name="extract">images/kiwi/sle12/config.sh</param>
    <param name="url">git://github.com/SUSE/cf-obs-stacks.git</param>
    <param name="revision">master</param>
    <param name="scm">git</param>
    <param name="changesgenerate">enable</param>
    <param name="changesauthor">mail@somewhere.com</param>
  </service>
</services>
```

Push the specfiles to the git repository and then create a new token with osc `osc token --create <PROJECT> <PACKAGE>`.

The token is consumed by the `OBS_TOKENS` env variable (which for automatically syncronization needs to be specified inside the Travis settings).

To test the triggers locally, you can run ```trigger_obs_services.sh```:

	OBS_TOKENS="token1 token2" ./ci/trigger_obs_services.sh

## Automatic Synchronization

Seems [automatic synchronization from OBS is not possible anymore](https://openbuildservice.org/2013/11/22/source-update-via_token/) since Github Services were deprecated.

To overcome this limitation, a Travis job is fired on each push of the ```master``` branch. In the travis settings there is set a ```OBS_TOKENS``` env var which contains the tokens relative to the project/packages that needs to be triggered.

The travis job calls an OBS servicerun on the packages refered by the tokens.
When a OBS servicerun is triggered, OBS will pull the sources declared in the ```_service``` file and trigger a build if needed.

## Testing changes

Create a branch or a fork and do your changes there.

To test the changes, branch also the relative package in OBS and edit the ```_service``` file to point to your testing repository where the specfile are (edit ```<param name="url">git://github.com/SUSE/cf-obs-stacks.git</param>``` and ```<param name="revision">master</param>``` accordingly).
