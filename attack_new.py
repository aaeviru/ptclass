import re
import os
import sys
import numpy as np
from numpy import linalg as nplg
from scipy import linalg as sclg
from scipy.sparse import linalg
from scipy import sparse as sp

if len(sys.argv) != 2:
    print "input: bk file\n"
    exit(0)

fwl = open("/home/ec2-user/git/statresult/wordslist_dsw.txt","r")
wtol = {}
itow = {}
i = 0
for line in fwl:
    term = line.strip('\n')
    wtol[term] = i
    itow[i] = term
    i = i + 1
fwl.close()

a = np.load('/home/ec2-user/data/classinfo/vt.npy')
s = np.load('/home/ec2-user/data/classinfo/sigma.npy')
kk = 623
s = 1 / s
total = 0
hit = 0
notin = 0
totalterm = 0
maxnum = 0
maxnum_1 = 0
aver1 = 0.0;
aver2 = 0.0;
aver3 = 0.0;
aver4 = 0.0;

vec = np.zeros(kk)
fng = open(sys.argv[1],"r")
qch = 0
query = []
rquery = []
bk = []

def attack():
    global vec,aver1,aver2,aver3,aver4,qch,query,rquery,bk,total,hit,a,maxnum,maxnum_1,totalterm
    if vec.max() < 0.0000000000001:
        print vec.max()
        print filename
    else:
        mmax = vec.argmax()
        mmax_1 = vec.max()
        aver4 = aver4 + mmax_1 / np.average(vec)
        vec[vec.argmax()] = 0
        mmax_2 = vec.max()
        vec[vec.argmax()] = 0
        mmax_3 = vec.max()
        vec[vec.argmax()] = 0
        mmax_4 = vec.max()
        aver1 = aver1 + mmax_1 / mmax_2
        aver2 = aver2 + mmax_2 / mmax_3
        aver3 = aver3 + mmax_3 / mmax_4
        tt = []
        for bbk in query:
            total = total + 1
            tttmp = ""
            for term in bbk:
                check = -1
                tmp = np.zeros(kk)
                if term in wtol:
                    totalterm = totalterm + 1
                    tmp = tmp + (s * a[:,wtol[term]])
                    if tmp[mmax] > check:
                        check = tmp[mmax]
                        tttmp = term
            tt.append(tttmp)
        i = 0
        for term in rquery:
            if term == tt[i]:
                hit = hit + 1
            i = i + 1
    print len(tt),len(rquery)
    for i in range(0,len(tt)):
        print tt[i]
        print rquery[i]

for line in fng:
    if line[0] == '@':
        print line
        if qch != 0:
            attack()
        query = []
	qch = 1
    elif len(line) < 2:
        query.append(bk)
        bk = []
    elif line[0] == '!':
        line = line[1:]
        line = line.split()
        rquery = []
        for term in line:
            rquery.append(term)
    else:
        term = line.strip('\n')
        if term in wtol:
            bk.append(term)
            tmp = np.zeros(kk)
            tmp = tmp + (s * a[:,wtol[term]])
            vec = vec + tmp
attack()


print "total:",total
print "hit:",hit
print "presion",1.0*hit/(total)
print "totalterm::",totalterm
print "per term:",1.0*totalterm/(total-notin)
total = 2908
print "maxnum:",maxnum
print "maxnum_1",maxnum_1
print "aver1",aver1/total
print "aver2",aver2/total
print "aver3",aver3/total
print "aver4",aver4/total

