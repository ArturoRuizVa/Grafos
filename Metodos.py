# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=trailing-newlines
# pylint: disable=trailing-whitespace
# pylint: disable=missing-final-newline
import random
import math

from Grafos import Grafo



def Erdos(n,m):
    """
    Metodo de Erdos
    n nodos y m aristas aleatorios
    """
    graf=Grafo()#se crea un grafo vacío
    for i in range(n):#Se añaden nodos hasta alcanzar n
        graf.addnode(str(i))
    
    for i in range(m):#Se agrega un arista entre 2 nodos aleatorios distintos
        u=random.randint(0, n-1)
        v=random.randint(0, n-1)
        if u != v:
            graf.addedge(str(u) + '->' +  str(v),  str(u),
                       str(v))

    return graf

def Gilbert(n, p):
    """
    Método Gilbert
    n nodos
    Cada arista posible puede existir con probabilidad p"""
    graf = Grafo()

    for i in range(n):#Se añaden nodos hasta alcanzar n
        graf.addnode(str(i))

    for i in range(n):
        for j in range(n):
            if random.random() < p:
                if (j != i):
                    graf.addedge(str(i) + '->' + str(j), str(i),str(j))
    return graf

def Geografico(n, r):
    """
    Método Geográfico
    Para n nodos se crean las aristas donde los nodos esten a una destacncia menor o igual a r (entre 0 y 1)
    """
    graf = Grafo()

    # Generar n nodos con coordenadas en el espacio ((0,0),(1,1))
    for i in range(n):
        node = graf.addnode(str(i))
        node.xposition = random.random()
        node.yposition = random.random()

    # Crear una arista entre cada par de nodos que están a distancia <= r
    for i in range(n):
        for j in range(n):
            if i != j:
                d = math.sqrt((graf.getnode(str(i)).xposition - graf.getnode(str(j)).yposition) ** 2 + (graf.getnode(str(i)).xposition - graf.getnode(str(j)).yposition) ** 2)
                if d <= r:
                    graf.addedge(str(i) + '->' + str(j), str(i),str(j))

    return graf

def Barabasi(n, d):
    """
    Método Barabasi
    para n nodos se crean d o menos aristas
    """
    graf = Grafo()
    

    for i in range(n):
        graf.addnode(str(i))
        for j in range(n):
            deg = graf.getdegree(str(j))
            p = 1 - deg / d
            if random.random() < p:
                if j != i:
                    graf.addedge( str(i) + '->' + str(j), str(i), str(j))

    return graf

grafo=Erdos(30,10)
grafo.save('Erdos_30_10.gv')
grafo=Erdos(100,10)
grafo.save('Erdos_100_10.gv')
grafo=Erdos(500,10)
grafo.save('Erdos_500_10.gv')
grafo=Gilbert(30,0.5)
grafo.save('Gilbert_30_0.5.gv')
grafo=Gilbert(100,0.5)
grafo.save('Gilbert_100_0.5.gv')
grafo=Gilbert(500,0.3)
grafo.save('Gilbert_500_0.3.gv')
grafo=Geografico(30,0.5)
grafo.save('Geografico_30_0.5.gv')
grafo=Geografico(100,0.4)
grafo.save('Geografico_100_0.4.gv')
grafo=Geografico(500,0.4)
grafo.save('Geografico_500_0.4.gv')
grafo=Barabasi(30,5)
grafo.save('Barabasi_30_5.gv')
grafo=Barabasi(100,4)
grafo.save('Barabasi_100_4.gv')
grafo=Barabasi(500,3)
grafo.save('Barabasi_500_3.gv')
