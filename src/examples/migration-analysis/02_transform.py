import sys
import os
from os import walk
from glob import glob

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../"))
import coach.speak as s #pylint: disable=E0401
from Print import Print #pylint: disable=E0401
import Paths #pylint: disable=E0401

print = Print()

def files():
    files = [y for x in os.walk(Paths.raw) for y in glob(os.path.join(x[0], '*.php'))]
    return list(map(lambda r: os.path.realpath(r), files))

def name_and_type_pairs(files):
    for file in files:
        pass
        #print("string", files)

# EXAMPLE row (user, repo, file, column_type, column_name)