##n = kxk
# dos tipos de aristas
#l: umbral de distancia de manhatann l o menos: no se puede mover en diagonal,
#k, enteros visualizacion: 7, pero intentemos 30, y una máxima
#l: menor a k, 1,2,3,4 aumenta la densidad 
#valor absoluto de diferencia de filas, y columnas
#distancia:  subrutina
#p: agregar arista dirigida, muy pequeña para que sean wormholes,
#verificar el número de aristas que se generaron así, no uniformemente al azar
#necesariamente, distancias más lejanas
#redes sociales
#s superior izq, t infder
#capacidades a las aristas, flujo, con distribución normal valores enteros,
#elegir una media y una desviación, sin negativos y sin ceros
#para las capacidades de largo alcance, distribución exponencial (buscar paquetes en python!)
#mostrar capacidades en el grafo!
#primero generador de estos grafos y que los grafique
#Percolación de vértices y de aristas, quitarle aristas al azar
#efectos en el flujo máximo FF!!!, y ejecución del algoritmo!
#dejas de quitar aristas cuando t ya no es alcanzable
#desde s
#quitar nodo con sus aristas
#visualizar el flujo.... plus

##resultados para mostrar:
#variar k, l y p
#opcionalmente variar: mu, sigma, lambda
#percolación: analizar cómo varía max_flow y tiempo de ff
#quitar vértices, quitar aristas, repetir secuencias!!
#que tanto afecta la primera, la segunda y asi en una grafiquita
#cuántas se pueden quitar??
#opcional: mostrar el flujo en el grafo

from grafo5 import Grafo
from random import random, gauss, expovariate, sample, randint
'''
g = Grafo()
g.manhattan_aleatorio()
g.gnuplot("manhattan.png","png", True, True)
x1,y2 = g.posicion['0']
print(x1,y2)

print(g.manh_dist('1','2'))
print(g.Ford_Fulkerson('0','24'))

g = Grafo()
k = 3
g.manhattan_aleatorio1(k,1,0.001)
g.gnuplot("manhattan.png","png", True, True)
print(g.Ford_Fulkerson('0',str((k)**2-1)))
g.gnuplot_mh("Mmanhattan.png","png", True, True)


print(g.vecinos['1'])
g.quitar_arista('1','2')
print(g.vecinos['1'])
g.quitar_arista('2','1')
g.quitar_nodo('3')
print(g.vecinos['0'])
print(g.nodos)
print(g.Ford_Fulkerson('0',str((k)**2-1)))
g.gnuplot_mh("9manhattan.png","png", True, True)
'''


g = Grafo()
k = 5
p = 0.001
mf = dict()
mf_time = dict()
acut = dict()
a = (k**2)*(k**2-1)
for i in range(a):
    mf[i] = set()
    mf_time[i] = set()
for i in range(10):
    g.manhattan_aleatorio(k,1,p)
    m, time = g.Ford_Fulkerson('0',str((k)**2-1))
    mf[0].add(m)
    mf_time[0].add(time)
    j = 1
    while m > 0 :
        found = False
        while not found:
            u = randint(0,(k)**2-1)
            u = str(u)
            if len(g.vecinos[u])>0:
                found = True
        v = sample(g.vecinos[u],1)[0]
        g.quitar_arista(u,v)
        #print("j = ",j,"quité",u,", ",v)
        m, time = g.Ford_Fulkerson('0',str((k)**2-1))
        mf[j].add(m)
        mf_time[j].add(time)
        j = j+1
    acut[i] = j
    #print("aristas que quité: ",j)
        
g.gnuplot_mh("manhattan.png","png", True, True)
g.gnuplot("1manhattan.png","png", True, True)

#Results!!







