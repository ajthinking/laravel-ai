import os
from github import Github

class GithubScraper(object):
    def __init__(
                    self,
                    max_repos = float('inf'),
                    overwrite_repos = True,
                ):
        self.max_repos = max_repos
        self.github = Github("2dcce1db26a94b4b4ff884e82fe902cf2e9a834a")

    def scrape(self):
        print("Initializing scrape")
        for repo_number, repo in enumerate(self.github.search_repositories(query="Laravel", sort="stars")):
            if repo_number >= self.max_repos:
                print("Max number of repos processed")
                break
            try:
                migrations = repo.get_dir_contents('database/migrations')
                for migration in migrations:
                    self.save_file(repo, migration)
            except:
                print('There was a problem when trying to get the database/migrations folder')

    def save_file(self, repo, file):
        try:
            root = os.path.dirname(os.path.realpath(__file__))
            filename = os.path.join(root, "scraped", repo.full_name, file.path)
        except:
            print("something here")

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            pass
            f.write(repo.file_get_content('composer.json')) # the error is here!
            f.close() 