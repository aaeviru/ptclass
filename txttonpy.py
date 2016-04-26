#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as nplg
from scipy import linalg as sclg
from scipy.sparse import linalg
from scipy import sparse as sp

tt = []
fin = open("/home/ec2-user/data/classinfo/matrix.txt","r")
#a = np.loadtxt('/mnt/nas2a/ko/classinfo/matrix.txt')
turn = 1
for line in fin:
	print turn
	turn = turn + 1
	tmptt = []
	for num in line.split():
		tmptt.append(int(num))
	tt.append(tmptt)
#	if turn > 5:
#		break
a = np.matrix(tt)	
np.save('/home/ec2-user/data/classinfo/matrix.npy',a)

