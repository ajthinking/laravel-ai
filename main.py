from GithubScraper import GithubScraper

GithubScraper(
        #max_repos=1,
        filters = [
                #"database/migrations",
                "composer.json"
        ]
).scrape()