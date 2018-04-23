from grafo5 import Grafo
from random import gauss, expovariate
'''
g = Grafo()
g.manhattan_aleatorio()
g.gnuplot("manhattan.png","png", True, True)
x1,y2 = g.posicion['0']
print(x1,y2)

print(g.manh_dist('1','2'))
print(g.Ford_Fulkerson('0','24'))
'''
g = Grafo()
k = 5
g.manhattan_aleatorio1(k,1,0.001)
g.gnuplot("manhattan.png","png", True, True)

g.gnuplot_flow("fmanhattan.png","png", True, True)
#print(g.aristas)
print(g.Ford_Fulkerson('0',str((k)**2-1)))
g.gnuplot_mh("Mmanhattan.png","png", True, True)


