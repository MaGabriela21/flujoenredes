n = 20
p = 0.15

from random import random

nodos = []
with open("nodos.dat",'w') as archivo:
    for i in range(n):
        x = random()
        y = random()
        #size= random()
        #color = random()
        nodos.append((x,y))
        print(x, y, file = archivo)
        #print(x, y,size, color, file = archivo)
archivo.close()

with open("aristas.dat",'w') as aristas:
    for i in range(n - 1):
        (x1, y1) = nodos[i] 
        for j in range(i + 1, n):
            (x2, y2) = nodos[j] 
            if random() < p:
                print(i, j, file = aristas)
