with open("pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()
    
pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]
#print(pokemon_lista)
#import data as d

def validate(name, p_l = pokemon_lista):#, mensaje = d.validacion_pokemon):#input(mensaje).lower()
    if name =='codigo-cero':
        name = 'type-null'
    x = 0
    while name not in p_l:
        return "Pokemon no encontrado"

    return name

if __name__ == '__main__':
    name = 'codigo-cero'
    print(validate(name))
    name = ('Ho-oH').lower()
    print(validate(name))