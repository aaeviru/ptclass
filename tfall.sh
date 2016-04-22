#!/bin/sh
for d in A B C D E F G H; do
	qrsh -N tf$d -nostdin python tfall.py /mnt/nas2a/ko/classinfo/$d/ >& log/$d.txt &
done

