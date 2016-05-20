import os
import sys

if len(sys.argv) < 4:
    print "input: fqfile,kdresult,outputfile"
    sys.exit(1)

ffq = open(sys.argv[1],"r")
fkd = open(sys.argv[2],"r")
fout = open(sys.argv[3],"w")

fqlist = []
for line in ffq:
    tmp = line.split(':')[0]
    tmp = tmp.split()
    if len(tmp) > 0:
        fqlist.append(tmp)
ffq.close()
cqg =set()

for line in fkd:
    tmp = line.split()
    cqg_tmp=[]
    for i in tmp:
        for j in fqlist[int(i)]:
            if int(j) not in cqg_tmp:
                cqg_tmp.append(int(j))
    cqg_tmp.sort()
    if tuple(cqg_tmp) not in cqg:
        cqg.add(tuple(cqg_tmp))
        fout.write(' '.join(str(a) for a in cqg_tmp)+'\n')
fkd.close()
fout.close()
print len(cqg)
