#Flujo Máximo, Corte Mínimo
# El corte mínimo es el cuello de botella
#Algoritmo de aproximación al corte mínimo, cota superior.
#Iterativamente contrae aristas, los vértices que conecta
#se convierten en uno solo, ese vértice tiene los vecinos
#combinados de los previos, elijo al azar algo para contraer
#contador de multiplicidad a las aristas (representan múltiples aristas)
#hay que ver cuánto pesan las aristas entre los grupos de vértices
#hacemos las contracciones muchas veces para encontrar la cota de corte mínimo
#no elegir al azar, cómo eliges? heurística
#gráfica, óptimo real, repeticiones del algoritmo de aproximación
#comparar cuanto tiempo tarda el ff, y cuántas veces logras repetir con el ff
import time
from grafo6 import Grafo
from random import sample
from copy import deepcopy


g = Grafo() #grafo original
'''
g.aleatorio()
s = sample(g.nodos,1)[0]
t = sample(g.nodos.difference(g.vecinos[s]),1)[0]
'''
k = 30
l = 1
p = 0.001
g.manhattan_aleatorio1(k,l,p)
mf, tm = g.Ford_Fulkerson('0',str((k)**2-1))
print("ff: ", mf)
print("tm: ", tm)
g.status['0'] = 2
g.status[str((k)**2-1)] = 3
#print('t: ',str((k)**2-1))

reps = 400
mincut = 100000
results = [0]*reps
st = time.perf_counter()
for i in range(reps):
    g1 = deepcopy(g)
    while len(g1.nodos) > 2:
        #g1.contraccion_st(s,t)
        g1.contraccion_st()
        #g1.contraccion()
    #print(g1.nodos)
    #print(next(iter(g1.aristas.values()))[0])
    cut = next(iter(g1.aristas.values()))[0]
    if cut < mincut:
        mincut = cut
    results[i] = mincut
    if mincut == mf:
        break

elapsed = time.perf_counter()-st
iters = i
print(mincut)
print(elapsed)

filename = "cuts-k"+str(k)+"-l"+str(l)
with open(filename+".dat",'w') as archivo:
    for i in range(reps):
        print(results[i], file = archivo)
archivo.close()    

with open(filename+".plt",'w') as archivo:
    print("reset", file = archivo)
    print("set term wxt", file = archivo)
    #print("set term epslatex color colortext", file = archivo)
    #print("set output '"+filenamef+".tex' ", file = archivo)
    print("set xrange [-0.005:"+str(iters)+"]",file = archivo)    
    print("set yrange [-0.005:*]",file = archivo)
    print("set xlabel 'número de iteraciones'", file = archivo)
    print("set ylabel 'mejor corte'", file = archivo)
    #print("set ylabel 'tiempo de ejecución'", file = archivo)
    print("set key off", file = archivo)
    print("set pointsize 1", file = archivo)
    print("set arrow 1 from 0,"+str(mf)+" to "+str(iters)+","+str(mf)+"nohead lw 2", file = archivo)
    print("plot '"+filename+".dat' using 1 with linespoints pt 7 lw 2", file = archivo)
archivo.close()

with open("diff_time.dat",'a') as archivo:
    print(k,l,mf,tm,mincut,elapsed,reps, file = archivo)
