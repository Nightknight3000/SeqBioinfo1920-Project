set terminal x11 font "Courier,8"
set ytics ( \
 "CP041955.1" 1, \
 "CP041956.1" 4856183, \
 "CP041957.1" 4931127, \
 "CP041958.1" 5014774, \
 "CP041959.1" 5018845, \
 "CP041960.1" 5103761, \
 "" 5201916 \
)
set size 1,1
set grid
unset key
set border 10
set tics scale 0
set xlabel "NC_004431.1"
set ylabel "QRY"
set format "%.0f"
set mouse format "%.0f"
set mouse mouseformat "[%.0f, %.0f]"
if(GPVAL_VERSION < 5) set mouse clipboardformat "[%.0f, %.0f]"
set xrange [1:5231428]
set yrange [1:5201916]
set style line 1  lt 1 lw 2 pt 6 ps 1
set style line 2  lt 3 lw 2 pt 6 ps 1
set style line 3  lt 2 lw 2 pt 6 ps 1
plot \
 "out.fplot" title "FWD" w lp ls 1, \
 "out.rplot" title "REV" w lp ls 2

print "-- INTERACTIVE MODE --"
print "consult gnuplot docs for command list"
print "mouse 1: coords to clipboard"
print "mouse 2: mark on plot"
print "mouse 3: zoom box"
print "'h' for help in plot window"
print "enter to exit"
pause -1
