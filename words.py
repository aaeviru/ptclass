import os
import os.path
import re
import sys
num = 0
sw = []
fin = open("/mnt/nas2a/ko/stopword2.txt","r")
for line in fin:
        sw.append(line.split()[0])
fin.close()
words = []
for root, dirs, files in os.walk(sys.argv[1]):
        for name in files:
                filename = root + '/' + name
		if filename[len(filename)-1] == 'q':
			fin = open(filename,"r")
			num = num + 1
			for line in fin:
                                tmp = line.split()[0]
                                if tmp in sw:
                                        continue
				if tmp in words:
					continue
				words.append(tmp)
			fin.close()
fout = open("/home/ko/class/result/words.txt","w")
for word in words:
	fout.write(word + "\n")
fout.close()
print num
