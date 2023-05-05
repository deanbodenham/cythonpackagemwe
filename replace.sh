# suggestion: first run cleanup
./cleanup.sh

# old is current name; new is future name
oldname="egpkg"
newname="egpkg"

# package folder contains the package, e.g. egpkg
oldpackagefolder="${oldname}_package"
newpackagefolder="${newname}_package"

# code folder contains the code, e.g. egpkg_folder/egpkg
oldcodefolder="${oldpackagefolder}/${oldname}"
newcodefolder="${oldpackagefolder}/${newname}"

# test file is Python file
oldtestfile="./${oldpackagefolder}/tests/test_${oldname}.py"
newtestfile="./${oldpackagefolder}/tests/test_${newname}.py"


## First change names of files and folders
# moving test file first
mv $oldtestfile $newtestfile

# then move code folder
mv $oldcodefolder $newcodefolder

# finally move package folder
mv $oldpackagefolder $newpackagefolder


## Finally change text inside files
# NOTE: this is for macOS; on Linux may need to be modified, check 'man sed'.
grep -rl "${oldname}" . | xargs sed -i '' -e "s/$oldname/$newname/g"
