from string import Template
from recurso.obtener_pokemon import *
from recurso.show import show_pics


with open('template/template_pokemon.html','r') as infile:
    entrada = infile.read()

document_template = Template(entrada)
pokemon = input("Ingrese el nombre del Pokemon: ").replace(" ","-").lower()

datos = obtenerPokemon(pokemon)
if isinstance(datos, str):
    print(datos)
    exit()

document_template_nuevo = document_template.substitute(
id = datos["id"], 
name = datos["nombre"].title() if datos["nombre"] != "type-null" else "Codigo Cero", 
img = datos["img"], 
hp = datos["estadisticas"]["hp"],
ataque = datos["estadisticas"]["ataque"],
defensa = datos["estadisticas"]["defensa"],
at_especial = datos["estadisticas"]["ataque_esp"],
def_especial = datos["estadisticas"]["defensa_esp"],
vel = datos["estadisticas"]["velocidad"],
tipo_poke = tipo_html(datos["tipo"]),
descripcion = datos["descripcion"],
super_efectivo_contra = tipo_html(datos["tipo_vs"]["super_efectivo_contra"]),
debil_contra = tipo_html(datos["tipo_vs"]["debil_contra"]),
resistente_contra = tipo_html(datos["tipo_vs"]["resistente_contra"]),
poco_eficaz_contra = tipo_html(datos["tipo_vs"]["poco_eficaz_contra"]),
inmune_contra = tipo_html(datos["tipo_vs"]["inmune_contra"]),
ineficaz_contra = tipo_html(datos["tipo_vs"]["ineficaz_contra"])
)

show_pics(document_template_nuevo, "output.html")