#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
import string
import re
import sys
import unicodedata
import codecs
num = 0
w = [] 
fen = open("/home/ec2-user/data/en_words.txt","r")
fout =[open("/home/ec2-user/data/"+str(i+1)+".txt","w") for i in range(11)]
for line in fen:
	term = line.strip('\n')
	w.append(term)
fen.close()
print "set up over"
for term in w:
	u = unicode(term, "utf-8")
	l = len(u)
	if l < 11:
		fout[l-1].write(term+"\n")
	else:
        	fout[10].write(term+"\n")
for i in range(11):
	fout[i].close()	
	

#for list in enl:
#	for term in list:
#		print term
print len(w)
