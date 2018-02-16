n = 80
p = 4
center = []

basicUnit = []
neighbors = []
territory = []
terr = [None]*n
BU_file = "psol80-05-2.dat"

with open("2DU80-05-2.dat",'r') as archivo:
        n = int(archivo.readline())
        for i in range(n):
            stringLine = archivo.readline()
            splitLine = stringLine.split(" ")
            valueList = [float(e) for e in splitLine]
            index, x, y, a, b, c = valueList
            basicUnit.append((x,y,a))
        neigh = int(archivo.readline())
        for i in range(neigh):
            stringLine = archivo.readline()
            splitLine = stringLine.split(" ")
            valueList = [int(e) for e in splitLine]
            neigh1, neigh2 = valueList
            neighbors.append((neigh1,neigh2))

archivo.close()
            
with open("sol80-05-2.txt",'r') as solucion:
    for i in range(p):
        c = int(solucion.readline())
        center.append(c)
    for i in range(p):
        string_terr = solucion.readline()
        splitLine = string_terr.split(" ")
        splitLine = splitLine[0:(len(splitLine)-1)]
        valueList = [int(e) for e in splitLine]
        territory.append(valueList)
        for j in range(len(splitLine)):
            idx = valueList[j]
            #print(idx)
            terr[idx-1]= i+1
solucion.close()
        

with open("psol80-05-2.dat",'w') as psolucion:    
    for i in range(n):
        x,y,size= basicUnit[i]
        print(x,y,size,terr[i], file = psolucion)
psolucion.close()

with open("solution.plt",'a') as aristas:
        print("set term png", file = aristas)
        print("set output 'psol.png' ", file = aristas)
        print("set pointsize 1", file = aristas)
        print("set size square", file = aristas)
        print("set style fill transparent solid 0.8", file = aristas)
        print("set palette defined (0 'blue', 3 'green', 6 'yellow', 10 'red') ", file = aristas)
        print("unset colorbox", file = aristas)
        num = 1
        for i in range(neigh):
            neigh1, neigh2 = neighbors[i]
            x1, y1, s1 = basicUnit[neigh1]
            x2, y2, s2 = basicUnit[neigh2]
            print("set arrow", num, "from", x1, "," ,y1," to ", x2, ",", y2, "nohead", file = aristas)
            num +=1
        #print("show arrow", file = aristas)
        #print("plot '"+ BU_file +" ' using 1:2 with points pt 7", file = aristas)
        print("plot 'psol80-05-2.dat' using 1:2:(2*sqrt($3-600)):4 with circles palette notitle", file = aristas)
        print("unset arrow", file = aristas)
        print("unset output", file = aristas)
aristas.close()
