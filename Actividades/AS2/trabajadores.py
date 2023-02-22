import time
from time import sleep
from threading import Thread

from centro_urbano import CentroUrbano

from parametros import ENERGIA_RECOLECTOR, ORO_RECOLECTADO, \
    TIEMPO_RECOLECCION, TIEMPO_CONSTRUCCION, ORO_CHOZA


# Completar
class Recolector(Thread):


    def __init__(self, nombre: str, centro_urbano: CentroUrbano) -> None:
        super().__init__()
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        self.energia = ENERGIA_RECOLECTOR
        self.oro = 0
        self.daemon = True

        # Completar

    def run(self) -> None:
        self.trabajar()
        self.ingresar_oro()
        self.dormir()

    def log(self, mensage: str) -> None:
        print(f"El recolector {self.nombre}: {mensage}")

    def trabajar(self) -> None:
        # Completar
        self.log("empezo a trabajar.....")
        if self.energia > 0:
            self.oro += ORO_RECOLECTADO
            self.energia -= 1
            time.sleep(TIEMPO_RECOLECCION)
        pass

    def ingresar_oro(self) -> None:
        with self.centro_urbano.lock_oro :
            self.centro_urbano.oro += self.oro
            self.log(f"ha ingresado oro {self.oro} al centro urbano, ahora el centro urbano tiene {self.centro_urbano.oro} en oro")
            # Completar

        pass

    def dormir(self) -> None:
        self.log("ha terminado su turno, procede a mimir")


# Completar
class Constructor(Thread):

    def __init__(self, nombre, centro_urbano: CentroUrbano) -> None:
        super().__init__()
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        self.daemon = True
        # Completar

    def run(self) -> None:
        while self.retirar_oro():
            self.log("está construyendo una choza de bárbaros")
            sleep(TIEMPO_CONSTRUCCION)
            self.construir_choza()
        self.log("terminó su trabajo por el día")

    def log(self, mensage: str) -> None:
        print(f"El constructor {self.nombre}: {mensage}")

    def retirar_oro(self) -> bool:

        with self.centro_urbano.lock_oro:
            if self.centro_urbano.oro >= ORO_CHOZA:
                self.centro_urbano.oro -= ORO_CHOZA
                self.log(f"ha retirado {ORO_CHOZA}, ahora centro urbano tiene {self.centro_urbano.oro} en oro")

                return True
            else:
                self.log("no ha encontrado suficiente oro ")

                return False

        # Completar
        pass

    def construir_choza(self) -> None:

        with self.centro_urbano.lock_chozas:
            self.centro_urbano.chozas += 1

            self.log(f"ha agregado 1 choza, el centro urbano ahora tiene {self.centro_urbano.chozas} ")


        # Completar
        pass
