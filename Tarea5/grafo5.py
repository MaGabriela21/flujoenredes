from math import sqrt, factorial, cos, sin, pi
from random import random, gauss, expovariate
import time

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
            
    def conecta(self, u, v,  peso=0, dirigido = False, tipo = 1):
        if not v in self.nodos:
            self.agrega(v)
        if not u in self.nodos:
            self.agrega(u)
        self.vecinos[u].add(v)
        if peso == 0:
            (x1, y1) = self.posicion[v]
            (x2, y2) = self.posicion[u]
            peso = sqrt((x1 - x2)**2 + (y1-y2)**2) #peso igual a distancia!! 
        if dirigido:
            self.aristas[(u, v)] = (peso, tipo, dirigido) # en solo un sentido
        else:
            self.aristas[(v, u)] = self.aristas[(u, v)] = (peso, tipo, dirigido)  # en ambos sentidos
            self.vecinos[v].add(u)
    def quitar_arista(self, u,v):
        p,t,d =self.aristas.pop((u,v))
        self.vecinos[u].remove(v)
        if not d:
            self.vecinos[v].remove(u)
    def quitar_nodo(self, u):
        vecindad = self.vecinos[u].copy()
        for i in vecindad:
            print("quité arista con",i)
            self.quitar_arista(u,i)
        for n in self.nodos:
            if u in self.vecinos[n]:
                print("uy quité arista con",n)
                self.quitar_arista(n,u)
        self.nodos.remove(u)
    def complemento(self):
        comp= Grafo()
        for v in self.nodos:
            for w in self.nodos:
                if v != w and (v, w) not in self.aristas:
                    comp.conecta(v, w, 1)
        return comp
    def aleatorio(self, n=10, prob = 0.5, dirigido = False, rand_peso = False, rand_style_aristas = False):
        from random import random
        for i in range(n):
            tag_nodo = str(i)
            x = random()
            y = random()
            size = random()
            color = random()
            self.agrega(tag_nodo, size, (x,y),color)
        for i in range(n - 1):
            if dirigido:
                inicio = 1
            else:
                inicio = i+1
            for j in range(inicio, n):
                if random() < prob and i!=j:
                    if rand_peso:
                        peso = int(10*random()+1)
                    else:
                        peso = 1
                    if rand_style_aristas:
                        atipo = int(10*random()) % 5
                    else:
                        atipo = 1
                    self.conecta(str(i),str(j),peso, dirigido,atipo)
    def circ_aleatorio(self, n=10, prob = 0.5,x0 =0.5, y0 = 0.5, dirigido = False, rand_peso = False, rand_style_aristas = True):
        from random import random
        for i in range(n):
            tag_nodo = str(i)
            x = x0 + 0.5*cos(2*pi*i/n)
            y = y0 + 0.5*sin(2*pi*i/n)
            size = random()
            color = random()
            self.agrega(tag_nodo, size, (x,y),color)
        for i in range(n - 1):
            if dirigido:
                inicio = 1
            else:
                inicio = i+1
            for j in range(inicio, n):
                if random() < prob and i!=j:
                    if rand_peso:
                        peso = int(10*random()+1)
                    else:
                        peso = 1
                    if rand_style_aristas:
                        atipo = int(10*random()) % 5
                    else:
                        atipo = 1
                    self.conecta(str(i),str(j),peso, dirigido,atipo)
    def kcirc_aleatorio(self, n=10, k = 3,prob = 0.5,x0 =0.5, y0 = 0.5, dirigido = False, rand_peso = False, rand_style_aristas = False):
        from random import random
        peso = 1
        atipo = 1
        for i in range(n):
            tag_nodo = str(i)
            x = x0 + 0.5*cos(2*pi*i/n)
            y = y0 + 0.5*sin(2*pi*i/n)
            size = random()
            color = random()
            self.agrega(tag_nodo, size, (x,y),color)
        for i in range(n):
            for j in range(k):
                jj = (i+j+1)%n            
                self.conecta(str(i),str(jj),peso, dirigido,atipo)
               
        for i in range(n-1):
            for j in range(n-2*k-1):
                jj = (i+j+k+1)%n
                if random() < prob:
                    peso = 1
                    self.conecta(str(i),str(jj),peso, dirigido,atipo)

    def manhattan_aleatorio(self, k = 5, l = 1, p = 0.001):
        nodo = 0
        wormholes = 0
        mu = 20
        sigma = 10
        lmbd = 5
        for i in range(k):
            for j in range(k):  
                name = str(nodo)
                #x = i/k
                #y = 1 -j/k
                x = i 
                y = k - j 
                self.agrega(name,1,(x,y),1)
                nodo = nodo+1  
        self.color['0'] = 2
        self.color[name] = 3
        #conecciones l
        for i in range(k**2-1):
            for j in range(i+1,k**2):
                if (self.manh_dist(str(i),str(j)) <= l):
                    lpeso = gauss(mu,sigma)
                    lpeso = abs(int(lpeso))+1
                    #print(lpeso)
                    self.conecta(str(i),str(j),lpeso,True,1)
                    self.conecta(str(j),str(i),lpeso,True,1)
                elif (random() < p) :
                    #print(i,',',j)
                    wormholes = wormholes+1
                    ppeso = expovariate(lmbd)*mu/4
                    ppeso = abs(int(ppeso))+1
                    #print("pp: ",ppeso)
                    self.conecta(str(i),str(j),ppeso,True,2)
                elif (random() < p) :
                    #print(j,',',i)
                    wormholes = wormholes+1
                    ppeso = expovariate(lmbd)*mu/4
                    ppeso = abs(int(ppeso))+1
                    #print("pp: ",ppeso)
                    self.conecta(str(j),str(i),ppeso,True,2)
        print('wormholes: ',wormholes)

    def manhattan_aleatorio1(self, k = 5, l = 1, p = 0.001):
        nodo = 0
        wormholes = 0
        for i in range(k):
            for j in range(k):  
                name = str(nodo)
                #x = i/k
                #y = 1 -j/k
                x = i 
                y = k - j 
                self.agrega(name,1,(x,y),1)
                nodo = nodo+1  
        self.color['0'] = 2
        self.color[name] = 3
        #conecciones l
        for i in range(k**2-1):
            for j in range(i+1,k**2):
                if (self.manh_dist(str(i),str(j)) <= l):
                    lpeso = 1
                    #print(lpeso)
                    self.conecta(str(i),str(j),lpeso,True,2)
                    self.conecta(str(j),str(i),lpeso,True,2)
                elif (random() < p) :
                    print(i,',',j)
                    wormholes = wormholes+1
                    ppeso = 0.5
                    self.conecta(str(i),str(j),ppeso,True,1)
                elif (random() < p) :
                    print(j,',',i)
                    wormholes = wormholes+1
                    ppeso =  0.2
                    self.conecta(str(j),str(i),ppeso,True,1)
        print('wormholes: ',wormholes)
        
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

    def manh_dist(self, a,b):
        md = 0
        x1, y1 = self.posicion[a]
        x2, y2 = self.posicion[b]
        md = abs(x1-x2) + abs(y2-y1) 
        return md
    def Floyd_Warshal(self):
        #start_FW = time.time()
        start_FW = time.perf_counter()
        d = dict() #diccionario de distancias
        for n in self.nodos:
            d[(n,n)] = 0
            for v in self.vecinos[n]:
                (p,vv,t) = self.aristas[(n,v)]
                d[(n,v)] = p
                #print(n,v,p)
        for intermedio in self.nodos:
            for desde in self.nodos:
                for hasta in self.nodos:
                    di = None
                    if (desde, intermedio) in d:
                        di = d[(desde,intermedio)]
                    ih = None
                    if (intermedio, hasta) in d:
                        ih = d[(intermedio, hasta)]
                    if di is not None and ih is not None:
                        c = di + ih
                        if (desde, hasta) not in d or c < d[(desde, hasta)]:
                            d[(desde, hasta)] = c
        #print('time Floyd Warshal', time.time()-start_FW)
        #elapsed_FW = time.time()-start_FW
        elapsed_FW = time.perf_counter()-start_FW
        return d, elapsed_FW
    def camino(self,s,t,ff):
        cola = [s]
        usados = set()
        camino = dict()
        while len(cola)>0:
            u = cola.pop(0)
            usados.add(u)
            for (w,v) in self.aristas:
                if w == u and v not in cola and v not in usados:
                    actual = ff.get((u,v), 0)
                    #print("actual: ",actual)
                    peso, d, f = self.aristas[(u,v)]
                    #print("peso: ", peso)
                    dif = peso - actual
                    if  dif > 0:
                        cola.append(v)
                        camino[v] = (u,dif)
        if t in usados:
            return camino
        else: #no se alcanzó
            return None
        
    def Ford_Fulkerson(self,s,t):
        start_FF = time.perf_counter()
        if s == t: 
            return 0
        maximo = 0
        f = dict()
        while True:
            aum = self.camino(s,t,f)
            if aum is None:
                #print("No hay camino")
                break #ya no hay
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            #print("incremento!: ",incr)
            u = t
            while u in aum:
                v = aum[u][0]
                #print("u,v:", u,v)
                actual = f.get((v,u), 0) #cero si no hay
                inverso = f.get((u,v), 0)
                #print("actual, incr", actual, incr)
                f[(v,u)] = actual + incr
                f[(u,v)] = inverso - incr
                u = v
            maximo += incr
            #print('maximo hasta ahora:',maximo)
            #print('camino',aum)
            #print('f',f)
        #print('time Ford Fulkerson: ', time.perf_counter()-start_FF)
        elapsed_FF = time.perf_counter()-start_FF
        for i in self.aristas:
            peso, tipo, dirg = self.aristas[i]
            self.aristas[i] = (peso,1,dirg)
        for i in f:
            if f[i] > 0:
                peso, tipo, dirg = self.aristas[i]
                self.aristas[i] = (peso,3,dirg)
        return maximo, elapsed_FF
    
    def dfs(self, origen, visitado = None):
        start_dfs = time.perf_counter()
        first = False
        if visitado is None:
            first = True
            visitado = set()
        if origen not in visitado:
            #print(origen)
            visitado.add(origen)
        for siguiente in self.vecinos[origen]-visitado:
            self.dfs(siguiente,visitado)
        elapsed_dfs = time.perf_counter()-start_dfs
        if first: print(elapsed_dfs)
        return visitado
    def bfs(self, origen):
        start_bfs = time.perf_counter()
        visitado = set()
        visitado.add(origen)
        level = set()
        level.add(origen)
        nextlevel = set()
        while len(level)>0:
            for i in level:
                for j in self.vecinos[i]:
                    if j not in visitado:
                        nextlevel.add(j)
                        #print(j)
                        visitado.add(j)
            level = nextlevel
            nextlevel = set()
        elapsed_bfs = time.perf_counter()-start_bfs
        print(elapsed_bfs)
        return visitado           

    def avg_dist(self):
        d, t_fw = self.Floyd_Warshal()
        s = 0
        for i in d.keys():
            s = s+ d[i]
        a = s/(len(self.nodos)**2)
        return a
    def clust_coef(self):
        delta = dict()
        for i in self.nodos:
            m = 0
            n = len(self.vecinos[i])
            #print(n)
            if n <= 2:
                delta[i]= 0
            else:
                m_max = factorial(n) / (2*factorial(n-2))
                for j in self.vecinos[i]:
                    for k in self.vecinos[j]:
                        if k in self.vecinos[i]:
                            m = m+1
                m = m/2
                delta[i] = m/m_max
        s = 0
        for i in delta.keys():
            s = s+ delta[i]
        c = s/len(self.nodos)
        return c

                
    def gnuplot(self,name = "grafo.png",term = "png", gcolor = False, gtamano = False):
        n = len(self.nodos)
        with open("nodos.dat",'w') as archivo_nodos:
            for nodo in self.nodos:
                #nodo = str(i)
                (x,y) = self.posicion[nodo]
                size = self.tamano[nodo]
                color = self.color[nodo]
                print(x, y,size,color, file = archivo_nodos)
        split = name.split(".")
        filename = split[0] + ".plt"
        arrow_idx = 1
        archivo_nodos.close()
        max_x = 5
        min_x = 0
        max_y = 5
        min_y = 0
        axis_border = 0.05
        edge_weight = 0.5
        with open(filename, 'w') as archivo:
            print("set term "+term, file = archivo)
            print("set output '"+name+"'", file = archivo)
            print("set pointsize 1", file = archivo)
            print("unset label", file = archivo)
            print("unset arrow", file = archivo)
            print("unset colorbox", file = archivo)
            print("set size square", file = archivo)
            for (ii,jj) in self.aristas:
                (x1, y1) = self.posicion[ii]
                (x2, y2) = self.posicion[jj]
                if x1<min_x: min_x = x1
                if x2<min_x: min_x = x2
                if y1<min_y: min_y = y1
                if y2<min_y: min_y = y2
                if x1>max_x: max_x = x1
                if x2>max_x: max_x = x2
                if y1>max_y: max_y = y1
                #print("set label '" + str(ii) + "' at ",x1+ axis_border,"," ,y1+0.05, " left offset char -0.4,0", file = archivo) # https://stackoverflow.com/questions/23690551/how-do-you-assign-a-label-when-using-set-object-circle-in-gnuplot
                #print("set label '" + str(jj) + "' at " ,x2+axis_border, "," ,y2+0.05, " left offset char -0.4,0", file = archivo)
                (apeso, atipo, adirected) = self.aristas[(ii,jj)]
                apeso = apeso*edge_weight
                head = "nohead"
                if adirected:
                    head = "head"
                print("set arrow", arrow_idx, "from", x1, "," ,y1," to ", x2, ",", y2, head, "filled lw ",apeso, " dashtype ", atipo, file = archivo)
                arrow_idx += 1
            #print("set style fill transparent solid 0.7", file = archivo)
            min_x = min_x - (max_x-min_x)/10
            max_x = max_x + (max_x-min_x)/10
            min_y = min_y - (max_y-min_y)/10
            max_y = max_y + (max_y-min_y)/10
            print("set xrange [",min_x,":",max_x,"]", file = archivo)
            print("set yrange [",min_y,":",max_y,"]", file = archivo)
            print("set style fill solid", file = archivo)
            print("set palette defined (0 'blue', 3 'green', 6 'yellow', 10 'red') ", file = archivo)
            if gcolor and gtamano:
                #print("color y tamaño!!")
                print("plot 'nodos.dat' using 1:2:(sqrt($3)/30):4 with circles palette notitle", file = archivo)
            elif gcolor:
                #print("sin tamaño!!")
                print("plot 'nodos.dat' using 1:2:3 with points pt 7 palette notitle", file = archivo)
            elif gtamano:
                #print("sin color!!")
                print("plot 'nodos.dat' using 1:2:(sqrt($3)/30) with circles notitle", file = archivo)
            else:
                #print("sin color sin tamaño!!")
                print("plot 'nodos.dat' using 1:2 with points pt 7 lc rgb 'blue' notitle", file = archivo)
                
            archivo.close()

    def gnuplot_flow(self,name = "grafo_flow.png",term = "png", gcolor = False, gtamano = False):
            n = len(self.nodos)
            with open("nodos.dat",'w') as archivo_nodos:
                for nodo in self.nodos:
                    #nodo = str(i)
                    (x,y) = self.posicion[nodo]
                    size = self.tamano[nodo]
                    color = self.color[nodo]
                    print(x, y,size,color, file = archivo_nodos)
            split = name.split(".")
            filename = split[0] + ".plt"
            arrow_idx = 1
            archivo_nodos.close()
            max_x = 1
            min_x = 0
            max_y = 1
            min_y = 1
            axis_border = 0.05
            edge_weight = 0.2
            with open(filename, 'w') as archivo:
                print("set term "+term, file = archivo)
                print("set output '"+name+"'", file = archivo)
                print("set pointsize 1", file = archivo)
                print("unset label", file = archivo)
                print("unset arrow", file = archivo)
                print("unset colorbox", file = archivo)
                for (ii,jj) in self.aristas:
                    (x1, y1) = self.posicion[ii]
                    (x2, y2) = self.posicion[jj]
                    if x1<min_x: min_x = x1
                    if x2<min_x: min_x = x2
                    if y1<min_y: min_y = y1
                    if y2<min_y: min_y = y2
                    if x1>max_x: max_x = x1
                    if x2>max_x: max_x = x2
                    if y1>max_y: max_y = y1
                    if y2>max_y: max_y = y2
                    print("set label '" + str(ii) + "' at ",x1,"," ,y1, " left offset char -0.4,0", file = archivo) # https://stackoverflow.com/questions/23690551/how-do-you-assign-a-label-when-using-set-object-circle-in-gnuplot
                    print("set label '" + str(jj) + "' at " ,x2, "," ,y2, " left offset char -0.4,0", file = archivo)
                    (apeso, atipo, adirected) = self.aristas[(ii,jj)]
                    apeso = apeso*edge_weight
                    head = "nohead"
                    off_arrow = 0.02
                    if x1<x2:
                        off_x1 = off_arrow
                        off_x2 = -off_arrow
                    else:
                        off_x1 = -off_arrow
                        off_x2 = off_arrow
                    if y1<y2:
                        off_y1 = off_arrow
                        off_y2 = -off_arrow
                    else:
                        off_y1 = -off_arrow
                        off_y2 = off_arrow
                    if adirected:
                        head = "head"
                        if (jj,ii) in self.aristas:
                            if y1<y2:
                                off_y1 = off_y1 + off_arrow/2
                                off_y2 = off_y2 + off_arrow/2
                            else:
                                off_y1 = off_y1 - off_arrow/2
                                off_y2 = off_y2 - off_arrow/2
                    print("set arrow", arrow_idx, "from", x1+off_x1, "," ,y1+off_y1," to ", x2+off_x2, ",", y2+off_y2, head, "filled lw ",apeso, " dashtype ", atipo, file = archivo)
                    arrow_idx += 1
                #print("set style fill transparent solid 0.7", file = archivo)
                min_x = min_x - (max_x-min_x)/10
                max_x = max_x + (max_x-min_x)/10
                min_y = min_y - (max_y-min_y)/10
                max_y = max_y + (max_y-min_y)/10
                print("set xrange [",min_x,":",max_x,"]", file = archivo)
                print("set yrange [",min_y,":",max_y,"]", file = archivo)
                print("set style fill empty", file = archivo)
                print("set palette defined (0 'blue', 3 'green', 6 'yellow', 10 'red') ", file = archivo)
                if gcolor and gtamano:
                    #print("color y tamaño!!")
                    print("plot 'nodos.dat' using 1:2:(sqrt($3)/30):4 with circles palette notitle", file = archivo)
                elif gcolor:
                    #print("sin tamaño!!")
                    print("plot 'nodos.dat' using 1:2:3 with points pt 7 palette notitle", file = archivo)
                elif gtamano:
                    #print("sin color!!")
                    print("plot 'nodos.dat' using 1:2:(sqrt($3)/30) with circles notitle", file = archivo)
                else:
                    #print("sin color sin tamaño!!")
                    print("plot 'nodos.dat' using 1:2 with circles lc rgb 'blue' notitle", file = archivo)
                    
                archivo.close()

    def gnuplot_mh(self,name = "grafo.png",term = "png", gcolor = False, gtamano = False):
        n = len(self.nodos)
        with open("nodos.dat",'w') as archivo_nodos:
            for nodo in self.nodos:
                (x,y) = self.posicion[nodo]
                size = self.tamano[nodo]
                color = self.color[nodo]
                print(x, y,size,color, file = archivo_nodos)
        split = name.split(".")
        filename = split[0] + ".plt"
        arrow_idx = 1
        archivo_nodos.close()
        max_x = 5
        min_x = 0
        max_y = 5
        min_y = 0
        axis_border = 0.05
        edge_weight = 0.2
        with open(filename, 'w') as archivo:
            print("set term "+term, file = archivo)
            print("set output '"+name+"'", file = archivo)
            print("set pointsize 1", file = archivo)
            print("unset label", file = archivo)
            print("unset arrow", file = archivo)
            print("unset colorbox", file = archivo)
            print("set size square", file = archivo)
            for (ii,jj) in self.aristas:
                (x1, y1) = self.posicion[ii]
                (x2, y2) = self.posicion[jj]
                if x1<min_x: min_x = x1
                if x2<min_x: min_x = x2
                if y1<min_y: min_y = y1
                if y2<min_y: min_y = y2
                if x1>max_x: max_x = x1
                if x2>max_x: max_x = x2
                if y1>max_y: max_y = y1
                #print("set label '" + str(ii) + "' at ",x1+ axis_border,"," ,y1+0.05, " left offset char -0.4,0", file = archivo) # https://stackoverflow.com/questions/23690551/how-do-you-assign-a-label-when-using-set-object-circle-in-gnuplot
                #print("set label '" + str(jj) + "' at " ,x2+axis_border, "," ,y2+0.05, " left offset char -0.4,0", file = archivo)
                (apeso, atipo, adirected) = self.aristas[(ii,jj)]
                apeso = apeso*edge_weight
                head = "nohead"
                if adirected:
                    head = "head"
                '''    
                if atipo > 2:
                    color = " 'red' "
                else:
                    color = " 'black' "
                print("set arrow", arrow_idx, "from", x1, "," ,y1,\
                      " to ", x2, ",", y2, head, "filled lw ",apeso,\
                      "lc rgb ", color, file = archivo)
                '''
                if atipo > 2 :
                    color = " 'red' "
                    print("set arrow", arrow_idx, "from", x1, "," ,y1,\
                      " to ", x2, ",", y2, head, "filled lw ",apeso,\
                      "lc rgb ", color, file = archivo)
                arrow_idx += 1
            #print("set style fill transparent solid 0.7", file = archivo)
            min_x = min_x - (max_x-min_x)/10
            max_x = max_x + (max_x-min_x)/10
            min_y = min_y - (max_y-min_y)/10
            max_y = max_y + (max_y-min_y)/10
            print("set xrange [",min_x,":",max_x,"]", file = archivo)
            print("set yrange [",min_y,":",max_y,"]", file = archivo)
            print("set style fill solid", file = archivo)
            print("set palette defined (0 'blue', 3 'green', 6 'yellow', 10 'red') ", file = archivo)
            if gcolor and gtamano:
                #print("color y tamaño!!")
                print("plot 'nodos.dat' using 1:2:(sqrt($3)/30):4 with circles palette notitle", file = archivo)
            elif gcolor:
                #print("sin tamaño!!")
                print("plot 'nodos.dat' using 1:2:3 with points pt 7 palette notitle", file = archivo)
            elif gtamano:
                #print("sin color!!")
                print("plot 'nodos.dat' using 1:2:(sqrt($3)/30) with circles notitle", file = archivo)
            else:
                #print("sin color sin tamaño!!")
                print("plot 'nodos.dat' using 1:2 with points pt 7 lc rgb 'blue' notitle", file = archivo)
                
            archivo.close()                        
                    
            
            
            
        
                
                
            
    
    
        
    
    
        
    
    
