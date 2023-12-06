""" — Mirar bien canvas — """

# Importación de módulos
from tkinter import *
import tkinter as tk

class Interfaz:

    # Constructor
    def __init__(self, grafo):

        self.grafo = grafo # Grafo
        self.ventana = Tk() # Ventanaaa
        self.ventana.geometry("1200x650") # Tamaño de la ventana
        self.ventana.title("Aeropuertos") # Nombre del Proyecto
        self.ventana.resizable(width=False, height=False) # no renderización de la ventana 
        self.xyz22 = Canvas(self.ventana) # Manejo de la  superficie  
        self.xyz22.pack(fill=BOTH, expand=True) # Posicionamiento
        self.urlFondo = "./recursos/fondo.png"
        self.ok_agregar = tk.BooleanVar()
        self.ok_agregarV = tk.BooleanVar()
        self.ok_agregar_edit = tk.BooleanVar()
        self.lista = []
        self.agregarFondo()
        self.imagenes = []

    """————————————————————————————————————————————GETS & SETS————————————————————————————————————————————————————"""
    def getVentana(self):
        return self.ventana
    
    def getXyz22(self):
        return  self.xyz22

    def generar(self):
        self.xyz22.delete("linea")
        self.crearAristas()

    def agregarFondo(self):
        """Pone una imagen de fondo en la ventana principal."""
        
        self.imagenFondo = PhotoImage(file=self.urlFondo)
        self.xyz22.create_image(0, 0, image=self.imagenFondo, anchor="nw")
        self.xyz22.pack(fill=BOTH, expand=True)
    
    def crearAristas(self):
        for arista in self.grafo.listaAristas:
            
            origen = self.grafo.obtenerVertice(arista.getOrigen(), self.grafo.getListaVertices())
            destino = self.grafo.obtenerVertice(arista.getDestino(), self.grafo.getListaVertices())
            id = self.crearArista(
                origen.getX(),
                origen.getY(),
                destino.getX(),
                destino.getY(),
                arista.getPeso(),
                f"{arista.peso}km-{arista.tiempo}m"
                )
            arista.Id = id

    def crearAristasRecorrido(self, recorrido, color):
        self.xyz22.delete("recorrido")
       
        for arista in recorrido:
            origen = self.grafo.obtenerVertice(arista.getOrigen(), self.grafo.getListaVertices())
            destino = self.grafo.obtenerVertice(arista.getDestino(), self.grafo.getListaVertices())
            self.crearArista(
                origen.getX(),
                origen.getY(),
                destino.getX(),
                destino.getY(),
                arista.peso,
                f"{arista.distancia}-{arista.tiempo}",
                color,
                "recorrido",
                6,
                False,
            )
    
    def crearArista(self, x1, y1, x2, y2, peso, string, color="#3c3c3c", tag="linea", grosor=3.2, it=True):
        """Crea una nueva linea entre dos vertices."""

        id = self.xyz22.create_line(
            x1, y1 + 25, x2, y2 + 25, fill=color, width=grosor, tags=[tag]
        )

        if peso > 0 and it:
            self.xyz22.create_text(
                (x1 + x2) / 2,
                ((y1 + 25 + y2 + 25) / 2) - 10,
                text=string,
                font="Roboto 13 italic",
                tags=["peso"],
            )
        return id

    
    def crearVertices(self, listaVertices):
        for vertice in listaVertices:
            vertice.Id = self.crearVertice(
                vertice.getX(), vertice.getY(), vertice.getNombre(), vertice.getImagen()
            )
    
    def crearVertice(self, x, y, nombre, imagen):
        # urlImagen = "./images/casita.png"
        self.imagenes.append(None)
        self.imagenes[len(self.imagenes) - 1] = PhotoImage(file=imagen)
        idImg = self.xyz22.create_image(
            x, y, image=self.imagenes[len(self.imagenes) - 1], anchor="center", tags=["imagen"]
        )
        self.xyz22.create_text(x + 5, y - 35, text=nombre, font="Cascadia 14 roman", fill="#E74C3C", tags=["texto_imagen"])
        return idImg


    def pintarRecorrido(self):
        self.xyz22.delete("linea")
        self.xyz22.delete("recorrido")
        for arista in self.grafo.listaAristas:
            origen = self.grafo.obtenerVertice(arista.getOrigen(), self.grafo.getListaVertices())
            destino = self.grafo.obtenerVertice(arista.getDestino(), self.grafo.getListaVertices())
            
            self.crearArista(
                origen.getX(),
                origen.getY(),
                destino.getX(),
                destino.getY(),
                arista.getPeso(),
                arista.getColor(),
                "recorrido",
                6,

                )