from grafo import Grafo
from math import floor
from random import random
from statistics import median, mean

#nn = 10
pp = 500
results = []
resultsff = []
rhisfw = dict()
rhistff = dict()
A = [10,20,30,40,50,60,70,80,90,100]
#A = [10,20,30,40,50]

open('cbFW.dat', 'w').close()
open('cbFF.dat', 'w').close()

for nn in A:
    for i in range(pp):
        G = Grafo()
        G.aleatorio(nn,0.3,False,False, True)
        d, time = G.Floyd_Warshal()
        results.append(time)
        a = 1
        b = 2   
        while (d.get((str(a),str(b)),0) < 1) and b not in G.vecinos[str(a)]:
            a = (int(1000*random()))%nn
            b = (int(1000*random()))%nn
            #print("a,b: ",a,b)
        #print("ya!!!!!!!")
        dff, time = G.Ford_Fulkerson(str(a),str(b))
        resultsff.append(time)
    with open('cbFW.dat','a') as fw:
        opening = min(results)
        closing = max(results)
        meanr = mean(results)
        sresults = sorted(results)
        low = median(sresults[0:(int(pp/2)-1)])
        high = median(sresults[(int(pp/2)):(pp-1)])
        print(nn,opening,low,meanr,high,closing, file = fw)
    fw.close()
    with open('cbFF.dat','a') as ff:
        opening = min(resultsff)
        closing = max(resultsff)
        meanr = mean(resultsff)
        sresults = sorted(results)
        low = median(sresults[0:(int(pp/2)-1)])
        high = median(sresults[(int(pp/2)):(pp-1)])
        print(nn,opening,low,meanr,high,closing, file = ff)
    ff.close()
    rhisfw[nn]=results
    rhistff[nn]=resultsff
    print(nn)
    

with open ('boxwFW.plt','w') as cbFW:
    print("reset", file = cbFW)
    print("set term wxt", file = cbFW)
    print("set boxwidth 0.9 absolute ", file = cbFW)
    print("set title 'Diagrama de caja y bigote' ", file = cbFW)
    print("set xrange [ 0.00000 : 110.0000 ] ", file = cbFW)
    print("plot 'cbFW.dat' using 1:3:2:6:5 with candlesticks lw 2 notitle, 'cbFW.dat' using 1:4:4:4:4 with candlesticks lt -1 notitle ", file = cbFW)
    
    












          
    
    

