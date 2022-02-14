from recurso.get_module import get_info
def pokemonVsTipo(urlTipo):
    versus_tipo = get_info(urlTipo)
    damage_relations = {
    "debil_contra":[k["name"] for k in versus_tipo["damage_relations"]['double_damage_from']],
    "resistente_contra": [k["name"] for k in versus_tipo["damage_relations"]['half_damage_from']],
    "inmune_contra": [k["name"] for k in versus_tipo["damage_relations"]['no_damage_from']],
    "super_efectivo_contra": [k["name"] for k in versus_tipo["damage_relations"]['double_damage_to']],
    "poco_eficaz_contra": [k["name"] for k in versus_tipo["damage_relations"]['half_damage_to']],
    "ineficaz_contra": [k["name"] for k in versus_tipo["damage_relations"]['no_damage_to']]
    }
    return damage_relations



if __name__ == '__main__':
    url = "https://pokeapi.co/api/v2/type/1"
    pokemonVsTipo(url)

#python pokemon_vstipo.py