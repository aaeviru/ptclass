from sklearn.neighbors import KDTree
import re
import os
import sys
import numpy as np
from numpy import linalg as nplg
from scipy import linalg as sclg
from scipy.sparse import linalg
from scipy import sparse as sp
if len(sys.argv) < 3:
    print "input: fqfile, outputfile"
    sys.exit(1)
a = np.load('/home/ec2-user/data/classinfo/vt.npy')
s = np.load('/home/ec2-user/data/classinfo/sigma.npy')
s = 1 / s
s = s.reshape(623,1)
a = s * a 
del s
x = []
ffq = open(sys.argv[1],"r")
for line in ffq:
    tmp = line.split(':')[0]
    tmp = tmp.split()
    if len(tmp) == 1:
        vec = a[:,int(tmp[0])]
    elif len(tmp) == 2:
        vec = a[:,int(tmp[0])] + a[:,int(tmp[1])]
    x.append(vec)
x = np.array(x)
del a
print x.shape

nbrs = KDTree(x)
np.savetxt(sys.argv[2],nbrs.query(x,k=3)[1],fmt='%i')
