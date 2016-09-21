#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as nplg
from scipy import linalg as sclg
from scipy.sparse import linalg
from scipy import sparse as sp
import sys
print "start"
a = np.loadtxt('/home/ec2-user/data/classinfo/matrix-tfidf.txt')	
print "load completed"
print a
sys.stdout.flush()
#kk = nplg.matrix_rank(a)
#print kk
#x = a.sum(axis = 0)
#print np.shape(x[x>5])
u,sigma,vt = sclg.svd(a,full_matrices=False)
#u,sigma,vt = linalg.svds(a,k=kk)
print "compute over"
sys.stdout.flush()
del a
print abs(u)
print sigma
print abs(vt)
#np.savetxt('/home/ec2-user/data/classinfo/u.txt',abs(u),fmt='%1.4e')
#np.savetxt('/home/ec2-user/data/classinfo/sigma.txt',sigma,fmt='%1.4e')
#np.savetxt('/home/ec2-user/data/classinfo/vt.txt',abs(vt),fmt='%1.4e')
np.save('/home/ec2-user/data/classinfo/u-tfidf.npy',abs(u))
np.save('/home/ec2-user/data/classinfo/sigma-tfidf.npy',sigma)
np.save('/home/ec2-user/data/classinfo/vt-tfidf.npy',abs(vt))
print "over"
