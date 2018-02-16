basicUnit = []
neighbors = []

with open("2DU60-05-1.dat",'r') as archivo:
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

with open("basicUnits.dat", 'w') as archivo:
    for i in range(n):
        x,y,a = basicUnit[i]
        print(x,y,a, file = archivo)

with open("instancias.plt",'w') as aristas:
    print("set term png", file = aristas)
    print("set output '2DU60-05-1.png'", file = aristas)
    print("set pointsize 2", file = aristas)
    print("unset arrow", file = aristas)
    print("set style fill transparent solid 0.6",file = aristas)
    print("unset colorbox", file = aristas)
    print("set xrange [0:550]", file = aristas)
    print("set yrange [0:550]", file = aristas)
    # print("set size square", file = aristas)
    # print("set palette model RGB defined ( 0 'red', 1 'green' )", file=aristas)
    num = 1
    for i in range(neigh):
        neigh1, neigh2 = neighbors[i]
        x1, y1,a = basicUnit[neigh1]
        x2, y2,a = basicUnit[neigh2]
        print("set arrow", num, "from", x1, "," ,y1," to ", x2, ",", y2, "nohead", file = aristas)
        num +=1
    print("show arrow", file = aristas)
    print("plot 'basicUnits.dat' using 1:2:(2*sqrt($3-800)) with circles notitle", file = aristas)


        



    
