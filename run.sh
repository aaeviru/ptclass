#!/bin/sh
qrsh -N class -nostdin ./a.out /mnt/nas2b/ko/Data/ >& log/fq.txt &
qrsh -N enfq -nostdin python enfq.py >& log/enfq.txt &
