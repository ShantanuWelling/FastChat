import socket
from threading import Thread
import mysql.connector
print("Entered program")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Clien initialized")
signin = input("U want to Register or Login in (R or L):  ")
nickname = ""
check = 0
rname = ""
porttoconnect=0
port=0
c="R"

if signin=="R" :
    while True:
        c=0
        name = input("Enter a name:")
        
        print("Entered name")

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Harshit123@",
            database="FASTCHAT"
        )

        mycursor = mydb.cursor(buffered=True)
        porttoconnect = 0
        mycursor.execute("SELECT name FROM CLIENTS")
        myresult = mycursor.fetchall()
        
        for x in myresult:
                print(x)
                if (x[0] == name):
                    c = 1
                    break
        if(c==0):
            nickname=name
            password = input("Enter password")
            p=-1
            sql = ("INSERT INTO CLIENTS (name, password,port) VALUES (%s, %s, %s)",(name, password, p))
            # sql = ("INSERT INTO favourite (number, info) VALUES (%s, %s)", (numbers, animals))
            mycursor.execute(*sql)
            mydb.commit()
            check=1
          
            break
        else:
            print("UserName Already Taken")
else:
    while True:
        name = input("Enter a name:")
        password = input("Enter password")
        print("Entered name")

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Harshit123@",
            database="FASTCHAT"
        )

        mycursor = mydb.cursor(buffered=True)
        porttoconnect = 0
        mycursor.execute("SELECT name,password FROM CLIENTS")
        myresult = mycursor.fetchall()
        
        for x in myresult:
                print(x)
                if (x[0] == name and x[1]==password):
                    check = 1
                    break
        if(check==1):
            nickname=name
            break
        else:
            print("Invalid Combination")

if check==1:

    mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Harshit123@",
                database="FASTCHAT"
                )

    mycursor = mydb.cursor(buffered=True)

    s1="select * from OFFLINE where reciever = %s"

    offline=(nickname, )

    mycursor.execute(s1, offline)

    myresult = mycursor.fetchall()
    # print("======PENDING CHATS=======")
    for x in myresult:
        print(x[0]," : ",x[2])
        print()

    s2="DELETE FROM OFFLINE WHERE reciever = %s"
    offline2=(nickname, )
    mycursor.execute(s2, offline2)
    mydb.commit()

    print("User Entered")
    while True:
        name2 = input("Enter Receiver's Name")
        print("Entered receiver name")
        check2 = 0
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harshit123@",
        database="FASTCHAT"
        )
        mycursor = mydb.cursor(buffered=True)
        porttoconnect = 0
        mycursor.execute("SELECT name FROM CLIENTS")
        myresult = mycursor.fetchall()
        for y in myresult:
            print(y)
            if (y[0] == name2):
                
                check2 = 1
                break
        if (check2 == 1):
            s="SELECT port FROM CLIENTS where name=%s"
            adr = (name2, )
            mycursor.execute(s, adr)
            myresult = mycursor.fetchall()
            port = 0
            for x in myresult:
                print("yes: ",x)
                port = x[0]
                porttoconnect = x[0]

            sql = "update CLIENTS set port=%s where name=%s"
            val = (port, nickname,)
            mycursor.execute(sql, val)
            mydb.commit()
            rname = name2
            break

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harshit123@",
        database="FASTCHAT"
    )

mycursor = mydb.cursor(buffered=True)
s="SELECT port FROM CLIENTS where name=%s"
adr = (rname, )
mycursor.execute(s, adr)
myresult = mycursor.fetchall()

for x in myresult:
    print("yes: ",x)
    port = x[0]
    porttoconnect = x[0]

sql = "update CLIENTS set port=%s where name=%s"
if porttoconnect==-1 :
    port=6993
val = (port, nickname,)
mycursor.execute(sql, val)
mydb.commit()
# rname = name2

print("PORT TO CONNECT: ",port)
print("NICKNAME IS",nickname)
print(port)
client.connect(("127.0.0.1", port))
print("Client connected")


