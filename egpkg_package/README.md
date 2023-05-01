# egpkg

A minimal working example of a Python package which 
uses C++ code via Cython. There are two functions, one 
to multiply a function by 2, and one to multiple a function by 3.

## Functions

  - `timesTwo`: pure Python implementation
  - `timesThree`: C++ implementation, wrapped with Cython

## Folders and files

  - `egpkg/src/`: contains `func.py` which contains `timesTwo` function.
  - `egpkg/cppsrc/`: contains `cppfunc.h` and `cppfunc.cpp`, which contains 
     the `cpp_timesThree` function, and `cppmethods.pyx` which wraps the 
     C++ code into the Python functions `timesThree`.

## Details

Uses Cython and `setuptools` to create package.
