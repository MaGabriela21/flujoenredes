from grafo import Grafo
from math import factorial
'''
nn = 20
G = Grafo()
G.aleatorio(nn,0.3,False,False, True)
d, time = G.Floyd_Warshal()
ag = G.avg_dist()
ac = G.clust_coef()
print(ag)
print(ac)

C = Grafo()
C.circ_aleatorio()
C.gnuplot("circulo.png")

nn = 10
k = 1
p = 2**(-2)
K = Grafo()
K.kcirc_aleatorio(nn,k,p)
K.gnuplot("rkcirc1.png")
s = (nn/2)/k
kag = K.avg_dist()
'''

nn = 50
k = 1
s = (nn/2)/k
results_ads = []
results_ac = []
for i in range(10):
    p = 2**(-10+i) #powers of 2 increasing from -10 to -1
    #print(i,' ',p)
    A = Grafo()
    A.kcirc_aleatorio(nn,k,p)
    ad = A.avg_dist()
    ads = ad / s
    ac = A.clust_coef()
    #ac = ac / s
    results_ads.append(ads)
    results_ac.append(ac)
 
with open('results_dc.dat', 'w') as dc:
    for a in range(10):
        i = results_ads[a]
        j = results_ac[a]
        p = 2**(-10+a)
        print(p, ' ', i, ' ', j, file = dc)
x0 = (2**(-11))
x1 = (2**(-1)+.05)
x1 = 1
y0 = -.01
y1 = 1.1
pltfile = 't4graph'+str(k)+'.plt'
outfile = "'g"+str(k)+".tex'"
with open(pltfile, 'w') as a:
    print("reset", file = a)
    print("set term epslatex color colortext", file = a)
    print("set output ",outfile, file = a)
    #print("set term wxt", file = a)
    print("set pointsize 1.5", file = a)
    print("set logscale x 2", file = a)
    print("set xtics (0.0009765625, 0.001953125,0.00390625, 0.0078125 , 0.015625, 0.03125,0.0625,0.125,0.25,0.5)", file = a)
    print("set xrange [ ",x0,':',x1,']',file = a)
    print("set yrange [ ",y0,':',y1,']',file = a)
    print("set xlabel 'p: probabilidad de conectar cada par de nodos' ", file = a)
    print("set ylabel 'd/s' rotate by 90", file = a)
    print("set y2label 'c' ", file = a)
    print("set key center top box",file = a)
    print("set format x '2^{%L}'", file = a)
    #print("plot 'results_dc.dat' using 1:2 with points notitle, 'results_dc.dat' using 1:3 with points notitle ", file = a)
    print("plot 'results_dc.dat' using 1:2 with points title 'd/s: distancia promedio', 'results_dc.dat' using 1:3 with points title 'c: coeficiente de agrupamiento' ", file = a)
    
dc.close()
#dac.close()
a.close()
'''
nn = 6
k = 1
p = 0
K = Grafo()
K.kcirc_aleatorio(nn,k,p)
K.conecta('1','4',1,False,1)  
K.conecta('2','4',1,False,1)
K.conecta('2','5',1,False,1)
K.gnuplot("rkcirc2.png")
print(K.clust_coef())
'''

