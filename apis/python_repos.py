import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


class Config(pygal.Config):
    def __init__(self):
        pygal.Config.__init__(self)
        
        self.x_label_rotation = 60
        self.show_legend = False
        self.title_font_size = 24
        self.label_font_size = 14
        self.major_label_font_size = 18
        self.truncate_label = 15
        self.show_y_guides = False
        self.width = 1000
        

def show_repositories_info(repo_dicts):
    print('\nSelected information about each repository:')
    for repo_dict in repo_dicts:
        print('\nName:', repo_dict['name'])
        print('Owner:', repo_dict['owner']['login'])
        print('Stars:', repo_dict['stargazers_count'])
        print('Repository:', repo_dict['html_url'])
        print('Created:', repo_dict['created_at'])
        print('Updated:', repo_dict['updated_at'])
        print('Description:', repo_dict['description'])


def get_api():
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
    
    store_name_and_stars(repo_dicts)
    

def store_name_and_stars(repo_dicts):
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label_y': repo_dict['description'],
            'xlink': repo_dict['html_url']
        }
        
        plot_dicts.append(plot_dict)
        
    create_graphic(names, plot_dicts)
        
    
def create_graphic(names, plot_dicts):
    #create the visualization
    my_config = Config()
    my_style = LS('#333366', base_style=LCS)
    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred Python Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('python_repos.svg')
    
    
#main
get_api()
