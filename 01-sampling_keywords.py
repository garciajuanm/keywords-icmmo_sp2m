import numpy as np

data = np.loadtxt('00-database.dat',delimiter='\t',dtype=np.str)

#~ n : number of publications
n = np.shape(data)[0]

f = open('02-keywords.dat','w')

#~ go through every publication
for i in range(n):
	#~ read doi, year and keywords of each publication 
	doi = data[i,1]
	year = data[i,3]
	keys = data[i,5].split(';')
	
	#~ write in lines of a new file
	for key in keys:
		f.write('%s\t%s\t%s\n' % (year,doi,key.lower()))

f.close()
