import random
import parametros
def  tabla(filas, columnas, valores):
    #Crea una matriz con las dimensiones que se pidieron
    tablero = []
    for i in range(filas):

        tablero.append([])

        for j in range(columnas):

            tablero[i].append(valores)
    return tablero

def  monsters(t,filas, columnas, monsters):
    #Coloca las N en partes aleatorias del tablero creado
    lista = []
    contador = 0
    while contador < monsters:
        x = random.randint(0, columnas - 1)
        y = random.randint(0, filas-1)
        if t[y][x] == " ":
            coor = (x, y)
            lista.append(coor)
            t[y][x] = "N"
            contador += 1
    print(lista)
    return t
#En esta funcion agregamos a puntajes.txt el usuario y el puntaje del jugador que gano la partida
def mejores_puntajes(tablero2,usuario):
    #Escribe el puntaje en el archivo cada vez cuando se termina una partida
    contador = 0
    contador1 = 0
    for i in tablero2:
        contador += i.count("N")
    for j in tablero2:
        contador1 += j.count(" ")

    puntaje = contador1 * contador * parametros.POND_PUNT

    string_puntaje = f"{puntaje},{usuario}"

    archivo = open("puntajes.txt", "a")
    archivo.write(f"{string_puntaje}\n")
    return puntaje
def mejores_diez():
    #Muestra los 10 mejores puntajes con sus usarios
    fichero = open("puntajes.txt", "r")
    todasLaslineas = fichero.readlines()
    lista1 = []
    lista_int = []
    for i in todasLaslineas:
        lista2 = i.replace("\n","").split(",")
        print(lista2)
        #transformamos nuestro lista2[0] en un entero para poder ordenar
        lista_int = [int(lista2[0]),lista2[1]]
        lista1.append(lista_int)

    lista_mejores = sorted(lista1, reverse=True)
    print(lista_mejores)
    contador = 0
    for j in lista_mejores:

        print(j[0],j[1])
        contador += 1
        if contador == 10:
            break






def hacer_tablero(lista):
    "Transforma la informacion de un texto de la carpeta partidas en tablero nuevameante"

    #tabla1 sera la matriz a la cual le iremos descubriendo casillas
    tabla1 = []
    #tabla_original sera la matriz la cual contiene la ubicacion principal de las bestias
    tabla_original = []
    #contador1 nos servira para no tomar en cuenta los corchetes principales y finales
    contador1 = 0

    contador_corchetes = 0
    for j in lista:
        contador1 += 1
        if len(lista) > contador1 > 0:
            if j == "[":
                contador_corchetes += 1
            if j == "]":
                contador_corchetes += 1
            if contador_corchetes == 2:
                tabla1.append([])
                contador_corchetes = 0

    print(tabla_original)
#Estos dos contadores cumpliran una funcion parecida a  que contador1 y contador_corchetes
    cont1 = 0
    cont2 = 0
#Con recorredor iremos iterando en el tablero1
    recorredor = 0
    espacio = 0
    for j in lista:
        cont1 += 1
        if len(lista) > cont1 > 0:
            if j == "[":
                cont2 = 1
            if j == "'":
                espacio += 1
            if cont2 == 1:
                if j == "N" :
                    tabla1[recorredor].append(j)

                    espacio = -1

                if j == "0" or j == "1" or j == "2" or j == "3" or j == "4" or j == "5" or j == "6" or j == "7" or j == "8":
                    tabla1[recorredor].append(j)

                    espacio = -1

                if espacio == 2:
                    tabla1[recorredor].append(" ")

                    espacio = 0
            if j == "]":
                cont2 = 0
                recorredor += 1

    return tabla1




