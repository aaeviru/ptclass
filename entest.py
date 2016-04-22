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
i = sys.argv[1]
fen = open("/home/ko/class/log/"+i+".txt","r")
dict = {}
fout =open("/home/ko/class/test/"+i+".txt","w")
for line in fen:
	term = line.strip('\n')
	w.append(term)
fen.close()

fin = open("/mnt/nas2a/ko/totalfq.txt","r")
for line in fin:
        num = num + 1
	term = line.split()[0]
	print num
	sys.stdout.flush()
	if term not in w:
		continue
	if term in dict:
		dict[term] = dict[term] + int(line.split()[1])
	else:
		dict[term] = int(line.split()[1])
fin.close()
print "read over",num
dict = sorted(dict.items(), key=lambda d: d[1], reverse = True)
for i in range(0,len(dict)):
	fout.write(dict[i][0] + " " + str(dict[i][1])+"\n")
fout.close()	
	

#for list in enl:
#	for term in list:
#		print term
print len(dict)
