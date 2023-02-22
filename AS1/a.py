class Investigador:

    def __init__(self, area='', **kwargs):
        print(f"init Investigador con area {area} y kwargs:{kwargs}")
        super().__init__(**kwargs)
        self.area = area
        self.num_publicaciones = 0


class Docente:

    def __init__(self, departamento='', **kwargs):
        print(f"init Docente con depto {departamento} y kwargs:{kwargs}")
        super().__init__(**kwargs)
        self.departamento = departamento
        self.num_cursos = 3


class Academico(Docente, Investigador):

    def __init__(self, nombre, oficina, **kwargs):
        print(f"init Academico con nombre {nombre}, oficina {oficina}, kwargs:{kwargs}")
        super().__init__(**kwargs)
        self.nombre = nombre
        self.oficina = oficina


print(Academico.__mro__)
p1 = Academico(
    "Emilia Donoso",
    oficina="O5",
    area="Inteligencia de Máquina",
    departamento="Ciencia De La Computación"
)
print("--------")
print(p1.nombre)
print(p1.area)
print(p1.departamento)