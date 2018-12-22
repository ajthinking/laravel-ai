import os
import sys
import base64
import time
from github import Github
from Print import Print
from Env import env

print = Print() # add glorious indentation and colors to print

class GithubScraper(object):
    def __init__(
                    self,
                    max_repos = float('inf'),
                    overwrite_repos = True,
                ):
        self.max_repos = max_repos
        self.github = Github(env.GITHUB_ACCESS_TOKEN)

    def scrape(self):
        print.info("Initializing scrape")
        for repo_number, repo in enumerate(self.github.search_repositories(query="Laravel", sort="stars")):
            print.reset()
            if repo_number >= self.max_repos:
                print.warning("Max number of repos processed, bye bye")
                break

            if self.github.rate_limiting[0] <= 1:
                print.warning("Going to sleep for 60 seconds due to API rate limiting:")
                print(self.github.rate_limiting[1] - self.github.rate_limiting[0], "/",self.github.rate_limiting[1])
                time.sleep(60)
                # Hack! resets the rate_limit dump to the core API
                # Then the rate will probably OK so we dont go back to sleep
                self.github.get_rate_limit()

            print.info(repo_number, repo.full_name, '**************************************************************************************')    
            print.group()

            root = os.path.dirname(os.path.realpath(__file__))
            repo_folder = os.path.join(root, "scraped", repo.full_name)
            
            if os.path.isdir(repo_folder):
                print.warning('Skipping already harvested repo', repo.full_name)
                continue

            os.makedirs(repo_folder, exist_ok=True)

            try:
                migrations = repo.get_dir_contents('database/migrations')
                for migration in migrations:
                    try:
                        self.save_file(repo, migration)    
                    except:
                        print.fail('Could not save database/migrations folder for', repo.full_name)                    
            except:
                print.fail('Could not find database/migrations folder of', repo.full_name)
        
        print.success("Done!")



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
            print.success('Saved', file.path) 