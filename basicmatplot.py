#import matplotlib
import matplotlib.pyplot as plt
#print(matplotlib.__version__)

#plt.plot([1,2,3,4],[1,4,9,16])
#plt.show()
#plt.scatter([1,2,3,4],[1,4,9,16])
#plt.show()
#plt.bar(['group_a','group_b','group_c'],[1,10,5])
#plt.show()
#plt.hist([1,2,2,3,4,4,])
#plt.show()
fig,ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('title')
plt.show()