#Messaging pattern latency
# 4 msgs from a to b
a1=[0.0010660000,
0.0000140000,
0.0000210000,
0.000367
]

#1 from a to b and 3 from b to a
a2=[0.0011040000,
0.0006170000,
0.0000430000,
0.0003310000,
]

#1 messages from a to b and 5 message from b to a
a3=[0.0000650000,
0.0005890000,
0.0003470000,
0.0002330000,
0.0000200000,
]

#3 messages from a to b and 3 message from b to a
a4=[0.0000010000,
0.0002950000,
0.0001320000,
0.0011110000,
0.0000080000,
0.0005300000,
]

import numpy as np
lat=[]
lat.append(np.mean(a1))
lat.append(np.mean(a2))
lat.append(np.mean(a3))
lat.append(np.mean(a4))

import matplotlib.pyplot as plt
plt.figure(figsize=(8,4))
plt.plot([i for i in range(4)], lat, 'bo')
plt.plot([i for i in range(4)], lat, 'b--')
plt.xlabel("Messaging pattern")
plt.ylabel("Latency in secs")
plt.xticks([i for i in range(4)],["4-0",'1-3','1-5','3-3'])
plt.title("Latency vs Messaging patterns")
plt.savefig("msgdiff.jpg",dpi=600)
plt.close()
