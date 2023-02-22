#funcion que nos permitira descubrir casillas
#esquinas izquierda superior
def calcular_casillas(tablero_original, x, y):
    altura = len(tablero_original)
    ancho = len(tablero_original[0])
    if tablero_original[x][y] != "N":
        if (x == 0 and y == 0):
            contador = 0
            if tablero_original[0][1] == "N":
                contador += 1

            if tablero_original[1][1] == "N":
                contador += 1

            if tablero_original[1][0] == "N":
                contador += 1

            return contador
        # esquina izquierda inferior
        if (x == altura - 1 and y == 0):
            print("Hey estamos en esquina izquierda inferior ")
            contador2 = 0
            if tablero_original[x - 1][0] == "N":
                contador2 += 1

            if tablero_original[x][1] == "N":
                contador2 += 1

            if tablero_original[x - 1][1] == "N":
                contador2 += 1

            return contador2
        # esquina derecha superior
        if (x == 0 and y == ancho -1):
            print("Hey estamos en esquina derecha superior ")
            contador3 = 0
            if tablero_original[0][altura - 1] == "N":
                contador3 += 1

            if tablero_original[1][ancho - 1] == "N":
                contador3 += 1

            if tablero_original[1][ancho - 1] == "N":
                contador3 += 1

            return contador3

        # esquina derecha inferior
        if (x == altura -1 and y == ancho - 1):
            print("Hey estamos en esquina derecha inferior ")
            contador3 = 0
            if tablero_original[x][y] == "N":
                contador3 += 1

            if tablero_original[x][y - 1] == "N":
                contador3 += 1

            if tablero_original[x - 1][y - 1] == "N":
                contador3 += 1

            return contador3
        # entre esquinas izquierda 5 casos
        if (0 < x < altura -1) and y == 0:
            print("Hey estamos entre esquina izquierda")
            contador3 = 0
            if tablero_original[x - 1][0] == "N":
                contador3 += 1

            if tablero_original[x + 1][0] == "N":
                contador3 += 1

            if tablero_original[x][1] == "N":
                contador3 += 1

            if tablero_original[x + 1][1] == "N":
                contador3 += 1

            if tablero_original[x - 1][1] == "N":
                contador3 += 1
            return contador3

        # entre esquina derecha 5 casos posibles
        if (0 < x < altura) and y == ancho - 1:
            contador4 = 0
            if tablero_original[x - 1][y] == "N":
                contador4 += 1

            if tablero_original[x - 1][y - 1] == "N":
                contador4 += 1

            if tablero_original[x][y - 1] == "N":
                contador4 += 1

            if tablero_original[x + 1][y - 1] == "N":
                contador4 += 1

            if tablero_original[x + 1][y] == "N":
                contador4 += 1

            return contador4
        if (0 < y < ancho) and x == 0:
            contador4 = 0
            if tablero_original[x][y -1] == "N":
                contador4 += 1

            if tablero_original[x][y + 1] == "N":
                contador4 += 1

            if tablero_original[x + 1][y - 1] == "N":
                contador4 += 1

            if tablero_original[x + 1][y] == "N":
                contador4 += 1

            if tablero_original[x + 1][y + 1] == "N":
                contador4 += 1

            return contador4
        # casillas de al medio 8 casos posibles
        if (0 < y < ancho) and x == altura - 1:
            contador4 = 0
            if tablero_original[x][y - 1] == "N":
                contador4 += 1

            if tablero_original[x][y + 1] == "N":
                contador4 += 1

            if tablero_original[x - 1][y - 1] == "N":
                contador4 += 1

            if tablero_original[x - 1][y] == "N":
                contador4 += 1

            if tablero_original[x - 1][y + 1] == "N":
                contador4 += 1

            return contador4


        if (0 < x < altura-1) and (0 < y < ancho-1):
            contador5 = 0
            if tablero_original[x - 1][y - 1] == "N":
                contador5 += 1

            if tablero_original[x - 1][y] == "N":
                contador5 += 1

            if tablero_original[x - 1][y + 1] == "N":
                contador5 += 1

            if tablero_original[x][y - 1] == "N":
                contador5 += 1

            if tablero_original[x][y + 1] == "N":
                contador5 += 1

            if tablero_original[x + 1][y - 1] == "N":
                contador5 += 1

            if tablero_original[x + 1][y] == "N":
                contador5 += 1

            if tablero_original[x + 1][y + 1] == "N":
                contador5 += 1

            return contador5
    if tablero_original[x][y] == "N":

        return "N"



