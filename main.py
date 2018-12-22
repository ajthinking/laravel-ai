from GithubScraper import GithubScraper

GithubScraper(
        max_repos=8,
        filters = [
                "database/migrations",
                "composer.json"
        ]
).scrape()