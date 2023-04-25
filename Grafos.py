
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=trailing-newlines
# pylint: disable=trailing-whitespace
# pylint: disable=missing-final-newline
import threading
import math
import random


lock = threading.Lock()#bloqueo de procesos multiples

class Grafo:  
    def __init__ (self):#Inicializador de la clase grafo 
        #atributos del objeto grafo (nombre, nodos y aristas)      
        self.id='Grafo'#identificación del grafo
        self.nodes={}
        self.edges={}
    
    def addnode (self,name):#Operación añadir nodo
        node = self.nodes.get(name)#Se busca un nodo con  el mismos nombree en el grafo

        if node is None:# si aun no existe un nodo con ese nombre se añade 
            node = Node(name)#se inicia un nodo con el nombre propuesto

            with lock:#Se añade el nodo con un bloqueo para evitar procesos multiples
                self.nodes[name] = node

        return node  
    
    def addedge(self,name,node1,node2):#Procedimiento para añadir un arista
        """
        Se repite un procedimiento similar al realizado para añadir un nodo
        
        """
        edge = self.edges.get(name)

        if edge is None:
            n0 = self.addnode(node1)
            n1 = self.addnode(node2)
            edge = Edge(n0, n1, name)

            with lock:
                self.edges[name] = edge
            n0.adyacencias.append(n1)#se agregan ambos nodos a la lista de adyacencias del otro
            n1.adyacencias.append(n0)

        return edge
    
    def getnode(self, name):
        """
        Se busca un nodo específico en el grafo
        """
        return self.nodes.get(name)
    
    def getdegree(self, name):
        """
        Obtiene el grado del nodo en cuestion
        """
        n = self.getnode(name)
        if n is None:
            return 0

        return len(n.adyacencias)#mide la longitud del vector de adyacencias
    

    def graphGV(self):
        """ 
        Escritura del grafo para Gephi
        """
        retVal = 'digraph X {\n'
        for e in self.edges.values():
            n0 = e.n0.idnode
            n1 = e.n1.idnode
            retVal += n0 + ' -> ' + n1 + ';\n'
        retVal += '}\n'

        return retVal
    
    def save(self, archivo):
        """
        Guarda el grafo en un archivo gv
        """
        gv = self.graphGV()
        f = open(archivo, 'w+')
        f.write(gv)
        print('Archivo', archivo, 'guardado con', len(self.nodes), 'nodos y', len(self.edges), 'aristas')

class Edge:
    """
    Clase arista
    """
    def __init__(self, source, target, idedge):
        """
        Parámetros: Origen, Destino y nombre
        """
        self.n0 = source
        self.n1 = target
        self.idedge = idedge

class Node:
    """
    Clase Nodo
    """

    def __init__(self, idnode):
        """
        Parametros: Nombre, Coordenadas y Adyacencias
        """
        self.idnode = idnode
        self.xposition= random.random()
        self.yposition= random.random()
        self.adyacencias=[]