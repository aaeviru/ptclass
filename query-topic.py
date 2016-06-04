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
    print "input: cqgfile, outputfile"
    sys.exit(1)
a = np.load('/home/ec2-user/data/classinfo/vt.npy')
s = np.load('/home/ec2-user/data/classinfo/sigma.npy')
s = 1 / s
s = s.reshape(623,1)
a = s * a 
del s
x = []
fcqg = open(sys.argv[1],"r")
for line in fcqg:
    tmp = line.split()
    vec = zeros(623)
    for i in tmp:
        vec = vec + a[:,int(i)]
    x.append(vec)
    break
fcqg.close()
del a
x = np.array(x)
print x.shape

nbrs = KDTree(x)
np.savetxt(sys.argv[2]+".txt",x,fmt='%1.4e')
np.save(sys.argv[2]+".npy",x)

