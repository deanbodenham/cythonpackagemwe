# Minimal working example for a Python package using C++ code

It can be somewhat intricate to create a Python package for 
distribution for others to use, especially when the Python package
uses C++ code. This repository attempts to provide a minimal working 
example.

## TL;DR

If using Linux or macOS, run the following scripts in sequence:

  - `build_dist.sh`
  - `install.sh`

and then run the script `script.py` using `python3 script.py`.

If using Windows, look at the commands in the scripts above.


## Details


The folder `egpkg_package` contains all the files and folders necessary to 
build the package.


### Requires

The following Python modules need to be installed:

  - `Cython`
  - `numpy`
  - `wheel`
  - `setuptools`

as well as a C++ compiler.

If you want to run the tests, `pytest` will also need to be installed.


## Building the package

Alternatively, one can navigate to the `egpkg_package` folder
and run the command:

```
python3 -m build
```

This will create a folder `dist` in `egpkg_package` which contains
`.whl` file and a `.tar.gz` file which can be used to distribute the package
for others to use.

(By the way, this is the main command in `build_dist.sh`)

**Note:** It seems that it is necessary to be connected to the internet, 
because Python seems to create a virtual environment and install `numpy` and
other packages in this environment before compiling the package.



## Details

This package contains two functions:

  - `timesTwo`: pure Python function, multiplies an argument by 2.
  - `timesThree`: C++ implementation, multiplies an argument by 3 (double).


### Scripts

  - `build_dist.sh`: builds the files used to install and share the package.
  - `buildinplace.sh`: builds the package, which can be used locally.
  - `cleanup.sh`: deletes files and folders to return the the `egpkg_package`
  directory to the state it was in before `build_dist.sh`.
  - `install.sh`: after `build_dist.sh` is run, will install `egpkg` using
  the `.whl` file.
  - `install_from_targz.sh`: after `build_dist.sh` is run, will install `egpkg` using
  the `.tar.gz` file.
  - `runtests.sh`: runs simple tests of `timesTwo` and `timesThree` using `pytest`.
  This script essentially calls `buildinplace.sh`, which does not install the package.
  - `replace.sh`: allows one to easily change from 'egpkg' to 'mypackage' 
  (or any other string); useful when using this package as a starting point.
  - `script.py`: A simple script which can be run, after `egpkg` is installed, to
  check that the functions `timesTwo` and `timesThree` work.
  - `uninstall.sh`: uninstalls the package, if it has been built and installed.
  - `show_uninstalled.sh`: shows the package has been uninstalled.



### Folders and files

  - `egpkg/src/`: contains `func.py` which contains `timesTwo` function.
  - `egpkg/cppsrc/`: contains `cppfunc.h` and `cppfunc.cpp`, which contains 
     the `cpp_timesThree` function, and `cppmethods.pyx` which wraps the 
     C++ code into the Python functions `timesThree`.



## Creating your own Python packages with Cython

This package can be used as a starting point.

  - In `setup.py`, change all instances of `egpkg` to whatever package name you want.
  - Change the subdirectory `egpkg_package/egpkg/` to the name of the package you wish.
  - Change the directory `egpkg_package` to another name (any you wish).
  - Include any C++ code in the folder `cppsrc`; follow the example of `cppmethods.pyx`.

The hardest part was to get the `.whl` file to be successfully built, and for the 
package to be installed from the `.whl` file so that the (C++ function) `timesThree`
could be called.


## Acknowledgements

Built with some help from the official documents, some help from ChatGPT, 
and some trial and error. 


## Disclaimer

There are also several other GitHub repos out there which aim to provide a MWE;
while I am sure they worked when originally created, all the ones tried now
(May 2023) seem to not (completely) work. 
I expect that eventually this code will stop working. Hopefully by that
stage the official Python packaging website will provide up-to-date
MWEs.

### Software/Hardware

This package was built using Python 3.11 on a (silicon-processor) Apple Macbook Air.
