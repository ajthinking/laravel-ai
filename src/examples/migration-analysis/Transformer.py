import os
import sys
import base64
import time
import datetime
import re
import inspect
from datetime import timedelta
from github import Github

# Add parent src hack 
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../"))

from Print import Print #pylint: disable=E0401
from Env import env #pylint: disable=E0401


print = Print() # add glorious indentation and colors to print


class Transformer(object):
    def __init__(self):
        pass

    def regex_for(self, type):
        expressions = {
            "table": r"(?:Schema::create\(')(.*)(?:')",
            "column_data_type": r"(?:\$table->)([a-z_A-Z]*)",
            "column_name": r"(?:\$table->.*')(.*)(?:')",
        }

        return expressions[type]

    # testing a cleaner interface
    def __getattr__(self, name):
        if name.startswith('regex_for_'):
            return self.regex_for(
                    name.split("regex_for_",1)[1] 
            )
        raise Exception('No such method')

    def table(self):
        return re.findall(
                self.regex_for_table,
                self.file_contents(
                    '/Users/anders/Code/github-scrape-laravel/data/raw/EmpeRoar/application/database/migrations/2014_10_12_000000_create_users_table.php'
                )
        )[0]

    def columns(self):
        return re.findall(
                self.regex_for_column_data_type,
                self.file_contents(
                    '/Users/anders/Code/github-scrape-laravel/data/raw/EmpeRoar/application/database/migrations/2014_10_12_000000_create_users_table.php'
                )
        )        

    def names(self):
        return re.findall(
                self.regex_for_column_name,
                self.file_contents(
                    '/Users/anders/Code/github-scrape-laravel/data/raw/EmpeRoar/application/database/migrations/2014_10_12_000000_create_users_table.php'
                )
        )

    def file_contents(self, path):
        with open(path, 'r') as file:
            return file.read()

if __name__ == '__main__':
    # Demo of the class 
    t = Transformer()
