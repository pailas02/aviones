"""— Clase vértice —"""

class Vertice:

    # Constructor
    def __init__(self, nombre, x, y):
        self.nombre = nombre
        self.Id = 0
        self.listaAdyacentes = []
        self.x = x
        self.y = y
        # self.imagen = "./recursos/icono_libreria.jpg"
        self.imagen = "./recursos/avion.png"


    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""
    # Set - Get | nombre
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    # Set - Get | lista adyacentes
    def getListaAdyacentes(self):
        return self.listaAdyacentes

    def setListaAdyacentes(self,listaAdyacentes):
        self.listaAdyacentes = listaAdyacentes
    
    # Set - Get | x
    def getX(self):
        return self.x
    
    def setX(self, x):
        self.x = x
    
    # Set - Get | y
    def getY(self):
        return self.y
    
    def setY(self, y):
        self.y = y

    # Set - Get | imagen
    def getImagen(self):
        return self.imagen
    
    def setImagen(self, imagen):
        self.imagen = imagen




