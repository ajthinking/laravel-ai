import sys
import os
from os import walk
from glob import glob

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../"))
import coach.speak as s #pylint: disable=E0401
from Print import Print #pylint: disable=E0401
import Paths #pylint: disable=E0401

print = Print()

def regex_for(type):
    expressions = {
        "table": r"(?:Schema::create\(')(.*)(?:')",
        "column_data_type": r"(?:\$table->)([a-z_A-Z]*)",
        "column_name": r"(?:\$table->.*')(.*)(?:')",
    }

    return expressions[type]

def files():
    files = [y for x in os.walk(Paths.raw) for y in glob(os.path.join(x[0], '*.php'))]
    return list(map(lambda r: os.path.realpath(r), files))



def table_name(file):
    return "users"

def column_definitions(file):
    return [
			r"$table->increments('id');",
			r"$table->string('username', 190)->unique();",
			r"$table->string('password', 60);",
			r"$table->string('name');",
			r"$table->string('remember_token', 100)->nullable();",
			r"$table->timestamps();",
    ]

def transform(files):
    rows = []
    for file_path in files:
        parts = file_path.split('/')
        file = parts[-1]
        repo = parts[-4]
        user = parts[-5]
        for definition in column_definitions(file_path):
            rows.append((
                    user,
                    repo,
                    file,
                    table_name(definition),
                    "string",
                    "some_column_name"
            ))
    return rows

for row in transform(files()):
    print(row)

# Disqualifyers (
#   multiple tables,
#   no create table statement)
#   no migrations
