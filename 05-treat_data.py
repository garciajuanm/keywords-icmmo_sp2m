import os,sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
plt.rc('text', usetex=True)

keywords = np.loadtxt('04-count.dat',delimiter='\t',dtype=np.str,usecols=(0,))
count	 = np.loadtxt('04-count.dat',delimiter='\t',dtype=np.int,usecols=(1,))

mask = (count > 2) *  (count < 68) + (keywords == 'plastic anisotropy') + (keywords == 'low cycle fatigue')

for i,key in enumerate(keywords[mask]):
	print key,count[mask][i]

indSort = np.argsort(count[mask])[::]

labels = np.array(keywords[mask])[indSort]
values = np.array(count[mask])[indSort]


bar_width=.4

indexes = np.arange(len(keywords[mask]))



plt.figure(figsize=(13,11))
plt.barh(indexes, values)

plt.ylabel(r'Mot cl\'{e}s',size=22)
plt.xlabel(r'Comptage',size=22)
plt.ylim(0,33)
plt.xlim(0,17)
# add labels
plt.xticks([0,2,4,6,8,10,12,14,16],['0','2','4','6','8','10','12','14','16'],size=18)
plt.yticks(indexes + bar_width, labels,size=18)
plt.tight_layout()
plt.axhline(30-.1,linestyle='--')
plt.axhline(29-.1,linestyle='--')
plt.axhline(28-.1,linestyle='--')
plt.axhline(27-.1,linestyle='--')
plt.axhline(25-.1,linestyle='--')
plt.text(16.5,31.5,'1',va='center',ha='center',fontsize=15,fontweight='heavy')
plt.text(16.5,29.5,'2',va='center',ha='center',fontsize=15,fontweight='heavy')
plt.text(16.5,28.5,'3',va='center',ha='center',fontsize=15,fontweight='heavy')
plt.text(16.5,27.5,'4',va='center',ha='center',fontsize=15,fontweight='heavy')
plt.text(16.5,26.0,'5',va='center',ha='center',fontsize=15,fontweight='heavy')
plt.savefig('bars.png',dpi=150)
os.system('cp bars.png /home/jgarcia/Documents/Candidatures/2020-03-16--MCF/figures/png/bars.png')

plt.show()
