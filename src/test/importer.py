"""
========================
My module importer
========================

Usage:
    1. This file deploy main script directory.
    2. Write add `from importer import import_my_module` your script.
    3. And wirte path you want read module 
      + `import_my_module('../YourModule')`
    4. Running your script. Maybe, Your module load after runnning your script.
"""

from sys import path
import os

def import_my_module(modulepath):
    """Add PYTHONPATH modulepath
    Return absolute path
    """
    p =  os.path.dirname(modulepath) if os.path.isabs(modulepath) \
             else os.path.dirname(os.path.realpath(modulepath))

    path.append(p)
    return p

if __name__ == '__main__':
    print(import_my_module(input('Input want read module name: ')))
