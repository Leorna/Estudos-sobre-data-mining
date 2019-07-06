import json
from pygal.maps.world import World, COUNTRIES
from pygal.style import RotateStyle, LightColorizedStyle


filename = 'gdp_json.json'


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        
    return None


def store_pib_info(country_infos, countries_pib):
    if country_infos['Year'] == 2014:
        country_name = country_infos['Country Name']
        pib = country_infos['Value']
        country_code = get_country_code(country_name)
            
        if country_name:
            countries_pib[country_code] = pib


def get_countries_pib():
    with open(filename, 'r') as file:
        countries_infos = json.load(file)
          
    countries_pib = dict()   
     
    for country_infos in countries_infos:
       store_pib_info(country_infos, countries_pib)
       
    return countries_pib       
      
            
hex_color = '#300011'
wm_style = RotateStyle(hex_color)

wm = World(style=wm_style)
wm.title = 'PIB in 2014, by country'
wm.add('2014', get_countries_pib())
wm.render_to_file('pib.svg')