from multiprocessing import Process
import os
import re
import time
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
def func(strg):
	os.system(strg)

directory = raw_input("Enter directory: ")
m = raw_input("Enter m: ")
m=int(m)
foldlist = list()
jobs=[]
t1=time.time()

for dirs in os.listdir(directory):
  	found = re.search(r'[0-9]+',str(dirs),0)
  	logging.warning(dirs)
  	#print f
#ipdir = str(sys.argv[1])
  	if found:
		for curr_dir, sub_dir, filenames in os.walk(directory+'/'+dirs):
			for sd in sub_dir:
				#print os.path.join(curr_dir,sd)
				f = re.search(r'[0-9]+',str(sd),0)
				if not f:
					continue
				strg = "python myalbum_p1.py " + os.path.join(curr_dir,sd) +' '+ sd
				#print strg
				foldlist.append(strg)

#for d in os.listdir(dirt):
#for d in os.listdir(str(os.getcwd())+"/"+dirt):
#	f = re.search(r'[0-9]+',str(d),0)
#	if f:
#		print d
		#	strg = "python new_mysong.py "+str(os.getcwd())+"/"+dirt+"/"+str(d)+' '+str(d)
		#strg="python mysong_p2.py " +dirt+"/"+str(d)+' '+str(d)
		#foldlist.append(strg)

n = len(foldlist)
logging.warning(n)
count=0
#m = 1
k = n/m
t = n%m
if t > 0:
	blocknumber = k+1
else:
	blocknumber = k
for j in range(1,blocknumber+1):
	p=j-1
	if p == blocknumber:
		q = t
	else:
		q = m
	for i in foldlist[p*m:p*m+q]:
		logging.warning(i)
		p = Process(target=func,args=(i,))
		findex = i.rfind(' ')
		foldname = i[findex+1:len(i)]
		logging.warning("folder name ==========================")
		logging.warning(foldname)
		count = count + 1
		logging.warning("count="+str(count))
		jobs.append(p)
		p.start()
	p.join()
logging.warning(time.time()-t1)

		
