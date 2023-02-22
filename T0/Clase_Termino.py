#cuenta los espacios blancos tanto del tablero 2 y tablero 1 para determinar si se termina la partida o no
class Termino:
    def __init__(self,lista1,lista2):
        self.lista1 = lista1
        self.lista2 = lista2
    def contador_monster(self):
        contador = 0
        for i in self.lista2:
            contador += i.count(" ")
        for j in self.lista1:

            contador += j.count(" ")

        return  contador



