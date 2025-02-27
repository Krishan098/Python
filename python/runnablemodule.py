from selectionsort import selection_sort
selection_sort([9,2,1,4])
# if __name__=='__main__' : check=>only runs the script if __name__ of script is same as the main file.
#the function calls in that file(selectionsort) are not performed here.


'''
    PYTHON PACKAGE:
            directory that contains zero or more python modules.
            can contain sub-packages.
            Each package contains a special file named __init__.py
'''
'''
    __init__.py: always executed when the package is imported.
    Use subpackages to group related modules together.
'''
'''
    For a runnable package ,__main__.py  is required in the root folder.
    
'''
''''
    A module is always a single file, while a package can contain many modules.
    A module bundles Python functions, classes, constants, and anything else you want to make reusable. A package, in turn, bundles modules.
    Modules can exist independently and don’t need to be part of a package, while a package needs modules to be useful.
    Together, packages and modules form a powerful way of organizing our code.
'''