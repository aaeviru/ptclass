import os
import os.path
import re
import sys
for root, dirs, files in os.walk(sys.argv[1]):
        for name in files:
                filename = root + '/' + name
		if filename[len(filename)-1] == 'w':#filename pattern
			num = 0
			fin = open(filename,"r")
			dict = {}
			line = fin.readline()
			while line:
				if line[0] == '@':
					line = fin.readline()
					num = num + 1
	#	print sorted(dict.items(), key=lambda d: d[1], reverse = True)
	#        raw_input("input")
					continue
				ssplit = line.split()
				if dict.has_key(ssplit[1]):
					dict[ssplit[1]]=dict[ssplit[1]]+int(ssplit[0])
				else:
					dict[ssplit[1]]=int(ssplit[0])
				line = fin.readline()
	
			fin.close()
			print(filename,num)
			fout = open(filename+".fq","w")
			dict = sorted(dict.items(), key=lambda d: d[1], reverse = True)
			for i in dict:
				fout.write(i[0] + " " + str(i[1]) + "\n")
			fout.close()

