#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import sys
import numpy as np
from numpy import linalg as nplg
from scipy import linalg as sclg
from scipy.sparse import linalg
from scipy import sparse as sp
from scipy.spatial import distance as dist

if len(sys.argv) != 2:
    print "input: topic-folder\n"
    exit(0)
fwl = open ("/home/ec2-user/git/statresult/wordslist_dsw.txt","r")
wtol = {}
ltow = {}
i = 0
for line in fwl:
    line = line.strip('\n')
    wtol[line]=i
    ltow[i]=line
    i = i + 1

a = np.load('/home/ec2-user/data/classinfo/vt-kk.npy')
s = np.load('/home/ec2-user/data/classinfo/sigma-kk.npy')
kk = 30
s = 1 / s
s = s.reshape(kk,1)
a = s * a
a = np.transpose(a)
maxid = a.shape[0]
del s
vec = np.zeros(kk)
for root, dirs, files in os.walk(sys.argv[1]):
    for name in files:
        filename = root + '/' + name
        if filename[len(filename)-1] == 't':#filename pattern
            print "@" + filename
            ftp = open(filename,"r")
            terms = []
            for line in ftp:
                term = line.strip('\n')
                terms.append(term)
                vec = vec + a[wtol[term]]
            mmax = vec.argmax()
            b = a[:,mmax].argsort()
            y = []
            for term in terms:
                y.append(np.where(b == wtol[term]))
            for i in range(0,len(terms)):
                tmp = []
                ttt = a[b[y[i][0][0]],mmax]
                tt = a[b[y[i][0][0]]]
                index = y[i][0][0] - 1
                while index > 0 and (abs(a[b[index],mmax] - ttt) < ttt * 0.05 or abs(index - y[i][0][0])<10):
                    tmp.append((index,dist.cosine(a[b[index]],tt)))
                    index = index - 1
                index = y[i][0][0] + 1
                while index < maxid and (abs(a[b[index],mmax] - ttt) < ttt * 0.05 or abs(index - y[i][0][0])<10):
                    tmp.append((index,dist.cosine(a[b[index]],tt)))
                    index = index + 1
                print ltow[b[y[i][0][0]]]
                dm = sorted(tmp,key=lambda x:x[1])
                print ltow[b[dm[0][0]]]
                print ltow[b[dm[1][0]]]
                print ltow[b[dm[2][0]]]
                print
            print "!"+" ".join(terms)
