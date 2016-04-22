#!/bin/sh
for n in 3 4 5 6 7 8 9 11 1 2; do
	qrsh -N enfq$n -q canis6.q -nostdin python entest.py $n  >& log/enfq$n.txt &
done
