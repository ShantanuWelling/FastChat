import socket
from threading import Thread
from hashlib import sha256
from getpass import getpass
import secrets
from crypt import AESCipher
import mysql.connector
print("Entered program")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client initialized")
signin = input("U want to Register or Login in: R or L")
nickname = ""
check = 0
if signin=="L" :
    while True:
        name = input("Enter a name:")
        password = getpass()
        print("Entered name")

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vatsalya@4A",
            database="FASTCHAT"
        )

        mycursor = mydb.cursor(buffered=True)
        porttoconnect = 0
        mycursor.execute("SELECT name,password FROM CLIENTS")
        myresult = mycursor.fetchall()
        
        for x in myresult:
                print(x)
                if (x[0] == sha256(bytes(name, 'utf-8')).hexdigest() and x[1]==sha256(bytes(password, 'utf-8')).hexdigest()):
                    check = 1
                    break
        if(check==1):
            nickname=name
            break
        else:
            print("Invalid Combination")
else:
    while True:
        c=0
        name = input("Enter a name:")
        
        print("Entered name")

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vatsalya@4A",
            database="FASTCHAT"
        )

        mycursor = mydb.cursor(buffered=True)
        porttoconnect = 0
        mycursor.execute("SELECT name FROM CLIENTS")
        myresult = mycursor.fetchall()
        
        for x in myresult:
                print(x)
                if (x[0] == sha256(bytes(name, 'utf-8')).hexdigest()):
                    c = 1
                    break
        if(c==0):
            nickname=name
            password = getpass()
            p=0
            name1=sha256(bytes(name, 'utf-8')).hexdigest()
            password1=sha256(bytes(password, 'utf-8')).hexdigest()
            pvtkey=''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(32))
            pvtkey=sha256(bytes(pvtkey,'utf-8')).hexdigest()
            sql = ("INSERT INTO CLIENTS (name, password,port, key) VALUES (%s, %s, %s)",(name1, password1, p, pvtkey))
            # sql = ("INSERT INTO favourite (number, info) VALUES (%s, %s)", (numbers, animals))
            mycursor.execute(*sql)
            mydb.commit()
            check=1
          
            break
        else:
            print("UserName Already Taken")
porttoconnect=0

sendkey=0
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vatsalya@4A",
        database="FASTCHAT"
        )
mycursor = mydb.cursor(buffered=True)
mycursor.execute("SELECT key FROM CLIENTS where name=%s",(sha256(bytes(nickname, 'utf-8')).hexdigest(),))
res2=mycursor.fetchall()
sendkey=res2[0]
scipher=AESCipher(sendkey)
# 
# PRITN OFFLINE AND del MSGS
# 
# 
recvkey=0
if check==1:

    print("User Entered")
    while True:
        name2 = input("Enter Receiver's Name")
        print("Entered receiver name")
        check2 = 0
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vatsalya@4A",
        database="FASTCHAT"
        )
        mycursor = mydb.cursor(buffered=True)
        porttoconnect = 0
        mycursor.execute("SELECT name FROM CLIENTS")
        myresult = mycursor.fetchall()
        for y in myresult:
            print(y)
            if (y[0] == sha256(bytes(name2, 'utf-8')).hexdigest()):
                check2 = 1
                break
        if (check2 == 1):
            s="SELECT port FROM CLIENTS where name=%s"
            adr = (sha256(bytes(name2, 'utf-8')).hexdigest(), )
            mycursor.execute(s, adr)
            myresult = mycursor.fetchall()
            port = 0
            for x in myresult:
                print("yes: ",x)
                port = x[0]
                porttoconnect = x[0]
            sql = "update CLIENTS set port=%s where name=%s"
            val = (port, sha256(bytes(nickname, 'utf-8')).hexdigest(),)
            mycursor.execute(sql, val)
            mycursor.execute("SELECT key FROM CLIENTS where name=%s",(adr,))
            res1=mycursor.fetchall()
            recvkey=res1[0]
            mydb.commit()
            break
        else:
            print("No such user exists")

rcipher=AESCipher(recvkey)
if(porttoconnect!=-1):
    client.connect(("127.0.0.1", porttoconnect))
    print("Client connected")
    file = open('myimg.jpeg', 'rb')
    img_data = file.read(2048)
    while img_data:
        client.send(img_data)
        img_data = file.read(2048)
    file.close()

    def recieve():
        """
        Recieving messages from server.
        """
        print("Entered recieve")
        while True:
            print("Entered while loop of receive")
            try:
                print("Entered try of receive")
                message = scipher.decrypt(client.recv(1024))
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
                client.close()
                break

    def send():
        print("Entered into send func")
        # while True:
        #     name2=input("Enter 2nd user: ")
        #     print("entered user2")
        client.send(name2.encode("ascii")) #rname<-name2
        while True:
            print("Entered while loop of send func")
            message = f"{nickname}: {input()}"
            print("Took msg from user")
            client.send(rcipher.encrypt(message))
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
    while True:
        msg=input()
        # 
        # 
        # ADD TO DATABASE OF NAME2 ALONG WITH NAME OF B
        # 
        # 