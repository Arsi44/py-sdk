
# Change Log
All notable changes to this project will be documented in this file.

## v0.0.14.a1 - 2022-08-13

Note that you now install the [`nibiru` package](https://pypi.org/project/nibiru/) with `pip install nibiru`.

### Improvements

* chore: Update package version to v0.0.14.a1 by @NibiruHeisenberg in https://github.com/NibiruChain/nibiru-py/pull/59
* [#46](https://github.com/NibiruChain/nibiru-py/pull/46) - Bugfix in query perp trader position
* test,ci,feat: (1) Use poetry for pkg management. (2) Improve CI. (3) Re-gen protos for v0.12.1-alpha of nibiru by @Unique-Divine in https://github.com/NibiruChain/nibiru-py/pull/53
* docs(README): Documented entire development setup. Fixed badges. Added installation instructions for pyenv, poetry, pip by @Unique-Divine in https://github.com/NibiruChain/nibiru-py/pull/55

### Fixes

* refactor: fix protogen script by @NibiruHeisenberg in https://github.com/NibiruChain/nibiru-py/pull/49
* Removed manual position deserialization by @onikonychev in https://github.com/NibiruChain/nibiru-py/pull/47
* Revert "Removed manual position deserialization" by @matthiasmatt in https://github.com/NibiruChain/nibiru-py/pull/48
* fix: Fix protogen script, upgraded proto  by @NibiruHeisenberg in https://github.com/NibiruChain/nibiru-py/pull/44
* Bugfix in query perp trader position by @onikonychev in https://github.com/NibiruChain/nibiru-py/pull/46

## v0.0.14 - 2022-08-11

- Upgraded proto to fit nibiru chain v0.12.2
- Simplified Makefile
- Fixed Protogen script

## v0.0.1 through v0.0.13

* Change the link of the conf.py file by @matthiasmatt in https://github.com/NibiruChain/nibiru-py/pull/43
* Add readthedoc configuration for autodoc by @matthiasmatt in https://github.com/NibiruChain/nibiru-py/pull/42
* Mat/more doc by @matthiasmatt in https://github.com/NibiruChain/nibiru-py/pull/41
* Add documentation and improve the output of the dex queries by @matthiasmatt in https://github.com/NibiruChain/nibiru-py/pull/40
* ci,tests: Verify the SDK works with tests and set up GHA workflow to build and run from scratch  by @Unique-Divine in https://github.com/NibiruChain/nibiru-py/pull/38
* Mat/autodoc by @matthiasmatt in https://github.com/NibiruChain/nibiru-py/pull/37
* Qol improvements by @matthiasmatt in https://github.com/NibiruChain/nibiru-py/pull/35
* Updated references to old repo name in https://github.com/NibiruChain/nibiru-py/pull/32
* Fix some issues with the rst files by @matthiasmatt in https://github.com/NibiruChain/nibiru-py/pull/34
* Add documentation on the nibiru perp by @matthiasmatt in https://github.com/NibiruChain/nibiru-py/pull/33
* Cleanup in https://github.com/NibiruChain/nibiru-py/pull/26
* Bump version to 0.0.11 to deploy Pypi by @onikonychev in https://github.com/NibiruChain/nibiru-py/pull/31
* feat: Add documentation by @matthiasmatt in https://github.com/NibiruChain/nibiru-py/pull/29
* Changed network default to secure in https://github.com/NibiruChain/nibiru-py/pull/30
* Removed auto cosmInt transformation from response in https://github.com/NibiruChain/nibiru-py/pull/28
* Added testnet and removed cookie code in https://github.com/NibiruChain/nibiru-py/pull/27
* Fixed paths in run script and added some info to README in https://github.com/NibiruChain/nibiru-py/pull/25
* Added pricefeed module in https://github.com/NibiruChain/nibiru-py/pull/23
* Added testnet network in https://github.com/NibiruChain/nibiru-py/pull/22
* Fixed float to int cast in https://github.com/NibiruChain/nibiru-py/pull/21
* Fixed sdk types and examples in https://github.com/NibiruChain/nibiru-py/pull/20
* Bumped version to release in https://github.com/NibiruChain/nibiru-py/pull/19
* Fixed error in https://github.com/NibiruChain/nibiru-py/pull/18
* Updated protos and fixed property names to snake_case in https://github.com/NibiruChain/nibiru-py/pull/17
* Fixed network assignment in https://github.com/NibiruChain/nibiru-py/pull/16
* Added vpool and removed async/await in https://github.com/NibiruChain/nibiru-py/pull/15
* Github workflow: do release on master merge by @onikonychev in https://github.com/NibiruChain/nibiru-py/pull/11
* Disabled cron job to sync timeout height in https://github.com/NibiruChain/nibiru-py/pull/10
* Changed tx default to async and leave sequence count in case of tx err in https://github.com/NibiruChain/nibiru-py/pull/9
* Added tx type option to sdk wrapper in https://github.com/NibiruChain/nibiru-py/pull/8
* Rethrow sim err and allow multiple msgs in tx in https://github.com/NibiruChain/nibiru-py/pull/7
* Refactored to use new sdk wrapper and cleanup in https://github.com/NibiruChain/nibiru-py/pull/6
* Added wrapper to simplify usage in https://github.com/NibiruChain/nibiru-py/pull/5
* Added pyi (type info) to generated protos + minor cleanup in https://github.com/NibiruChain/nibiru-py/pull/3