#Throughput
window=0.00001
#7 messages
inpthr=[]
outthr=[]

inp1=[4.807281, 4.855927, 4.807299, 4.835159, 4.880234, 4.855912, 4.835123]
out1=[4.807657, 4.856251, 4.807475, 4.836843, 4.880235, 4.856281, 4.83556]
mininp1=min(inp1)
maxinp1=max(inp1)
lframe=mininp1
rframe=mininp1+window
inp_thr=[]
while rframe<=maxinp1:
    count=0
    for x in inp1:
        if x<=rframe and x>=lframe:
            count+=1
    # print(count, lframe, rframe)
    inp_thr.append(count)
    lframe+=window
    rframe+=window
print("Input throughput for 7 messages: ",sum(inp_thr)/(len(inp_thr)*window))
inpthr.append(sum(inp_thr)/(len(inp_thr)*window))

minout1=min(out1)
maxout1=max(out1)
lframe=minout1
rframe=minout1+window
out_thr=[]
while rframe<=maxout1:
    count=0
    for x in out1:
        if x<=rframe and x>=lframe:
            count+=1
    # print(count, lframe, rframe)
    out_thr.append(count)
    lframe+=window
    rframe+=window
print("Output throughput for 7 messages: ",sum(out_thr)/(len(out_thr)*window))
outthr.append(sum(out_thr)/(len(out_thr)*window))

#10 messages
inp2=[1.634675, 1.595457, 1.635329, 1.672219, 1.562923, 1.596236, 1.711465, 1.672849, 1.55778, 1.71152]
out2=[1.635106, 1.595689, 1.635631, 1.672458, 1.56325, 1.596732, 1.720364, 1.673033, 1.55798, 1.712105]

mininp2=min(inp2)
maxinp2=max(inp2)
lframe=mininp2
rframe=mininp2+window
inp_thr=[]
while rframe<=maxinp2:
    count=0
    for x in inp2:
        if x<=rframe and x>=lframe:
            count+=1
    # print(count, lframe, rframe)
    inp_thr.append(count)
    lframe+=window
    rframe+=window
print("Input throughput for 10 messages: ",sum(inp_thr)/(len(inp_thr)*window))
inpthr.append(sum(inp_thr)/(len(inp_thr)*window))

minout2=min(out2)
maxout2=max(out2)
lframe=minout2
rframe=minout2+window
out_thr=[]
while rframe<=maxout2:
    count=0
    for x in out2:
        if x<=rframe and x>=lframe:
            count+=1
    # print(count, lframe, rframe)
    out_thr.append(count)
    lframe+=window
    rframe+=window
print("Output throughput for 10 messages: ",sum(out_thr)/(len(out_thr)*window))
outthr.append(sum(out_thr)/(len(out_thr)*window))

#20 messages
inp3= [8.93735407, 8.92904484, 8.96166066, 8.94850438, 8.91155991, 8.93024289, 8.92650851, 8.93299007, 8.92550545, 8.92545595, 8.91524109, 8.9844557,
8.93363204, 8.97991074, 8.94588033, 8.95067023, 8.92719479, 8.9363051, 8.96087742, 8.9587719 ]
out3=[8.94146198, 8.91745354, 8.92069526, 8.91988165, 8.92088645, 8.94020783, 8.98363308, 8.94002697, 8.93386365, 8.94290043, 8.97708703, 8.95120019,
8.94375468, 8.97953179, 8.91723752, 8.92369027, 8.97076528, 8.95391915, 8.96495676, 8.98042508]

mininp3=min(inp3)
maxinp3=max(inp3)
lframe=mininp3
rframe=mininp3+window
inp_thr=[]
while rframe<=maxinp3:
    count=0
    for x in inp3:
        if x<=rframe and x>=lframe:
            count+=1
    # print(count, lframe, rframe)
    inp_thr.append(count)
    lframe+=window
    rframe+=window
print("Input throughput for 20 messages: ",sum(inp_thr)/(len(inp_thr)*window))
inpthr.append(sum(inp_thr)/(len(inp_thr)*window))

minout3=min(out3)
maxout3=max(out3)
lframe=minout3
rframe=minout3+window
out_thr=[]
while rframe<=maxout3:
    count=0
    for x in out3:
        if x<=rframe and x>=lframe:
            count+=1
    # print(count, lframe, rframe)
    out_thr.append(count)
    lframe+=window
    rframe+=window
print("Output throughput for 20 messages: ",sum(out_thr)/(len(out_thr)*window))
outthr.append(sum(out_thr)/(len(out_thr)*window))

import matplotlib.pyplot as plt
plt.plot([i for i in range (3)], inpthr, 'ro')
plt.plot([i for i in range (3)], outthr, 'bo')
plt.plot([i for i in range (3)], inpthr, 'r--')
plt.plot([i for i in range (3)], outthr, 'b--')
plt.xlabel("Number of messages exchanged")
plt.ylabel("Throughput")
plt.title("Throughput vs Number of messages")
plt.legend(["Input throughput", "Output throughput"])
plt.xticks([i for i in range(3)], [7,10,20])
plt.savefig("Thr_msgs.jpg",dpi=600)
plt.close()