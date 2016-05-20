#!/bin/sh
for n in A B C D E F G H; do
	./marketformat /home/ec2-user/data/classinfo/$n/  >& log/market$n.txt &
done
