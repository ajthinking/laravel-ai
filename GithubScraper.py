import os
import sys
import base64
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
                
            print("Proccessing repo number", repo_number, repo.full_name, '**************************************************************************************')    
            
            root = os.path.dirname(os.path.realpath(__file__))
            repo_folder = os.path.join(root, "scraped", repo.full_name)
            
            if os.path.isdir(repo_folder):
                print('Skipping already harvested repo', repo.full_name)
                continue


            os.makedirs(os.path.dirname(repo_folder), exist_ok=True)

            try:
                migrations = repo.get_dir_contents('database/migrations')
                for migration in migrations:
                    try:
                        self.save_file(repo, migration)    
                    except:
                        print('Could not save database/migrations folder for', repo.full_name)                    
            except:
                print('Could not find database/migrations folder of', repo.full_name)




    def save_file(self, repo, file):
        root = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(root, "scraped", repo.full_name, file.path)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as f:
            f.write(
                    base64.b64decode(
                            repo.get_contents(file.path).content
                    )
            )
            f.close()
            print('Saved', file.path) 