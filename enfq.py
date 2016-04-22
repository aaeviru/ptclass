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
fen = open("/home/ko/class/result/en_words.txt","r")
dict = {}
fout =[open("/home/ko/class/result/"+str(i)+".txt","w") for i in range(11)]
for line in fen:
	term = line.strip('\n')
	w.append(term)
fen.close()

fin = open("/mnt/nas2a/ko/NTCIR.txt","r")
for line in fin:
        num = num + 1
	if line[0] == '@':
		continue
	term = line.split()[1]
	if term not in w:
		continue
	if term in dict:
		dict[term] = dict[term] + int(line.split()[0])
	else:
		dict[term] = int(line.split()[0])
fin.close()
print "read over",num
dict = sorted(dict.items(), key=lambda d: d[1], reverse = True)
for i in range(0,len(dict)):
	term = dict[i][0]
	u = unicode(term, "utf-8")
	l = len(u)
	if l < 11:
		fout[l].write(term + " " + str(dict[i][1])+"\n")
	else:
        	fout[0].write(term + " " + str(dict[i][1])+"\n")
for i in range(11):
	fout[i].close()	
	

#for list in enl:
#	for term in list:
#		print term
print len(dict)
