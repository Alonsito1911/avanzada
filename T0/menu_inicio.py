import math
import parametros
import funciones
import Clase_Termino
import descubrir_casillas
import tablero
import os
if os.path.exists("partidas") == False:
    ruta = os.getcwd()
    nombre = "partidas"
    ruta_final = ruta + "\\" + nombre
    os.mkdir(ruta_final)
class  Menu_juego:
    def __init__(self, tablero1, tablero2, usuario):
        self.tablero1 = tablero1
        self.tablero2 = tablero2
        self.usuario = usuario


        self.opciones = {   "1": self.descubrir_sector,
                            "2": self.guardar_partida,
                            "3": self.salir_partida} #creamos un diccionario para acceder a los metodos
    def menu(self):

        print("Seleccion una opcion:\n[1] Descubrir un sector\n[2] Guardar la partida\n[3] Salir de la partida")

    def menu_juego(self, o):
        opcion = o
        casillas_restantes = True
        while opcion != "3" and casillas_restantes:
            self.menu()
            opcion = input("Eliga su opcion: ")
            dicc = self.opciones.get(opcion)
            if dicc:
                dicc()
            else:
                print(f"[{opcion}] no esta dentro de nuestras opciones, porfavor elige otra")
            suma_celda_vacias = Clase_Termino.Termino(self.tablero1, self.tablero2).contador_monster()

            dimension_matriz = len(self.tablero1) * (len(self.tablero1[0]))
            if dimension_matriz < suma_celda_vacias:
                casillas_restantes = True
            else:
                casillas_restantes = False
        if opcion != "3":
            funciones.mejores_puntajes(self.tablero2, self.usuario)
            contador = 0
            contador1 = 0
            for i in self.tablero2:
                contador += i.count("N")
            for j in self.tablero2:
                contador1 += j.count(" ")

            puntaje = contador1 * contador * parametros.POND_PUNT

            print(f"Felicidades, has ganado {self.usuario} con un puntaje:{puntaje} ")

        menu_inicio()
    def descubrir_sector(self):
        #crearemos un diccionario para ocupar coordenadas alfanumericas
        diccionario_alfanumerico = {"A": 0,"B": 1, "C": 2, "D": 3,  "E": 4,  "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
                                    "K": 10, "L": 11, "M": 12, "N": 13, "O": 14}
        tablero.print_tablero(self.tablero1, utf8=True)
        altura = len(self.tablero1)
        ancho = len(self.tablero1[0])
        print("Eliga coordenadas:")
        x = input("Coordenada Numerica:")
        while x != "0" and x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "6" and x != "7" \
        and x != "8" and x != "9" and x != "10" and x != "11" and x != "12" and x != "13"  and x != "14":
            x = input("Eliga su coordenada numerica correctamente:")

        while int(x) >= altura or int(x) < 0:
            x = int(input("Ingrese su coordenada numerica nuevamante: "))
        y = input("Coordenada Alfabetica:")
        #jjejeje vaya forma:/
        while y != "A" and y != "B" and y != "C" and y != "C" and y != "D" and y != "E" and y != "F" and y != "G" \
        and y != "H" and y != "I" and y != "J" and y != "K" and y != "L" and y != "M"  and y != "N":
            y = input("Ingrese la coordenada alfabetica correctamente:")
        letra = diccionario_alfanumerico.get(y)

        u = descubrir_casillas.calcular_casillas(self.tablero2, int(x) , letra)
        if u != "N":
            self.tablero1[int(x)][letra] = str(u)

            tablero.print_tablero(self.tablero1)
        else:
            print("Cueak, has perdido")
            file = os.path.exists(f'partidas\{self.usuario}.txt')

            if file == True:

                os.remove(f"partidas\{self.usuario}.txt")
                menu_inicio()

            else:

                menu_inicio()



    def guardar_partida(self):

        archivo = open(f"partidas\{self.usuario}.txt", "w")
        archivo.close()
        archivo = open(f"partidas\{self.usuario}.txt", "a")
        archivo.write(f"{self.tablero1};")
        archivo.write(f"{self.tablero2}")
        archivo.close()
        print("GUARDADO EXITOSO!")


    def  salir_partida(self):

        print("Desea guardar la partida\n[1] No\n[2] SI")
        opcion = input("Opcion: ")
        if opcion == "1":
            print(" ")
            print(" ")
            menu_inicio()

        if opcion == "2":
            archivo = open(f"partidas\{self.usuario}.txt", "w")
            archivo.close()
            archivo = open(f"partidas\{self.usuario}.txt", "a")
            archivo.write(f"{self.tablero1};")
            archivo.write(f"{self.tablero2}")
            print("Partida guardada correctamente, Nos vemos!")
            menu_inicio()
##prueba

def menu_inicio():
    print("Bienvenidos a Star Advanced")
    print("############################")
    print("Seleccione una opcion:\n[1] Crear Partidad\n[2] Cargar Partida\n[3] Ver ranking\n[0] Salir")
    opcion = input("Ingrese su opcion:")

    print(" ######### ")
    print("   ##### ")
    print("    ### ")

    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "0":
        opcion = input("INGRESE UNA OPCION CORRECTAMENTE:")





    if opcion == "1":
        usuario = input("Nombre de usuario:")
        if usuario == "":
            print("el nombre ingresado debe ser valido ")
            menu_inicio()

        print("Ingrese la altura y el ancho de su tablero\nRecuerde que dichos valores deben estar dentro del intervalo [3,15]!:)")
        largo = int(input("altura:"))

        while largo > 15 or largo < 3:
            largo = int(input("Ingrese nuevamente la altura de su tablero:"))
        ancho = int(input("ancho: "))
        while ancho > 15 or ancho < 3:
            ancho = int(input("Ingrese nuevamente el ancho de su tablero:"))
        tablero_1 = funciones.tabla(largo, ancho, " ")
        tablero_2 = funciones.tabla(largo, ancho, " ")
        m = largo * ancho * parametros.PROB_BESTIA
        cantidad_bestias = math.ceil(m)
        print(f"Jugaras con {cantidad_bestias} bestias, SUERTE!")
        funciones.monsters(tablero_2,len(tablero_2),len(tablero_2[0]),m)



        print("Tu estado actual de tu tablero es:")

        tablero.print_tablero(tablero_1)

        m1 = Menu_juego(tablero_1,tablero_2,usuario)

        m1.menu_juego(0)


    if opcion == "2":
        print("Ingrese su nombre de usuario!")
        nombre = input()
        if os.path.exists(f"partidas\{nombre}.txt") == True:
            archivo = open(f"partidas\{nombre}.txt", "r")

            primeralinea = archivo.readline()
            lista1 = primeralinea.split(";")
            lista_a_ocupar1 = lista1[0]
            lista_a_ocupar2 = lista1[1]
            archivo.close()
            # calcularemos el ancho y la altura nuevamente (solo una lista)

            newtablero = funciones.hacer_tablero(lista_a_ocupar1)

            newtablero2 = funciones.hacer_tablero(lista_a_ocupar2)
            print(newtablero)
            tablero.print_tablero(newtablero, utf8=False)
            m2 = Menu_juego(newtablero, newtablero2, nombre)
            m2.menu_juego(0)
        else:
            print("Lamentamos pero este archivo no existe;(")
            menu_inicio()
    if opcion == "3":
        print("10 mejores puntajes")
        funciones.mejores_diez()
        menu_inicio()

    if opcion == "0":

        print("Nos vemos pronto!")
    if opcion == "":
        menu_inicio()
menu_inicio()
