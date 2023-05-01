# move into folder
cd egpkg_package/

# build package locally and test
python3 setup.py build_ext --inplace
python3 -m pytest

# move back into folder
cd ..
