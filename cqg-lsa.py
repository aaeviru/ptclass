import re
import os
import sys
import numpy as np
from numpy import linalg as nplg
from scipy import linalg as sclg
from scipy.sparse import linalg
from scipy import sparse as sp

if len(sys.argv) != 2:
    print "input: cqg file\n"
    exit(0)

a = np.load('/home/ec2-user/data/classinfo/vt-kk.npy')
s = np.load('/home/ec2-user/data/classinfo/sigma-kk.npy')
kk = 30 
s = 1 / s
s = s.reshape(kk,1)
a = s * a
del s
matrix = []

fcqg = open(sys.argv[1])
for line in fcqg:
    line = line.strip('\n')
    line = line.split()
    vec = np.zeros(kk)
    for term in line:
        vec = vec + a[:,int(term)]
    matrix.append(vec)
del a
matrix = np.array(matrix)
print matrix.shape
np.savetxt('/home/ec2-user/data/classinfo/cqg-kk.txt',abs(matrix),fmt='%1.4e')
np.save('/home/ec2-user/data/classinfo/cqg-kk.npy',abs(matrix))
