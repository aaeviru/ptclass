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
sw = []
fin = open("/home/ko/class/result/wordslist.txt","r")
fjp = open("/home/ko/class/result/jp_words.txt","w")
fen = open("/home/ko/class/result/en_words.txt","w")
felse = open("/home/ko/class/result/else_words.txt","w")
def is_japanese(string):
    	for ch in string[:len(string)-1]:
        	name = unicodedata.name(ch) 
        	if "CJK UNIFIED" in name \
	        or "HIRAGANA" in name \
	        or "KATAKANA" in name:	
			return True
	return False

def is_en(string):
    	for ch in string[:len(string)-1]:
        	name = unicodedata.name(ch) 
		if "LATIN" not in name and "GREEK" not in name and "DIGIT" not in name:
			return False
	return True

for line in fin:
	check = 0
	u = unicode(line, "utf-8",'ignore')
	if u != unicode(line, "utf-8",'replace'):
		continue
	if is_japanese(u):
		fjp.write(line)
	elif is_en(u):
		fen.write(line)
	else:
		felse.write(line)
	num = num + 1
	print num
	sys.stdout.flush()
fin.close()
fjp.close()
fen.close()
print num
