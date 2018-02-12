unset object
set object 1 circle at 130,120 size 162 fc rgb 'red' fs transparent solid 0.15
set object 2 circle at 178,340 size 162 fc rgb 'red' fs transparent solid 0.15
set object 3 circle at 390,434 size 162 fc rgb 'red' fs transparent solid 0.15
set object 5 circle at 440,148 size 162 fc rgb 'red' fs transparent solid 0.15


set size square
plot '1basicUnits.dat' using 1:2 with points pt 7 linecolor rgb 'navy'
