import datetime

#

from GithubScraper import GithubScraper

GithubScraper(
        #max_repos=1,
        
        filters = [
                "database/migrations",
                "composer.json"
        ],

        # Release date of Laravel 5
        #start_date = datetime.datetime.strptime('20160823', r'%Y%m%d').date(),
        
        # continue crashed execution
        start_date = datetime.datetime.strptime('20161018', r'%Y%m%d').date(),
        #interval_length = 1
).scrape()