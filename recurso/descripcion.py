import random
from recurso.get_module import get_info

def get_descripcion(url_desc):
    poke_desc = get_info(url_desc)["flavor_text_entries"]
    descriptions = [k["flavor_text"].replace("\n", " ") for k in poke_desc if k["language"]["name"] == "es"]
    return random.choice(descriptions)


#=======================================================================
if __name__ == '__main__':
    url = "https://pokeapi.co/api/v2/pokemon-species/1"
    print(get_descripcion(url))