def recieve():
    global rname
    """
    Recieving messages from server.
    """
    print("Entered recieve")
    while True:
        print("Entered while loop of receive")
        try:
            
            print("Entered try of receive")
            message = client.recv(1024).decode("ascii")
            # print("Message received: ", message)
            if (rname=="X"):
                break
            # if message=="CLOSE":
            #     return
            if message == "NICK":
                print("msg recieved is nick")
                client.send(nickname.encode("ascii"))
            #recieving image from server
            elif message == "Image is incoming from server":
                print("image message recieved in client")
                print("recieving client")
                file = open('finalRecieved.jpeg', 'wb')
                img_data = client.recv(2048)
                while img_data:
                    file.write(img_data)
                    img_data = client.recv(2048)
                file.close()
                print("file recieved at client")
            else:
                print("message received is not nick and not image")
                print(message)
            
            
        except Exception as e:
            print(e)
            print("Some error occured!")
            # client.close()
            break

def send():
    global rname
    global port
    global porttoconnect
    print("Entered into send func")
    global c
    c="R"
    while True:
        if(rname=="X"):
            break
        

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Harshit123@",
            database="FASTCHAT"
        )

        mycursor = mydb.cursor(buffered=True)
        s="SELECT port FROM CLIENTS where name=%s"
        adr = (rname, )
        mycursor.execute(s, adr)
        myresult = mycursor.fetchall()
        
        for x in myresult:
            print("yes: ",x)
            port = x[0]
            porttoconnect = x[0]

        sql = "update CLIENTS set port=%s where name=%s"
        if porttoconnect==-1 :
            port=6993
        val = (port, nickname,)
        mycursor.execute(sql, val)
        mydb.commit()
      
        z=""
        if(porttoconnect!=-1):
            while True:
                client.send(rname.encode("ascii"))
                print("Entered while loop of send func")
                # mystr = input()
                # message = nickname + ": " + mystr
                choice = input("Enter 'M' to send message or 'I' for image: ")
                if(choice=="M"):
                    
                    z=input()
                    
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="Harshit123@",
                            database="FASTCHAT"
                        )

                    mycursor = mydb.cursor(buffered=True)
                    s="SELECT port FROM CLIENTS where name=%s"
                    adr = (rname, )
                    mycursor.execute(s, adr)
                    myresult = mycursor.fetchall()
                    
                    for x in myresult:
                        porttoconnect = x[0]

                    sql = "update CLIENTS set port=%s where name=%s"
                    if porttoconnect==-1 :
                        break



                    message = f"{nickname}: {z}"
                    print("Took msg from user")
                    client.send(message.encode("ascii"))
                    print("Sent mssg")

                else:
                    msg = "Image is incoming"
                    client.send(msg.encode("ascii"))
                    print("Sent image message to server")
                    imgName = input("Enter name of the image: ")
                    print("Sending image to server")
                    file = open(imgName, 'rb')
                    img_data = file.read(2048)
                    while img_data:
                        client.send(img_data)
                        img_data = file.read(2048)
                    file.close()
                    print("Image sent to Server")
                    print("sending sent mssg to server")
                    sentMsg = "Image sent"
                    client.send(sentMsg.encode("ascii"))
                    print("completed sent msg to server")
                
                # OFFLINE MESSAGES

                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Harshit123@",
                database="FASTCHAT"
                )

                mycursor = mydb.cursor(buffered=True)
                
                s1="select * from OFFLINE where reciever = %s"

                offline=(nickname, )

                mycursor.execute(s1, offline)

                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x[0]," : ",x[2])
                    print()

                s2="DELETE FROM OFFLINE WHERE reciever = %s"
                offline2=(nickname, )
                mycursor.execute(s2, offline2)
                mydb.commit()

                xinp = input("Enter X to exit")

                if xinp == "X":
                    
                    # global rname
                    # c=input("You want to close the App (C) or Chat with another person (R)")
                    # if c=="R":
                    #     rname=input("Enter Name of Person u want to chat with now: ")
                    while True:
                        rname=input("Enter Name of Person u want to chat with now:(X for closing)  ")
                        if(rname!="X"):
                            check2 = 0
                            mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="Harshit123@",
                            database="FASTCHAT"
                            )
                            mycursor = mydb.cursor(buffered=True)
                            # porttoconnect = 0
                            mycursor.execute("SELECT name FROM CLIENTS")
                            myresult = mycursor.fetchall()
                            for y in myresult:
                                print(y)
                                if (y[0] == name2):
                                    
                                    check2 = 1
                                    break
                            if (check2 == 1):
                                x1 = "Exiting chat"
                                client.send(x1.encode("ascii"))
                                break
                        else:
                            print("CLosing the CLients")
                            mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="Harshit123@",
                                    database="FASTCHAT"
                                    )
                            mycursor = mydb.cursor(buffered=True)
                            sql = "update CLIENTS set port=%s where name=%s"
                            close=-1
                            val = (close, nickname,)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            x2 = "Closing chat"
                            client.send(x2.encode("ascii"))
                            break
                            # print("Closing the App")
                            # closing="CLOSE"
                            # client.send(closing.encode("ascii")) 
                    break
                else:
                    x1 = "Continue"
                    client.send(x1.encode("ascii"))
                    
      



        if(porttoconnect==-1):
            print("SEND OFFLINE MSG USER NOT ACTIVE")
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Harshit123@",
            database="FASTCHAT"
            )
            mycursor = mydb.cursor(buffered=True)
            if(z!=""):
                myquery2 = "INSERT INTO OFFLINE (sender, reciever, message) VALUES (%s, %s, %s)",(nickname, rname, z)
                mycursor.execute(*myquery2)
                mydb.commit()
            msg=input()
            myquery = "INSERT INTO OFFLINE (sender, reciever, message) VALUES (%s, %s, %s)",(nickname, rname, msg)
            mycursor.execute(*myquery)
            mydb.commit()

            xinp2 = input("Enter X to exit")

            if xinp2 == "X":
                
                # global rname
                # c=input("You want to close the App (C) or Chat with another person (R)")
                # if c=="R":
                #     rname=input("Enter Name of Person u want to chat with now: ")
                while True:
                    rname=input("Enter Name of Person u want to chat with now:(X for closing)  ")
                    if(rname!="X"):
                        check2 = 0
                        mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Harshit123@",
                        database="FASTCHAT"
                        )
                        mycursor = mydb.cursor(buffered=True)
                        # porttoconnect = 0
                        mycursor.execute("SELECT name FROM CLIENTS")
                        myresult = mycursor.fetchall()
                        for y in myresult:
                            print(y)
                            if (y[0] == name2):
                                
                                check2 = 1
                                break
                        if (check2 == 1):
                            # x1 = "Exiting chat"
                            # client.send(x1.encode("ascii"))
                            break
                    else:
                        print("CLosing the CLients")
                        mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="Harshit123@",
                                database="FASTCHAT"
                                )
                        mycursor = mydb.cursor(buffered=True)
                        sql = "update CLIENTS set port=%s where name=%s"
                        close=-1
                        val = (close, nickname,)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        # x2 = "X"
                        client.send(rname.encode("ascii"))
                        break
                        # print("Closing the App")
                        # closing="CLOSE"
                        # client.send(closing.encode("ascii")) 
                
            

















print("Before receiving thread")
r_thread = Thread(target=recieve)
print("initialized rec thread")
r_thread.start()
print("Started rec thread")

# sending thread
print("before send thread init")
s_thread = Thread(target=send)
print("init send thread")
s_thread.start()
# 
# CHANGE ITS PORT NUMBER TO -1
# 
# 

print("started send thread")
# CHANGE PORT TO -1 BEFORE CLOSING THE SERVER

