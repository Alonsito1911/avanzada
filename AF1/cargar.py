# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
def cargar_platos(ruta_archivo: str) -> list:
    mis_platos = []
    plato = namedtuple("Plato", ["Nombre", "categoria", "tiempo" , "precio" , "ingredientes"] )

    with open("ruta_archivo","r") as platos:
        platos = file.readlines()
        for plato in platos:
            print(plato)

path = "C:\Users\Lenovo\Desktop\S\Syllabus\Actividades\AF1\cargar.py"

# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    pass
#git add AF1

#lo