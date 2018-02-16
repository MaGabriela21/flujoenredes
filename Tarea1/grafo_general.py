n = 20
p = 0.15

from random import random

nodos = []
with open("nodos.dat",'w') as archivo:
    for i in range(n):
        x = random()
        y = random()
        nodos.append((x,y))
        print(x, y, file = archivo)


with open("grafo_general.plt",'w') as aristas:
    print("set term png", file = aristas)
    print("set output 'grafo.png'", file = aristas)
    print("set pointsize 2", file = aristas)
     print("unset arrow", file = aristas)

    num = 1
    for i in range(n - 1):
        (x1, y1) = nodos[i] 
        for j in range(i + 1, n):
            (x2, y2) = nodos[j] 
            if random() < p:
                print("set arrow", num, "from", x1, "," ,y1," to ", x2, ",", y2, "nohead", file = aristas)
                num += 1
    #print("show arrow", file = aristas)
    print("plot 'nodos.dat' with points pt 7", file = aristas)


