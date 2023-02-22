class TrickOrTreater: #TrickOrTreater = tot

    def __init__(self, nombre: str): 
        self.nombre = nombre
        self.protagonista = False
        self.siguiente = None #persona despues en la fila
    


class ColaDulces:   
    """
    Clase que representa una lista ligada
    """    

    def __init__(self):
        """
        Inicializa una lista ligada vacia, con una referencia nula a su cabeza y cola.
        """
        self.primero = None
        self.ultimo = None

    def tot_llega(self, nombre: str):
        """
        Agrega un nodo al final de la cola
        """
        nuevo = TrickOrTreater(nombre)

        if self.primero is None:
            self.primero = nuevo
            self.ultimo = self.primero

        else:            
            self.ultimo.siguiente = nuevo
            self.ultimo = self.ultimo.siguiente
            
    def obtener_tot(self, posicion: int): 
        """
        Recibe una posición como argumento y retorna 
        el tot en esa posición de la cola
        """
        tot_actual = self.primero
        
        for _ in range(posicion):
            if tot_actual is not None:
                tot_actual = tot_actual.siguiente
            else:
                return None

        return tot_actual
            
            

            
    def obtener_posicion_protagonista(self):
        posicion = 0
        nodo_actual = self.primero
        while nodo_actual.protagonista != True:

            nodo_actual = nodo_actual.siguiente


            posicion += 1

        return posicion


    
    def tot_se_cola(self, nombre: str, posicion: int):
        cliente = TrickOrTreater(nombre)
        cliente_actual = self.primero
        if posicion == 0:
            cliente.siguiente = self.primero
            self.primero = cliente
            if cliente.siguiente is None:
                self.ultimo = cliente

            return
        for _ in range(posicion - 1):
            if cliente_actual is not None:
                cliente_actual = cliente_actual.siguiente
        if cliente_actual is not None:
            cliente.siguiente = cliente_actual.siguiente
            cliente_actual.siguiente = cliente

            if cliente.siguiente is None:
                self.ultimo = cliente
        #VAMOOOOO VAMOOOO CHILENOOOOOOOOO



    def tot_se_va(self, posicion: int):
        """
        Elimina a la persona de la posición recibida de la cola.
        """
        if posicion == 0:
            tot_nuevo = self.primero.siguiente
            self.primero.siguiente = None
            self.primero = tot_nuevo

            if tot_nuevo.siguiente is None:
                self.ultimo = tot_nuevo

            return
            
        tot_actual = self.obtener(posicion-1)
        tot_fuera = tot_actual.siguiente
        tot_actual.siguiente = tot_fuera.siguiente
        tot_fuera.siguiente = None
        if tot_actual.siguiente is None:
            self.ultimo=tot_actual
    
    def atender_tot(self):

        cliente = self.primero
        self.primero = cliente.siguiente

        return cliente


    def obtener_largo(self):
        posicion = 0
        nodo_actual = self.primero
        while nodo_actual != None:

            nodo_actual = nodo_actual.siguiente

            posicion += 1

        return posicion


    def __str__(self) -> str:
        """
        Retorna una representación de la fila con los nombres de
        cada uno de sus participantes.
        """
        string = "DULCES :) "
        tot_actual = self.primero
        while tot_actual:
            string += "<- "+tot_actual.nombre
            tot_actual = tot_actual.siguiente
   
        return string