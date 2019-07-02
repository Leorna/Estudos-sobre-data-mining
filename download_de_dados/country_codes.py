from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Returns the code of two letters of the parameter"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    
    #If the country was not found
    return None





