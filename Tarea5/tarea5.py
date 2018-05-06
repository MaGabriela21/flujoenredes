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
k = 30
l = 3
p = 0.0001
repetitions = 2
quitados = 5
#mf = dict() #maximum flow
#mf_time = dict()
acut = dict()
a = (k**2)*(k**2-1)
'''
for i in range(a):
    mf[i] = set()
    mf_time[i] = set()
'''
for i in range(repetitions):
    ii = i
    #filename = "results-k"+str(k)+"-l"+str(l)+"-p"+str(p)+"-q"+str(quitados)+".txt"
    filename = str(i)+"results-k"+str(k)+"-l"+str(l)+"-p"+str(p)+".txt"
    with open(filename, 'w') as results:
        g.manhattan_aleatorio(k,l,p)
        m, time = g.Ford_Fulkerson('0',str((k)**2-1))
        init_m = m #initial maxflow
        #mf[0].add(m)
        #mf_time[0].add(time)
        print(0," ",1," ",time, file = results)
        j = 1
        while m >0 : ##FF da resultados menor a uno por alguna razón... 
            for q in range(quitados):
                '''
                found = False #if an existing edge was found
                while not found:
                    u = randint(0,(k)**2-1)
                    u = str(u)
                    if len(g.vecinos[u])>0:
                        found = True
                v = sample(g.vecinos[u],1)[0]
                g.quitar_arista(u,v)
                '''
                u = sample(g.nodos,1)[0]
                u = str(u)
                g.quitar_nodo(u)
            #print("j = ",j,"quité",u,", ",v)
            m, time = g.Ford_Fulkerson('0',str((k)**2-1))
            m = m/init_m 
            #mf[j].add(m)
            #mf_time[j].add(time)
            print(j*quitados," ",m," ",time, file = results)
            j = j+1
    acut[i] = j-1
    results.close()
    print("maxflow:",init_m)
        #print("aristas que quité: ",j)

g.gnuplot_mh("manhattan.png","png", True, True)
g.gnuplot("1manhattan.png","png", True, True)


#Results!!
for i in range(repetitions):
        print(acut[i])
filename = "k"+str(k)+"-l"+str(l)+"-p"+str(p)+".dat"
with open(filename, 'w') as resultsf:
    for i in range(repetitions):
        print(acut[i], file = resultsf)







