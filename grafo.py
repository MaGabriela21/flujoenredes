class Nodo:
    def __init__(self, tamaño = 1, posicion = (0,0), color = 0):
        self.tamaño = tamaño
        self.posicion = posicion
        self.color = color
        self.vecinos = set()

class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = dict()
        self.vecinos = dict()
        self.tamano = dict()
        self.color = dict()
        self.posicion = dict()
    def agrega(self, v,tamano = 1, posicion = (0,0), color = 0):
        self.nodos.add(v)
        self.tamano[v] = tamano
        self.posicion[v] = posicion
        self.color[v] = color
        if not v in self.vecinos:
            self.vecinos[v] = set()
            
    def conecta(self, v, u, peso=1, dirigido = False, tipo = 1):
        if not v in self.nodos:
            self.agrega(v)
        if not u in self.nodos:
            self.agrega(u)
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
        if dirigido:
            self.aristas[(u, v)] = (peso, tipo, dirigido) # en ambos sentidos
        else:
            self.aristas[(v, u)] = self.aristas[(u, v)] = (peso, tipo, dirigido)  # en ambos sentidos

        
    def complemento(self):
        comp= Grafo()
        for v in self.nodos:
            for w in self.nodos:
                if v != w and (v, w) not in self.aristas:
                    comp.conecta(v, w, 1)
        return comp
    def aleatorio(self, n=10, prob = 0.5, dirigido = False, rand_style_aristas = False):
        from random import random
        for i in range(n):
            tag_nodo = str(i)
            x = random()
            y = random()
            size = random()
            color = random()
            self.agrega(tag_nodo, size, (x,y),color)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if random() < prob:
                    if rand_style_aristas:
                        atipo = int(10*random()) % 5
                        peso = 3*random()
                    else:
                        atipo = 1
                        peso = 1
                    self.conecta(str(i),str(j),peso, dirigido,atipo)
    def leer(self, filename = "2DU80-05-2.dat"):
        with open(filename, 'r') as archivo:
            nn = int(archivo.readline())
            for i in range(nn):
                stringLine = archivo.readline()
                splitLine = stringLine.split(" ")
                valueList = [float(e) for e in splitLine]
                index, x, y, a, b, c = valueList
                index = int(index)
                idx = str(index)                
                #print(idx)
                a = pow((a - 590),3)
                self.agrega(idx, a, (x,y), 1)
            neigh = int(archivo.readline())
            for i in range(neigh):
                stringLine = archivo.readline()
                splitLine = stringLine.split(" ")
                neigh1, neigh2 = splitLine
                neigh2, basura = neigh2.split("\n")
                self.conecta(neigh1,neigh2,1)
        archivo.close()
    def gnuplot(self, gcolor = True, gtamano = True, name = "grafo_a"):
        n = len(self.nodos)
        with open("nodos.dat",'w') as archivo_nodos:
            for nodo in self.nodos:
                #nodo = str(i)
                (x,y) = self.posicion[nodo]
                size = self.tamano[nodo]
                color = self.color[nodo]
                print(x, y,size,color, file = archivo_nodos)
        filename = name + ".plt"
        imagename = " '"+ name + ".png' "
        arrow_idx = 1
        archivo_nodos.close()
        with open(filename, 'w') as archivo:
            print("set term png", file = archivo)
            print("set output"+imagename, file = archivo)
            print("set pointsize 2", file = archivo)
            print("unset arrow", file = archivo)
            print("unset colorbox", file = archivo)
            for (ii,jj) in self.aristas:
                (x1, y1) = self.posicion[ii]
                (x2, y2) = self.posicion[jj]
                (apeso, atipo, adirected) = self.aristas[(ii,jj)]
                head = "nohead"
                if adirected:
                    head = "head"
                print("set arrow", arrow_idx, "from", x1, "," ,y1," to ", x2, ",", y2, head, " lw ",apeso, " dashtype ", atipo, file = archivo)
                arrow_idx += 1
            #print("set style fill transparent solid 0.7", file = archivo)
            print("set style fill solid", file = archivo)
            print("set palette defined (0 'blue', 3 'green', 6 'yellow', 10 'red') ", file = archivo)
            if gcolor and gtamano:
                print("color y tamaño!!")
                print("plot 'nodos.dat' using 1:2:(sqrt($3)/30):4 with circles palette notitle", file = archivo)
            elif gcolor:
                print("sin tamaño!!")
                print("plot 'nodos.dat' using 1:2:3 with points pt 7 palette notitle", file = archivo)
            elif gtamano:
                print("sin color!!")
                print("plot 'nodos.dat' using 1:2:(sqrt($3)/30) with circles notitle", file = archivo)
            else:
                print("sin color sin tamaño!!")
                print("plot 'nodos.dat' using 1:2 with points pt 7 lc rgb 'blue' notitle", file = archivo)
                
            archivo.close()

                        
                    
            
            
            
        
                
                
            
    
    
        
    
    
        
    
    
