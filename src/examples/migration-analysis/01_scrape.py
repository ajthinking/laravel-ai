import datetime
import sys
import os

# Add parent src hack 
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../"))

from Print import Print #pylint: disable=E0401
from Env import env #pylint: disable=E0401
from GithubScraper import GithubScraper #pylint: disable=E0401

GithubScraper(
        #max_repos=1,
        
        filters = [
                "database/migrations",
                "composer.json"
        ],

        # Release date of Laravel 5
        #start_date = datetime.datetime.strptime('20160823', r'%Y%m%d').date(),
        
        # continue crashed executions
        start_date = datetime.datetime.strptime('20161105', r'%Y%m%d').date(),
        #interval_length = 1
).scrape()