import numpy as np

keywords = np.loadtxt('02-keywords.dat',delimiter='\t',dtype=np.str)

f = open('04-count.dat','w')

for key in np.unique(keywords[::,2]):
	n=list(keywords[::,2]).count(key)
	print'/%s/' % key,n
	f.write('%s\t%s\n' % (key,n))
f.close()
