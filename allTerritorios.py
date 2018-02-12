nfiles = 20
with open("terr.plt",'w') as aristas:
        print("set term png", file = aristas)

for file in range(nfiles):
    sfile = str(file+1)
    filename = "2DU60-05-" + sfile + ".dat"
    imagename = " '2DU60-05-" + sfile + ".png' "
    BU_file = sfile + "basicUnits.dat"

    basicUnit = []
    neighbors = []

    with open(filename,'r') as archivo:
        n = int(archivo.readline())
        for i in range(n):
            stringLine = archivo.readline()
            splitLine = stringLine.split(" ")
            valueList = [float(e) for e in splitLine]
            index, x, y, a, b, c = valueList
            basicUnit.append((x,y))
        neigh = int(archivo.readline())
        for i in range(neigh):
            stringLine = archivo.readline()
            splitLine = stringLine.split(" ")
            valueList = [int(e) for e in splitLine]
            neigh1, neigh2 = valueList
            neighbors.append((neigh1,neigh2))

    with open(BU_file, 'w') as archivo:
        for i in range(n):
            x,y = basicUnit[i]
            print(x,y, file = archivo)

    with open("terr.plt",'a') as aristas:
        print("set output" + imagename, file = aristas)
        print("set pointsize 1", file = aristas)
        print("set size square", file = aristas)
        # print("set size square", file = aristas)
        # print("set palette model RGB defined ( 0 'red', 1 'green' )", file=aristas)
        num = 1
        for i in range(neigh):
            neigh1, neigh2 = neighbors[i]
            x1, y1 = basicUnit[neigh1]
            x2, y2 = basicUnit[neigh2]
            print("set arrow", num, "from", x1, "," ,y1," to ", x2, ",", y2, "nohead", file = aristas)
            num +=1
        print("show arrow", file = aristas)
        print("plot '"+ BU_file +" ' using 1:2 with points pt 7", file = aristas)
        print("unset arrow", file = aristas)
        print("unset output", file = aristas)

        



    
