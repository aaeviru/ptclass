#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as nplg
from scipy import linalg as sclg
from scipy.sparse import linalg
from scipy import sparse as sp
import sys
print "start"
a = np.load('/mnt/nas2a/ko/classinfo/matrix_int.npy')	
print "load completed"
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
np.savetxt('/mnt/nas2a/ko/classinfo/u.txt',abs(u),fmt='%1.4e')
np.savetxt('/mnt/nas2a/ko/classinfo/sigma.txt',sigma,fmt='%1.4e')
np.savetxt('/mnt/nas2a/ko/classinfo/vt.txt',abs(vt),fmt='%1.4e')
np.save('/mnt/nas2a/ko/classinfo/u.npy',abs(u))
np.save('/mnt/nas2a/ko/classinfo/sigma.npy',sigma)
np.save('/mnt/nas2a/ko/classinfo/vt.npy',abs(vt))
print "over"
