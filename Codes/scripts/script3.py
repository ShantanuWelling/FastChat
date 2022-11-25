#Script for messaging pattern
#This particular script is for 3 messages from a to b and 1 message from b to a

from pwn import *
import os, datetime, time
import mysql.connector

s=process(['python3','server.py'])
p=[]
n=100
for i in range(2):
    # a23="out"+str(i)+".txt"
    p.append(process(['python3','client.py']))
    p[i].sendline(b'R')
    user="GH"+str(i)
    p[i].sendline(bytes(user,'utf-8'))
    p[i].sendline(b'1')
    p[i].sendline(b'P')
    
    
for i in range(2):
    recv="GH"+str((i+1)%2)
    p[i].sendline(bytes(recv,'utf-8'))


#we can change this for loop for various case like for 2 messages from a to b
#and 1 message from b to a
for j in range(3):
    for i in range(1):
    # recv="b"+str((i+1)%2)
    # p[i].sendline(bytes(recv,'utf-8'))
        p[i].sendline(b'M')
        str1="hello"+str(j)
        p[i].sendline(bytes(str1,'utf-8'))
        p[i].sendline(b"m")

        #for 2 messages from a to b and 1 from b to a
        #also for 3 messages from a to b and 1 from b to a

        # if(i==0):
        #     p[i].sendline(b'M')
        #     str1="hi"+str(j)
        #     p[i].sendline(bytes(str1,'utf-8'))
        #     p[i].sendline(b"m")
            # p[i].sendline(b'M')
            # str1="abc"+str(j)
            # p[i].sendline(bytes(str1,'utf-8'))
            # p[i].sendline(b"m")


# with context.local(log_level='info'):
#         data = p[0].clean_and_log()
#         print(data)


# print("+======--=-=-=-----------------------------------")
# print("+======--=-=-=-----------------------------------")
# print("+======--=-=-=-----------------------------------")
# print("+======--=-=-=-----------------------------------")
# print("+======--=-=-=-----------------------------------")
# print(stream())
print("+======--=-=-=-----------------------------------")
print("+======--=-=-=-----------------------------------")
print("+======--=-=-=-----------------------------------")
print("+======--=-=-=-----------------------------------")
print("+======--=-=-=-----------------------------------")

# print(p[1].stream())


# p[1].recvall()

# p[0].recvall()

for j in range(100):
    
    print(p[1].recvline(timeout=0.01))
    
   
for j in range(100):
   
    print(p[0].recvline(timeout=0.01))

mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Harshit123@",
                    database="FASTCHAT"
)
mycursor = mydb.cursor(buffered=True)
myquery2 = "select message from TIME"
mycursor.execute(myquery2)
res=mycursor.fetchall()
# print(res)
res=set(res)
# print(res)
arr = []
inp=[]
out=[]
for x in res:
    mes=x[0]
    sq="SELECT time from TIME where message=%s"
    mycursor.execute(sq,(mes,))
    r1=mycursor.fetchall()
    format_data="%H:%M:%S.%f"
    if(len(r1)==2):
        t1=datetime.datetime.strptime(r1[0][0],format_data)
        t2=datetime.datetime.strptime(r1[1][0],format_data)
        t3=datetime.timedelta(hours=t1.hour, minutes=t1.minute, seconds=t1.second, microseconds=t1.microsecond)
        t4=datetime.timedelta(hours=t2.hour, minutes=t2.minute, seconds=t2.second, microseconds=t2.microsecond)
        time1 = abs(t3-t4)
        
        time1=str(time1)
        time2=time1[-8:]
        time2=float(time2)
        arr.append(time2)
        t3 = str(t3)
        t3=t3[-8:]
        t3=float(t3)
        t4 = str(t4)
        t4=t4[-8:]
        t4=float(t4)
        inp.append(min(t3,t4))
        out.append(max(t3,t4))
        # print(time2)
        print("{0:.10f}".format(time2))
avg = sum(arr)/len(arr)
print("average: ", avg)
   
#input throughput
#output throughput
inp.sort()
out.sort()
print(inp)
print(out)