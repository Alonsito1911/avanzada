from random import randint, choice, random
from fauna import Carnivoro, Herbivoro, Omnivoro
from parametros import MULTIPLICADOR_RECAUDACION, EVENTO_HERBIVOROS \
                        ,EVENTO_CARNIVOROS, FEROCIDAD, ADORABILIDAD \
                        ,PROBABILIDAD_EVENTO, VISITANTES
from abc import  abstractmethod

# MODIFICAR
@abstractmethod
class Atraccion:

    def __init__(self, numero):
        self.id = numero
        self.animales = []
        self.especies_disponibles = {"Carnivoro":[], "Herbivoro":[], "Omnivoro":[]}
        self.cargar_especies("especimenes.csv")

    def cargar_especies(self, ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                tipo, especie = linea.strip("\n").split(",")
                self.especies_disponibles[tipo].append(especie)

    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentarse()

    # MODIFICAR
    @property
    def visitantes(self) -> int:
        visitante = randint(VISITANTES[0],VISITANTES[1])

        return visitante

    # MODIFICAR
    def recaudacion(self) -> int:
        dinero = 0
        for animal in self.animales:
            animal.alimentarse()
            dinero += animal.ganancia_actual
        u = dinero * self.visitantes * MULTIPLICADOR_RECAUDACION
        probabilidad = random()
        if probabilidad > PROBABILIDAD_EVENTO:
            u += self.evento()
            return u

        else:
            return u
    # MODIFICAR
    @abstractmethod
    def crear_animales(self):
        pass
      
    # MODIFICAR
    @abstractmethod
    def __str__(self):
        pass

    # MODIFICAR
    @abstractmethod
    def evento(self):
        pass


# MODIFICAR
class GranjaHerbivoros(Atraccion):

    # MODIFICAR
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)


    def crear_animales(self):
        tipo = choice(["Herbivoro", "Omnivoro"])
        especies = self.especies_disponibles[tipo]
        seleccionada = choice(especies)
        if tipo == "Herbivoro":
            animal = Herbivoro(especie=seleccionada, adorabilidad=randint(*ADORABILIDAD))
        elif tipo == "Omnivoro":
            animal = Omnivoro(especie=seleccionada, adorabilidad=randint(*ADORABILIDAD), \
                             ferocidad=randint(*FEROCIDAD))
        self.animales.append(animal)

    # MODIFICAR
    def __str__(self) -> str:
        self.numero = 0
        texto = f"Granja he Herbivoros {self.numero}"

        return texto


    
    # MODIFICAR
    def evento(self):
        print(f"\nEVENTO {self}: AVISTAMIENTO DE BRACHIOUSAURUS\n")
        pass
        

# MODIFICAR
class PaseoCarnivoros(Atraccion):

    # MODIFICAR
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def crear_animales(self):
        tipo = choice(["Carnivoro", "Omnivoro"])
        especies = self.especies_disponibles[tipo]
        seleccionada = choice(especies)
        if tipo == "Carnivoro":
            animal = Carnivoro(especie=seleccionada, ferocidad=randint(*FEROCIDAD))
        elif tipo == "Omnivoro":
            animal = Omnivoro(especie=seleccionada, adorabilidad=randint(*ADORABILIDAD), \
                             ferocidad=randint(*FEROCIDAD))
        self.animales.append(animal)

    # MODIFICAR
    def __str__(self):
        self.numero = 0
        texto = f"Granja he Herbivoros {self.numero}"
        return  texto
    # MODIFICAR
    def evento(self):
        print(f"\nEVENTO {self}: SE ALIMENTARA AL TYRANOSAUROS\n")
