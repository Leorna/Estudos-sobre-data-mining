import requests


#calls the api and stores the answer
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)
print('Status code:', req.status_code)

#stores the answer of the api in a variable
response_dict = req.json()
print('Total repositories:', response_dict['total_count'])

#explores the info about the repositories
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])