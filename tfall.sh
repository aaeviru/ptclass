#!/bin/sh
for d in A B C D E F G H; do
	python tfall.py ~/data/classinfo/$d/ >& log/$d.txt &
done

