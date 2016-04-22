#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
#创建一个用于读取sheet的生成器,依次生成每行数据,row_count 用于指定读取多少行, col_count 指定用于读取多少列
root = "/mnt/nas2a/ko/classinfo/"
fin = open(sys.argv[1],"r")
file = ''
num = 0
fout = open("result/class.txt","w")
for line in fin:
	check = 0
	if file != line[25]:
		file = line[25]
		fclass = open(root + file.lower() + ".txt")
		text = fclass.readlines()
		fclass.close()
	name = re.findall('[A-H]\d+[A-Z]',line)[0]
	if len(name) < 4:
		name = ""+name[0]+"0"+name[1:3]
	for cl in text:
		if cl.split()[0] == name:
			num = num + 1
			fout.write(cl)
			check = 1
	if check == 0:
		print line
print num
fout.close()
