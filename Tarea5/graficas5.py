iidd = "k20-l3"
filename = "ttm"+iidd
#idd = idd +"-p0.0001"
idd = iidd +"-p0.0001"

with open("tm.plt", "w") as archivo:
    print("reset", file = archivo)
    #print("set term wxt", file = archivo)
    print("set term epslatex color colortext", file = archivo)
    print("set output '"+filename+".tex' ", file = archivo)
    #print("set yrange [-0.005:1.05]",file = archivo)
    print("set xlabel 'nodos eliminados'", file = archivo)
    #print("set ylabel 'flujo maximo'", file = archivo)
    print("set ylabel 'tiempo de ejecucion'", file = archivo)
    print("set key off", file = archivo)
    print("plot 'aa2results-"+idd +".txt' using 1:3 with linespoints pt 5 lc 1" ,
          #" ,'a4results-"+idd +".txt' using 1:3 with linespoints pt 7 lc 5",
          #" ,'a3results-"+idd +".txt' using 1:3 with linespoints pt 7 lc 4",
          #" ,'a2results-"+idd +".txt' using 1:3 with linespoints pt 7 lc 3",
          " ,'aa1results-"+idd +".txt' using 1:3 with linespoints pt 5 lc 2",file = archivo)


filenamef = "mmmmmf"+iidd


with open("mmf.plt", "w") as archivo:
    print("reset", file = archivo)
    print("set term wxt", file = archivo)
    #print("set term epslatex color colortext", file = archivo)
    #print("set output '"+filenamef+".tex' ", file = archivo)
    print("set yrange [-0.005:1.05]",file = archivo)
    print("set xlabel 'nodos eliminados'", file = archivo)
    print("set ylabel 'flujo maximo'", file = archivo)
    #print("set ylabel 'tiempo de ejecución'", file = archivo)
    print("set key off", file = archivo)
    print("plot 'aa2results-"+idd +".txt' using 1:2 with linespoints pt 5 lc 1" ,
          #" ,'a4results-"+idd +".txt' using 1:2 with linespoints pt 7 lc 5",
          #" ,'a3results-"+idd +".txt' using 1:2 with linespoints pt 7 lc 4",
          #" ,'a2results-"+idd +".txt' using 1:2 with linespoints pt 7 lc 3",
          " ,'aa1results-"+idd +".txt' using 1:2 with linespoints pt 5 lc 2",file = archivo)

