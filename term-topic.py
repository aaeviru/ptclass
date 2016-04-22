#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
import numpy as np
from numpy import linalg as nplg
from scipy import linalg as sclg
from scipy.sparse import linalg
from scipy import sparse as sp
fin = open("/home/ko/class/result/wordslist.txt","r")
words = fin.readlines()
fin.close()
fin = open("/home/ko/class/result/class.txt","r")
classname = fin.readlines()
fin.close()
a = np.load('/mnt/nas2a/ko/classinfo/vt.npy')
while 1:
	print "term:", 
	sys.stdout.flush()
	term = raw_input()
	if len(term.split()) == 2:
		term_a = term.split()[0]+"\n"
               	if term_a in words:
                        index_a = words.index(term_a)
                        print index_a
               	else:
                        print "none:",term.split()[0]
		term_b = term.split()[1]+"\n"
               	if term_b in words:
                        index_b = words.index(term_b)
                        print index_b
               	else:
                        print "none:",term.split()[1]
		vec_a = a[:,index_a]
		vec_b = a[:,index_b]
		print nplg.norm(vec_a - vec_b)
	else:
		term = term+"\n"
		if term in words:
			index = words.index(term)
			print index 
		else:
			print "none"
		sys.stdout.flush()
		b = a[:,index]
		print b.max(),classname[b.argmax()] 
		b[b.argmax()] = 0
		print b.max(),classname[b.argmax()]
