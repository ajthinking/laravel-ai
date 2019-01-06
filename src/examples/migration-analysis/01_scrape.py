import datetime
import sys
import os
from dotenv import load_dotenv
from pathlib import Path
#load_dotenv(dotenv_path=Path('../../../') / '.env')
load_dotenv()

# Add parent src hack 
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../"))

from Print import Print #pylint: disable=E0401
from GithubScraper import GithubScraper #pylint: disable=E0401

GithubScraper(        
        filters = [
                "database/migrations",
                "composer.json"
        ],

        # Release date of Laravel 5
        #start_date = datetime.datetime.strptime('20160823', r'%Y%m%d').date(),
        
        # continue crashed executions 2017-03-13 it got to this data but there was no saved files...
        start_date = datetime.datetime.strptime('20161105', r'%Y%m%d').date(),
        #interval_length = 10000
).scrape()
