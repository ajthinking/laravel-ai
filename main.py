from github import Github

github = Github("2dcce1db26a94b4b4ff884e82fe902cf2e9a834a")

for i, repo in enumerate(github.search_repositories(query="Laravel", sort="stars")):
    if i > 0:
        break
    
    tree = repo.get_git_tree(
            repo.get_commits()[0].sha,
            True
    ).tree

    for element in tree:
        pass #print(element)

    print(" \n")

    try:
        migrations = repo.get_dir_contents('database/migrations')
    except:
        print('There was a problem when trying to get the database/migrations folder')


    print(migrations)


















# Ok, but how to get the custom quota for the SEARCH API?
#print("Your quota", github.get_rate_limit()) # 5000/5000
#print("Your quota", github.rate_limit) # 28/30