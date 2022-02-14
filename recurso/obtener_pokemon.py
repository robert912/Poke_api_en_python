
from recurso.get_module import get_info
from recurso.poke_validation import validate
from recurso.pokemon_vs_tipo import pokemonVsTipo
from recurso.descripcion import get_descripcion

def obtenerPokemon(pokemon):
    tipo = None
    pokeValid = validate(pokemon)
    if pokeValid != pokemon and pokeValid != "type-null":
        return pokeValid
    url = "https://pokeapi.co/api/v2/pokemon/"
    infoPokemon = get_info(url+pokeValid)
    tipos = [k["type"]["name"] for k in infoPokemon["types"]]
    indi_esp = get_indicador_especial(infoPokemon['id'])
    if indi_esp:
        tipos.append(indi_esp)
    vsTipos = [pokemonVsTipo(k["type"]["url"]) for k in infoPokemon["types"]]
    vsTipos = {k :v for k,  v in vsTipos[0].items()} if len(vsTipos) == 1 else {k : set(v + vsTipos[1][k]) for k,  v in vsTipos[0].items()}

    estadisticas = {
        "hp":infoPokemon["stats"][0]["base_stat"],
        "ataque":infoPokemon["stats"][1]["base_stat"],
        "defensa":infoPokemon["stats"][2]["base_stat"],
        "ataque_esp":infoPokemon["stats"][3]["base_stat"],
        "defensa_esp":infoPokemon["stats"][4]["base_stat"],
        "velocidad":infoPokemon["stats"][5]["base_stat"]
    }

    data_pokemon = {
        "id": infoPokemon["id"],
        "nombre": infoPokemon["name"],
        "img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/"+str(infoPokemon['id'])+".png",
        "tipo": tipos,
        "tipo_vs": vsTipos,
        "estadisticas":estadisticas,
        "descripcion": get_descripcion("https://pokeapi.co/api/v2/pokemon-species/"+str(infoPokemon['id']))
    }

    return data_pokemon

def tipo_html(tipos):
    tipos_html = ""
    if len(tipos):
        for t in tipos:
            tipos_html += "<span class='label "+t+"'>"+diccionario_es[t]+"</span>"
    return tipos_html

diccionario_es = {
    "normal": "Normal", "fire": "Fuego", "flying": "Volador",
    "steel": "Acero", "water": "Agua", "electric": "Eléctrico",
    "grass": "Planta", "ice": "Hielo", "fighting": "Lucha",
    "poison": "Veneno", "ground": "Tierra", "psychic": "Psíquico",
    "bug": "Bicho", "rock": "Roca", "ghost": "Fantasma",
    "dragon": "Dragón", "dark": "Siniestro", "fairy": "Hada", 
    "baby": "Bebé", "legendary": "Legendario", "mythical": "Mítico"
}

def get_indicador_especial(id_poke):
    especial = get_info("https://pokeapi.co/api/v2/pokemon-species/"+str(id_poke))
    return "baby" if especial["is_baby"] else "legendary" if especial["is_legendary"] else "mythical" if especial["is_mythical"] else None

#=======================================================================
if __name__ == '__main__':
    poke = ("Mr-Mime").lower()
    print(obtenerPokemon(poke))