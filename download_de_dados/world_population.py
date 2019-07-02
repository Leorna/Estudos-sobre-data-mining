import json
import math
from pygal.maps.world import World, COUNTRIES


def get_country_code(country_name):
    """Returns the code of two letters of the parameter"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    
    #If the country was not found
    return None


#Loads the data into a list
filename = 'population_data.json'
with open(filename, 'r') as file:
    pop_data = json.load(file)
    
cc = dict()
     
#Shows the population of each country in 2010
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = math.ceil(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc[code] = population
         
                    
wm = World()
wm.title = 'World Population in 2010'
wm.add('2010 population', cc)
wm.render_to_file('w_pop.svg')