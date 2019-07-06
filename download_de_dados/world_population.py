import json
import math
from pygal.maps.world import World, COUNTRIES
from pygal.style import RotateStyle, LightColorizedStyle


def get_country_code(country_name):
    """Returns the code of two letters of the parameter"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    
    if country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Tanzania':
        return 'tz'
    elif country_name == 'Vietnam':
        return 'vn'
    elif country_name == 'Egypt':
        return 'eg'
    
    #If the country was not found
    return None


#Loads the data into a list
filename = 'population_data.json'
with open(filename, 'r') as file:
    pop_data = json.load(file)
    
cc_pop = dict()
missing_countries = dict()
     
#Shows the population of each country in 2010
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = math.ceil(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_pop[code] = population        
                    

#groups the countries in three populational levels           
cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for cc, pop in cc_pop.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop
         

hex_color = '#336699'
wm_style = RotateStyle(hex_color, base_style=LightColorizedStyle)                 
wm = World(style=wm_style)
wm.title = 'World Population in 2010'
wm.add('0-10m', cc_pops1)
wm.add('10m-1bn', cc_pops2)
wm.add('>1bn', cc_pops3)
wm.render_to_file('w_pop.svg')