"""— Clase grafo —"""

#  Importación de módulos
from copy import copy #para realizar copias de objetos
from clases.arista import *
from clases.vertice import *

class Grafo:

   # Constructor
   def __init__(self):
      self.listaVertices = []
      self.listaAristas = []
      self.profundidad = []
      self.anchura = []
   
   """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""
   
   # Set - Get | lista de vertices
   def getListaVertices(self):
      return self.listaVertices

   def setListaVertices(self, listaVertices):
      self.listaVertices = listaVertices

   # Set - Get | lista de aristas
   def getListaAristas(self):
      return self.listaAristas

   def setListaAristas(self, listaAristas):
      self.listaAristas = listaAristas

   # Set - Get | recorrido profundidad
   def getProfundidad(self):
      return self.profundidad

   def setProfundidad(self, profundidad):
      self.profundidad = profundidad

   # Set - Get | recorrido anchura
   def getAnchura(self):
      return self.anchura

   def setAnchura(self,anchura):
      self.anchura = anchura

   """—————————————————————————————————————————FUNCIONES VERTICE————————————————————————————————————————————————"""
   # Ingresar vértice
   def ingresarVertice(self, nombre, x, y):
      if not self.existeVertice(nombre, self.listaVertices):
            self.listaVertices.append(Vertice(nombre, x, y))

   # Existe vértice
   def existeVertice(self, nombre, listaVertices):
      for i in listaVertices:
         if nombre == i.getNombre():
            return True
      return False

   # Obtener vértice
   def obtenerVertice(self, origen, lista):
      for i in lista:
         if origen == i.getNombre():
            return i

   """—————————————————————————————————————————FUNCIONES ARISTA—————————————————————————————————————————————————"""

   # Ingresar arista
   def ingresarArista(self, origen, destino, peso,tiempo):
      if not self.existeArista(origen, destino, self.listaAristas):
         if self.existeVertice(origen, self.listaVertices) and self.existeVertice(destino, self.listaVertices):
            self.listaAristas.append(Arista(origen, destino, peso,tiempo))
            self.obtenerVertice(origen, self.listaVertices).getListaAdyacentes().append(destino)

   # Existe arista
   def existeArista(self, origen, destino, lista):
      for i in lista:
         if origen == i.getOrigen() and destino == i.getDestino():
            return True
      return False     
   
   # Obtener Arista
   def obtenerArista(self, origen, destino, lista):
      for i in lista:
         if origen.lower() == i.getOrigen().lower() and destino.lower() == i.getDestino().lower():
            return i
   
   # Obtener arista de menor peso
   def obtenerAristaMenor(self, aristas):
      menor = aristas[0]
      for a in aristas:  
         if a.getPeso() < menor.getPeso():
            menor = a
      return menor
   
   def eliminarArista(self, origen, destino):
      verticeOrigen = self.obtenerVertice(origen, self.listaVertices)
      aristaOrigen = self.obtenerArista(origen, destino, self.listaAristas)
      if aristaOrigen:
         verticeOrigen.getListaAdyacentes().pop(verticeOrigen.getListaAdyacentes().index(destino))
         self.listaAristas.pop(self.listaAristas.index(aristaOrigen))

      verticeDestino = self.obtenerVertice(destino, self.listaVertices)
      aristaDestino = self.obtenerArista(destino, origen, self.listaAristas)
      if aristaDestino:
         verticeDestino.getListaAdyacentes().pop(verticeDestino.getListaAdyacentes().index(origen))
         self.listaAristas.pop(self.listaAristas.index(aristaDestino))
      
   """—————————————————————————————————————————————FUNCTIONS————————————————————————————————————————————————————————"""           

   # Convertir dirigido a no dirigido
   def noDirigido(self):
      lista = copy(self.listaAristas)
      for i in lista:
         crear = True
         for j in lista:
            if i.getOrigen() == j.getDestino() and i.getDestino() == j.getOrigen():
               crear = False
               break
         if crear:
            self.ingresarArista(i.getDestino(), i.getOrigen(), i.getPeso(),i.tiempo)
   




   #prim
   def prim(self, origen):
      verticesAux = []
      verticesD = []
      caminos = self.ordenarPrim(origen, verticesAux)
      self.rutas(verticesD, verticesAux, origen, origen)
      aristas = []
      for i in range(1,len(verticesD)):
         aristas.append(self.obtenerArista(verticesD[i],verticesAux[i], self.listaAristas))
      return aristas
   
   def ordenarPrim(self, origen, verticesAux):
      visitados = []
      caminos = []
      for v in self.listaVertices:
         caminos.append(float("inf"))
         visitados.append(False)
         verticesAux.append(None)
         if v.getNombre() == origen:
            caminos[self.listaVertices.index(v)] = 0
            verticesAux[self.listaVertices.index(v)] = v.getNombre()
      while not self.todosVisitados(visitados):
         menorAux = self.menorNoVisitado(caminos, visitados)
         if menorAux == None:
            break
         indice = self.listaVertices.index(menorAux)
         visitados[indice] = True
         valorActual = caminos[indice]
         for adyacencia in menorAux.getListaAdyacentes():
            indiceNuevo = self.listaVertices.index(self.obtenerVertice(adyacencia, self.listaVertices))
            arista = self.verificarArista(menorAux.getNombre(), adyacencia)
            if caminos[indiceNuevo] > arista.getPeso():
               caminos[indiceNuevo] = arista.getPeso()
               verticesAux[indiceNuevo] = self.listaVertices[indice].getNombre()
      return caminos
   
   #kruskal
   def kruskal(self):
      aristas = copy(self.listaAristas)
      aristas.sort(key=lambda arista: arista.getPeso())
      aristasMST = []
      verticesAux = []
      for v in self.listaVertices:
         verticesAux.append(v.getNombre())
      for a in aristas:
         if not self.formaCiclo(a, verticesAux):
            aristasMST.append(a)
            verticesAux[self.listaVertices.index(self.obtenerVertice(a.getDestino(), self.listaVertices))] = verticesAux[self.listaVertices.index(self.obtenerVertice(a.getOrigen(), self.listaVertices))]
      return aristasMST
  
   
   # Dijkstra
   def dijkstra(self, origen, destino): 
      verticesAux = [] #lista auxiliar
      verticesD = [] 
      caminos = self.ordenarDijkstra(origen, verticesAux)
      #devuelve una lista que contiene las distancias más cortas desde el origen hasta todos los demás vértices del grafo
      self.rutas(verticesD, verticesAux, destino, origen)
      print(verticesAux)
      aristas = []
      for i in range(len(verticesD)-1):
         aristas.append(self.obtenerArista(verticesD[i],verticesD[i+1], self.listaAristas))
      return aristas

   def ordenarDijkstra(self, origen, verticesAux):
      visitados = []  # lista de visitados
      caminos = []  # recorrido final

      for v in self.listaVertices:  
         caminos.append(float("inf")) #agrega el infinito
         visitados.append(False)
         verticesAux.append(None)
         if v.getNombre() == origen:
            caminos[self.listaVertices.index(v)] = 0
            verticesAux[self.listaVertices.index(v)] = v.getNombre()

      while not self.todosVisitados(visitados):
            menorAux = self.menorNoVisitado(caminos, visitados)  # obtiene el menor no visitado
            if menorAux == None:
               break
            indice = self.listaVertices.index(menorAux)  # indice del menor no marcado
            visitados[indice] = True
            valorActual = caminos[indice]

            for adyacencia in menorAux.getListaAdyacentes():
               indiceNuevo = self.listaVertices.index(self.obtenerVertice(adyacencia, self.listaVertices))
               arista = self.verificarArista(menorAux.getNombre(), adyacencia)
               if caminos[indiceNuevo] > valorActual + arista.getPeso():
                  caminos[indiceNuevo] = valorActual + arista.getPeso()
                  verticesAux[indiceNuevo] = self.listaVertices[indice].getNombre()

      return caminos

   def verificarArista(self, origen, destino):
      for i in range(len(self.listaAristas)):
         if origen == self.listaAristas[i].getOrigen() and destino == self.listaAristas[i].getDestino():
               return self.listaAristas[i]
      return None

   def todosVisitados(self, visitados):
      for vertice in visitados:
         if vertice == False:
            return False

      return True

   def menorNoVisitado(self, caminos, visitados):
      verticeMenor = None
      caminosAux = sorted(caminos)  # organiza de menor a mayor

      copiaCaminos = copy(caminos)
      bandera = True
      cont = 0

      while bandera:
         menor = caminosAux[cont]

         if visitados[copiaCaminos.index(menor)] == False:
            verticeMenor = self.listaVertices[copiaCaminos.index(menor)]
            bandera = False

         else:
            copiaCaminos[copiaCaminos.index(menor)] = "x"
            cont += 1

      return verticeMenor

   def rutas(self, verticesD, verticesAux, destino, origen):
      verticeDestino = self.obtenerVertice(destino, self.listaVertices)
      indice = self.listaVertices.index(verticeDestino)

      if verticesAux[indice] == None:
         print("No hay camino entre: ", (origen, destino))
         return
      aux = destino

      while aux != origen:
         verticeDestino = self.obtenerVertice(aux, self.listaVertices)
         indice = self.listaVertices.index(verticeDestino)
         verticesD.insert(0, aux) #Comienza desde atras hacia delante
         aux = verticesAux[indice]
      verticesD.insert(0, aux)
      
      
   def serializar_objeto(self, objeto):
         if isinstance(objeto,Arista):
            return {
         "origen": objeto.origen, 
         "destino": objeto.destino,
         "distancia": objeto.distancia,
         "tiempo": objeto.tiempo,
         "peso": objeto.peso,
         "Id": objeto.Id
         }
         raise TypeError("El objeto no es una instancia de la clase 'Objeto'.")


   def serializar_objeto2(self, objeto):
      if isinstance(objeto,Vertice):
             return {
            "nombre": objeto.nombre, 
            "x": objeto.x,
            "y": objeto.y
            }
      raise TypeError("El objeto no es una instancia de la clase 'Objeto'.")   

  