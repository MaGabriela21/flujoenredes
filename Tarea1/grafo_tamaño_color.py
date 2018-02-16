n = 20
p = 0.15

from random import random

nodos = []
with open("nodos.dat",'w') as archivo_nodos:
    for i in range(n):
        x = random()
        y = random()
        size= random()
        color = random()
        nodos.append((x,y))
        #print(x, y, file = archivo)
        print(x, y,color, file = archivo_nodos)
        #print(x, y,size,color, file = archivo_nodos)

with open("grafo_color.plt",'w') as archivo:
    print("set term png", file = archivo)
    print("set output 'grafo_color.png'", file = archivo)
    print("set pointsize 2", file = archivo)
    print("unset arrow", file = archivo)
    print("unset colorbox", file = archivo)
    # print("set size square", file = archivo)
    num = 1
    for i in range(n - 1):
        (x1, y1) = nodos[i] 
        for j in range(i + 1, n):
            (x2, y2) = nodos[j] 
            if random() < p:
                print("set arrow", num, "from", x1, "," ,y1," to ", x2, ",", y2, "nohead", file = archivo)
                num += 1
    print("show arrow", file = archivo)
    print("set style fill solid", file = archivo)
    #print("set palette defined (0 'blue', 3 'green', 6 'yellow', 10 'red') ", file = archivo)
    #print("plot 'nodos.dat' using 1:2:(sqrt($3)/30) with circles", file = archivo)
    print("plot 'nodos.dat' using 1:2:3 with points pt 7 palette", file = archivo)
    #print("plot 'nodos.dat' using 1:2:(sqrt($3)/30):4 with circles palette notitle", file = archivo)


