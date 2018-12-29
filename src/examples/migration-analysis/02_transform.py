import sys
import os
from os import walk
from glob import glob
import numpy as np
import re
import json

from MigrationFile import MigrationFile

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../"))
from Print import Print #pylint: disable=E0401
import Paths #pylint: disable=E0401

print = Print()

def files():
    files = [y for x in os.walk(Paths.raw) for y in glob(os.path.join(x[0], '*/*/**/*.php'))]
    migration_files = list(map(lambda r: MigrationFile(os.path.realpath(r)), files)) 
    return list(filter(lambda mf: mf.qualifies(), migration_files))

def transform(migration_files):
    rows = []
    for migration_file in migration_files:
        for column_data_type, column_name in migration_file.column_definitions:
            rows.append((
                    migration_file.user,
                    migration_file.repo,
                    migration_file.name,
                    migration_file.table,
                    column_data_type,
                    column_name
            ))
    return rows

rows = transform(files())

#sample
with open(os.path.join(Paths.processed,'migration-analysis-data-sample.json'), 'w') as outfile:
    json.dump(rows[:10], outfile, indent=4)
#full
with open(os.path.join(Paths.processed,'migration-analysis-data.json'), 'w') as outfile:
    json.dump(rows, outfile)    
