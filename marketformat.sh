#!/bin/sh
for n in A B C D E F G H; do
	qrsh -N market$n -q canis6.q -nostdin ./marketformat /mnt/nas2a/ko/classinfo/$n/  >& log/market$n.txt &
done
