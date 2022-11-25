import matplotlib.pyplot as plt
#2 clients, varying number of msgs
#20 msgs
a20=[0.00020726, 0.00076856, 0.00052257, 0.00050621, 0.00035936, 0.00040109, 0.00059885, 0.00013394, 0.00026897, 0.00026648, 0.00021604, 0.00082189, 0.00072587, 0.00043022, 0.00034825, 0.0003583,  0.00058661, 0.00016771, 0.00023534, 0.00013437]
plt.plot([i for i in range(20)],[sum(a20)/len(a20) for i in range(20)],'b--')
plt.plot([i for i in range(20)],a20, 'r--')
plt.plot([i for i in range(20)],a20, 'ro')
plt.title("2 clients, 20 msgs")
plt.ylabel("Time difference in seconds")
plt.xlabel("Message")
plt.legend(["Latency"])
plt.xticks([i for i in range(20)],[i+1 for i in range(20)])
plt.savefig("Latency20.jpg", dpi=600)
# plt.show()
plt.close()

#10 msgs
a10=[0.0000530, 0.0002960, 0.0002718, 0.0005080, 0.0003860, 0.0003760, 0.0000360, 0.0002220, 0.0000310, 0.0005390]
plt.plot([i for i in range(10)],[sum(a10)/len(a10) for i in range(10)],'b--')
plt.plot([i for i in range(10)],a10, 'r--')
plt.plot([i for i in range(10)],a10, 'ro')
plt.title("2 clients, 10 msgs")
plt.ylabel("Time difference in seconds")
plt.xlabel("Message")
plt.legend(["Latency"])
plt.xticks([i for i in range(10)],[i+1 for i in range(10)])
plt.savefig("Latency10.jpg", dpi=600)
# plt.show()
plt.close()

#8 msgs
a8=[0.000039, 0.000562,0.000453, 0.000829, 0.000216, 0.000109, 0.000286, 0.000093]
plt.plot([i for i in range(8)],[sum(a8)/len(a8) for i in range(8)],'b--')
plt.plot([i for i in range(8)],a8, 'r--')
plt.plot([i for i in range(8)],a8, 'ro')
plt.title("2 clients, 8 msgs")
plt.ylabel("Time difference in seconds")
plt.xlabel("Message")
plt.legend(["Latency"])
plt.xticks([i for i in range(8)],[i+1 for i in range(8)])
plt.savefig("Latency8.jpg", dpi=600)
plt.close()

#5 msgs
a5=[0.0004720, 0.0002560, 0.0015900, 0.0002350, 0.0006110]
plt.plot([i for i in range(5)],[sum(a5)/len(a5) for i in range(5)],'b--')
plt.plot([i for i in range(5)],a5, 'r--')
plt.plot([i for i in range(5)],a5, 'ro')
plt.title("2 clients, 5 msgs")
plt.ylabel("Time difference in seconds")
plt.xlabel("Message")
plt.legend(["Latency"])
plt.xticks([i for i in range(5)],[i+1 for i in range(5)])
plt.savefig("Latency5.jpg", dpi=600)
plt.close()


#1 server, multiple clients
b3=[0.0015710000,0.0074840000,0.0045275] #3 clients
b4=[0.0030960000, 0.0000460000, 0.0048430000,0.0026616666666666663] #4 clients
b5=[0.0653380000,0.0071570000,0.0074040000,0.0039150000,0.020953499999999996] #5 clients
b6=[0.0004620000, 0.0000710000, 0.0012670000, 0.0129090000, 0.0020070000, 0.0033432] #6 clients

import numpy as np
lat=[]
lat.append(np.mean(b3))
lat.append(np.mean(b4))
lat.append(np.mean(b5))
lat.append(np.mean(b6))
plt.plot([i for i in range(4)],lat,'r--')
plt.plot([i for i in range(4)],lat,'ro')
plt.title("Multiple clients on 1 server")
plt.ylabel("Latency in seconds")
plt.xlabel("Number of clients")
plt.xticks([i for i in range(4)],[3,4,5,6])
plt.savefig("Multiclient_lat.jpg", dpi=600)
plt.close()

#1 server, 2 client, 6 messages
c1=[0.0003010000, 0.0000380000,0.0004500000,0.0011260000,0.0000120000,0.00038540000000000004]
c1m=np.mean(c1)
print("Latency (in secs) for 1 server, 2 clients, 6 messages is: ", c1m)

