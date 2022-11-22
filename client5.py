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
# nickname = input("Enter a nickname: ")
# print("Entered nickname")
# password=input("Enter password")
# client.connect(("127.0.0.1", 6961))
# print("Client connected")

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
            p=6963
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

if(porttoconnect!=-1):
    print("PORT TO CONNECT: ",porttoconnect)
    print("NICKNAME IS",nickname)
    client.connect(("127.0.0.1", porttoconnect))
    print("Client connected")
    def recieve():
        """
        Recieving messages from server.
        """
        print("Entered recieve")
        while True:
            print("Entered while loop of receive")
            try:
                print("Entered try of receive")
                message = client.recv(1024).decode("ascii")
                print("Message received")
                if message == "NICK":
                    print("msg recieved is nick")
                    client.send(nickname.encode("ascii"))
                else:
                    print("message received is not nick")
                    print(message)
            except Exception as e:
                print(e)
                print("Some error occured!")
                # client.close()
                break

    def send():
        print("Entered into send func")
        # while True:
        #     name2=input("Enter 2nd user: ")
        #     print("entered user2")
        client.send(rname.encode("ascii"))
        while True:
            print("Entered while loop of send func")
            mystr = input()
            message = nickname + ": " + mystr
            # message = f"{nickname}: {input()}"
            print("Took msg from user")
            client.send(message.encode("ascii"))
            print("Sent mssg")
            xinp = input("Enter X to exit")
            if xinp == "X":
                x1 = "Exiting chat"
                client.send(x1.encode("ascii"))
                break
            else:
                x1 = "Continue"
                client.send(x1.encode("ascii"))

    # recieving thread
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
    client.close()
    print("started send thread")
else:
    print("aa gya")



# def recieve():
#     """
#     Recieving messages from server.
#     """
#     print("Entered recieve")
#     while True:
#         print("Entered while loop of receive")
#         try:
#             print("Entered try of receive")
#             message = client.recv(1024).decode("ascii")
#             print("Message received")
#             if message == "NICK":
#                 print("msg recieved is nick")
#                 client.send(nickname.encode("ascii"))
#             else:
#                 print("message received is not nick")
#                 print(message)
#         except Exception as e:
#             print(e)
#             print("Some error occured!")
#             client.close()
#             break


# def send():
#     print("Entered into send func")
#     while True:
#         name2=input("Enter 2nd user: ")
#         print("entered user2")
#         client.send(name2.encode("ascii"))
#         while True:
#                 print("Entered while loop of send func")
#                 message = f"{nickname}: {input()}"
#                 print("Took msg from user")
#                 client.send(message.encode("ascii"))
#                 print("Sent mssg")
#                 xinp=input("Enter X to exit")
#                 if xinp=="X": 
#                     x1="Exiting chat"
#                     client.send(x1.encode("ascii"))
#                     break
#                 else:
#                     x1="Continue"
#                     client.send(x1.encode("ascii"))



# # recieving thread
# print("Before receiving thread")
# r_thread = Thread(target=recieve)
# print("initialized rec thread")
# r_thread.start()
# print("Started rec thread")

# # sending thread
# print("before send thread init")
# s_thread = Thread(target=send)
# print("init send thread")
# s_thread.start()
# print("started send thread")
