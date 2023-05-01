import os

import numpy as np

from os.path import join
from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# Define the extension
ext = Extension(
    'egpkg.cppsrc.cppmethods',
    sources=[
        os.path.join('egpkg', 'cppsrc', 'cppmethods.pyx'),
        os.path.join('egpkg', 'cppsrc', 'cppfunc.cpp')
    ],
    include_dirs=[],
    language='c++',
    extra_compile_args=["-std=c++11"]
)

# Use cythonize on the extension object.
setup(
    name='egpkg',
    version="0.0.1",
    install_requires=["scipy>=1", "numpy>=1"],
    author="Name Other",
    author_email="name@mail.com",
    description="Example Python package with C++ code",
    ext_modules=cythonize(ext),
    packages=find_packages(),
    package_data={
        "egpkg": ["cppsrc/*.pyx", "cppsrc/*.cpp", "cppsrc/*.h", "cppsrc/*.so", "cppsrc/*.pyd"]
    },
    include_package_data=True,
    zip_safe=False,
)

