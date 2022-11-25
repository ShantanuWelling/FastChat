import load
import socket
from threading import Thread
import mysql.connector
from hashlib import sha256
from getpass import getpass
import secrets
import string
from crypt import AESCipher
import base64
from datetime import datetime
from datetime import timedelta
import sys
# print("Entered program")


CB = load.ClientBalance()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print("Client initialized")
signin = input("U want to Register or Login in (R or L):  ")
nickname = ""
check = 0
rname = ""
porttoconnect = 0
port = 0
c = "R"

if signin == "R":
    while True:
        c = 0
        name = input("Enter a name:")

        # print("Entered name")

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
            # print(x)
            if (x[0] == name):
                c = 1
                break
        if (c == 0):
            nickname = name
            # print("WNtwe jsfnj")
            # password = getpass()
            password=input("Enter Password")
            # print("kd")
            p = -1
            pvtkey = ''.join(secrets.choice(string.ascii_uppercase +
                             string.digits + string.ascii_lowercase) for i in range(16))
            # pvtkey=bytes(pvtkey,'utf-8')
            enc_pass = sha256(bytes(password, 'utf-8')).hexdigest()
            sql = ("INSERT INTO CLIENTS (name, password,port,pkey) VALUES (%s, %s, %s, %s)",
                   (name, enc_pass, p, pvtkey))
            # sql = ("INSERT INTO favourite (number, info) VALUES (%s, %s)", (numbers, animals))
            mycursor.execute(*sql)
            mydb.commit()
            check = 1

            break
        else:
            print("UserName Already Taken")
else:
    while True:
        name = input("Enter a name:")
        password = getpass()
        # print("Entered name")

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
            # print(x)
            if (x[0] == name and x[1] == sha256(bytes(password, 'utf-8')).hexdigest()):
                check = 1
                break
        if (check == 1):
            nickname = name
            break
        else:
            print("Invalid Combination")

if check == 1:

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vatsalya@4A",
        database="FASTCHAT"
    )

    mycursor = mydb.cursor(buffered=True)
    s2 = "select pkey from CLIENTS where name=%s"  # start
    mycursor.execute(s2, (nickname,))
    res = mycursor.fetchall()
    mykey = res[0][0]
    # print(mykey)
    sendcip = AESCipher(mykey)  # end

    s1 = "select * from OFFLINE where reciever = %s"

    offline = (nickname, )

    mycursor.execute(s1, offline)

    myresult = mycursor.fetchall()
    # print("======PENDING CHATS=======")
    for x in myresult:
        print(x[0], " : ", sendcip.msg_decrypt(x[2]))
        print()

    s2 = "DELETE FROM OFFLINE WHERE reciever = %s"
    offline2 = (nickname, )
    mycursor.execute(s2, offline2)
    mydb.commit()

    ####
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vatsalya@4A",
        database="FASTCHAT"
    )

    mycursor = mydb.cursor(buffered=True)

    s3 = "select * from IMAGES where reciever = %s"

    off = (nickname, )

    mycursor.execute(s3, off)

    myresult2 = mycursor.fetchall()

    for x in myresult2:
        print("Image from ", x[0])
        msg2 = bytes(x[2], "utf-8")
        msg3 = base64.decodebytes(msg2)
        file = open("ReceivedImg.jpg", "wb")
        file.write(msg3)
        file.close()
        from PIL import Image
        img = Image.open("ReceivedImg.jpg")
        img.show()

        print()

    s4 = "DELETE FROM IMAGES WHERE reciever = %s"
    offline3 = (nickname, )
    mycursor.execute(s4, offline3)
    mydb.commit()
    # print("User Entered")

# while True:
type2 = input(
    "ENTER GR: GROUP MESSAGING  || P: PERSONAL MESSAGING || X: LEAVE CHAT")

if type2 == "P":
    notexit=0
    if check == 1:
        while True:
            name2 = input("Enter Receiver's Name")
            # print("Entered receiver name")
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
                # print(y)
                if (y[0] == name2):

                    check2 = 1
                    break
            if (check2 == 1):
                s = "SELECT port FROM CLIENTS where name=%s"
                adr = (name2, )
                mycursor.execute(s, adr)
                myresult = mycursor.fetchall()
                port = 0
                for x in myresult:
                    # print("yes: ", x)
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
        password="Vatsalya@4A",
        database="FASTCHAT"
    )

    mycursor = mydb.cursor(buffered=True)
    s = "SELECT port FROM CLIENTS where name=%s"
    adr = (rname, )
    mycursor.execute(s, adr)
    myresult = mycursor.fetchall()

    for x in myresult:
        # print("yes: ", x)
        port = x[0]
        porttoconnect = x[0]

    sql = "update CLIENTS set port=%s where name=%s"
    if porttoconnect == -1:
        port = CB.Addconn()
    else:
        CB.incrementconn(port)
    val = (port, nickname,)
    mycursor.execute(sql, val)
    mydb.commit()
    # rname = name2

    print("PORT TO CONNECT: ", port)
    print("NICKNAME IS", nickname)
    # print(port)
    client.connect(("127.0.0.1", port))
    # print("Client connected")

    s6 = "select pkey from CLIENTS where name=%s"  # start
    mycursor.execute(s6, (rname,))
    res1 = mycursor.fetchall()
    reckey = res1[0][0]
    # print(reckey)
    recvcip = AESCipher(reckey)  # end

    def recieve():
        """This function is implemented to recieve messages from the server. The message can be Image or text. Both cases are handeled differently. If a Image is recieved then first a message indicating that a image is incoming is recieved so that the client knows that it has to now recieve image.
        """
        global rname
        global sendcip
        """
        Recieving messages from server.
        """
        # print("Entered recieve")
        while True:
            # print("Entered while loop of receive")
            try:

                # print("Entered try of receive")
                message = client.recv(1048576).decode("ascii")
                # print("Received Something")
                # message = sendcip.msg_decrypt(message) ##
                # print("Message received: ", message)
                if (rname == "X"):
                    break
                # if message=="CLOSE":
                #     return
                if message == "TESTNAME":
                    # print("msg recieved is testname")
                    client.send(nickname.encode("ascii"))
                    

                elif message[0:17] == "Image is incoming":
                    # print("Image looping")
                    msg2 = message[17:]
                    # msg2 = sendcip.msg_decrypt(msg)
                    msg2 = bytes(msg2, "utf-8")
                    msg3 = base64.decodebytes(msg2)
                    file = open("ReceivedImg.jpg", 'wb')
                    file.write(msg3)
                    file.close()
                    from PIL import Image
                    img = Image.open('ReceivedImg.jpg')
                    img.show()

                else:
                    # print("In Else")
                    # print(message)
                    message = sendcip.msg_decrypt(message)
                    # print("message received is not nick")
                    print(message)
                    # print("][][]][][][][]")
                    # print("][][]][][][][]")
                    print("Msg Received by ",nickname)
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Vatsalya@4A",
                        database="FASTCHAT"
                    )
                    mycursor = mydb.cursor(buffered=True)
                    t=datetime.now().time()
                    t=str(t)
                    myquery2 = "INSERT INTO TIME (message, time) VALUES (%s, %s)", (
                                message,t)
                    mycursor.execute(*myquery2)
                    mydb.commit()
                    # print("][][]][][][][]")
                    # print("][][]][][][][]")

            except Exception as e:
                # print(e)
                print("Some error occured!")
                # client.close()
                break

    def send():
        """This function is used to send messages to the server which sends messages to another client. Here also the messages can be image or text. For image it takes image name as input from the user and for text it takes the message as input from the user. If another client is offline then the messages are stored in a database of MySQL which are redirected to the client when it comes online. The messages stored in the database or sent to the client are first encrypted for implementing E2E encryption. 
        """
        global rname
        global port
        global porttoconnect
        global recvcip
        global sendcip
        # print("Entered into send func")
        global c
        c = "R"
        while True:
            if (rname == "X"):
                break

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Vatsalya@4A",
                database="FASTCHAT"
            )

            mycursor = mydb.cursor(buffered=True)
            s = "SELECT port FROM CLIENTS where name=%s"
            adr = (rname, )
            mycursor.execute(s, adr)
            myresult = mycursor.fetchall()

            for x in myresult:
                # print("yes: ", x)
                port = x[0]
                porttoconnect = x[0]

            # sql = "update CLIENTS set port=%s where name=%s"
            # if porttoconnect==-1 :
            #     port=ClientBalance
            # val = (port, nickname,)
            # mycursor.execute(sql, val)
            # mydb.commit()

            z = ""
            str1 = ""
            choice = "N"
            choice5 = "N"
            if (porttoconnect != -1):
                while True:
                    client.send(rname.encode("ascii"))
                    # print("Entered while loop of send func")
                    # mystr = input()
                    # message = nickname + ": " + mystr
                    choice = input("ENTER M FOR MESSAGE OR I FOR IMAGE: ")
                    if choice == "M":
                        # msg = "Text is incoming"
                        # client.send(msg.encode("ascii"))
                        z = input()
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="Vatsalya@4A",
                            database="FASTCHAT"
                        )
                        mycursor = mydb.cursor(buffered=True)
                        s = "SELECT port FROM CLIENTS where name=%s"
                        adr = (rname, )
                        mycursor.execute(s, adr)
                        myresult = mycursor.fetchall()

                        for x in myresult:
                            porttoconnect = x[0]

                        sql = "update CLIENTS set port=%s where name=%s"
                        if porttoconnect == -1:
                            choice5 = "B"
                            break
                        message = f"{nickname}: {z}"
                        # print("Took msg from user")
                        msg1 = recvcip.msg_encrypt(message)
                        client.send(msg1.encode("ascii"))
                        # print("//////////////")
                        # print("//////////////")
                        print("Msg Sent by ",nickname)
                        mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Vatsalya@4A",
                        database="FASTCHAT"
                        )
                        mycursor = mydb.cursor(buffered=True)
                        t=datetime.now().time()
                        t=str(t)
                        myquery2 = "INSERT INTO TIME (message, time) VALUES (%s, %s)", (
                                    message,t)
                        mycursor.execute(*myquery2)
                        mydb.commit()
                        # print("//////////////")
                        # print("//////////////")
                        
                        ##TIME MODUle
                        print("Sent mssg")

                    elif choice == "I":
                        msg = "Image is incoming"
                        client.send(msg.encode("ascii"))
                        # print("Sent image message to server")
                        imgName = input("Enter name of the image: ")
                        # print("Sending image to server")

                        file = open(imgName, 'rb')
                        img_data = file.read()
                        str1 = base64.encodebytes(img_data)
                        str1 = str(str1, "utf-8")
                        # str2=recvcip.msg_encrypt(str1)
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="Vatsalya@4A",
                            database="FASTCHAT"
                        )
                        mycursor = mydb.cursor(buffered=True)
                        s = "SELECT port FROM CLIENTS where name=%s"
                        adr = (rname, )
                        mycursor.execute(s, adr)
                        myresult = mycursor.fetchall()

                        for x in myresult:
                            porttoconnect = x[0]

                        sql = "update CLIENTS set port=%s where name=%s"
                        if porttoconnect == -1:
                            choice5 = "B"
                            break
                        client.send(str1.encode("ascii"))

                        file.close()

                    # OFFLINE MESSAGES

                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Vatsalya@4A",
                        database="FASTCHAT"
                    )

                    mycursor = mydb.cursor(buffered=True)

                    s1 = "select * from OFFLINE where reciever = %s"

                    offline = (nickname, )

                    mycursor.execute(s1, offline)

                    myresult = mycursor.fetchall()

                    for x in myresult:
                        print(x[0], " : ", sendcip.msg_decrypt(x[2]))
                        print()

                    s2 = "DELETE FROM OFFLINE WHERE reciever = %s"
                    offline2 = (nickname, )
                    mycursor.execute(s2, offline2)
                    mydb.commit()

                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Vatsalya@4A",
                        database="FASTCHAT"
                    )

                    mycursor = mydb.cursor(buffered=True)

                    s3 = "select * from IMAGES where reciever = %s"

                    off = (nickname, )

                    mycursor.execute(s3, off)

                    myresult2 = mycursor.fetchall()

                    for x in myresult2:
                        print("Image from ", x[0])
                        msg2 = bytes(x[2], "utf-8")
                        msg3 = base64.decodebytes(msg2)
                        file = open("ReceivedImg.jpg", "wb")
                        file.write(msg3)
                        file.close()
                        from PIL import Image
                        img = Image.open("ReceivedImg.jpg")
                        img.show()

                        print()

                    s4 = "DELETE FROM IMAGES WHERE reciever = %s"
                    offline3 = (nickname, )
                    mycursor.execute(s4, offline3)
                    mydb.commit()

                    xinp = input("Enter X to exit")

                    if xinp == "X":

                        # global rname
                        # c=input("You want to close the App (C) or Chat with another person (R)")
                        # if c=="R":
                        #     rname=input("Enter Name of Person u want to chat with now: ")
                        while True:
                            rname = input(
                                "Enter Name of Person u want to chat with now:(X for closing)  ")
                            if (rname != "X"):
                                check2 = 0
                                mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="Vatsalya@4A",
                                    database="FASTCHAT"
                                )
                                mycursor = mydb.cursor(buffered=True)
                                # porttoconnect = 0
                                mycursor.execute(
                                    "SELECT name FROM CLIENTS")
                                myresult = mycursor.fetchall()
                                for y in myresult:
                                    # print(y)
                                    if (y[0] == name2):

                                        check2 = 1
                                        break
                                if (check2 == 1):
                                    x1 = "Exiting chat"
                                    client.send(x1.encode("ascii"))
                                    break
                            else:
                                # print("CLosing the CLients")
                                mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="Vatsalya@4A",
                                    database="FASTCHAT"
                                )
                                mycursor = mydb.cursor(buffered=True)
                                s4 = "select port from CLIENTS where name=%s"
                                ad = (nickname, )
                                mycursor.execute(s4, ad)
                                r = mycursor.fetchall()
                                porttochange = 0
                                for x in r:
                                    porttochange = x[0]
                                CB.delconn(porttochange)
                                sql = "update CLIENTS set port=%s where name=%s"
                                close = -1
                                val = (close, nickname,)
                                mycursor.execute(sql, val)
                                mydb.commit()

                                x2 = "Closing chat"
                                client.send(x2.encode("ascii"))
                                notexit=1
                                break
                                # print("Closing the App")
                                # closing="CLOSE"
                                # client.send(closing.encode("ascii"))
                        break
                    else:
                        x1 = "Continue"
                        client.send(x1.encode("ascii"))

            if (porttoconnect == -1):
                print("SEND OFFLINE MSG USER NOT ACTIVE")
                if (choice5 != "B"):
                    choice2 = input("ENTER M FOR MESSAGE OR I FOR IMAGE: ")
                    if choice2 == "M":

                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="Vatsalya@4A",
                            database="FASTCHAT"
                        )
                        mycursor = mydb.cursor(buffered=True)
                        if (z != ""):
                            encz = recvcip.msg_encrypt(z)
                            myquery2 = "INSERT INTO OFFLINE (sender, reciever, message) VALUES (%s, %s, %s)", (
                                nickname, rname, encz)
                            mycursor.execute(*myquery2)
                            mydb.commit()
                        msg = input()
                        encmsg = recvcip.msg_encrypt(msg)
                        myquery = "INSERT INTO OFFLINE (sender, reciever, message) VALUES (%s, %s, %s)", (
                            nickname, rname, encmsg)
                        mycursor.execute(*myquery)
                        mydb.commit()
                    else:
                        # msg = "Image is incoming"
                        # client.send(msg.encode("ascii"))
                        # print("Sent image message to server")
                        imgName = input("Enter name of the image: ")
                        # print("Sending image to server")
                        # file = open(imgName, 'rb')
                        # img_data = file.read()
                        # count=0
                        # while img_data:
                        #     count=count+1
                        #     img_data = file.read()
                        # file.close()
                        # client.send(str(count-1).encode("ascii"))
                        file = open(imgName, 'rb')
                        img_data = file.read()
                        str1 = base64.encodebytes(img_data)
                        str1 = str(str1, "utf-8")
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="Vatsalya@4A",
                            database="FASTCHAT"
                        )
                        mycursor = mydb.cursor(buffered=True)
                        myquery = "INSERT INTO IMAGES (sender, reciever, message) VALUES (%s, %s, %s)", (
                            nickname, rname, str1)
                        mycursor.execute(*myquery)
                        mydb.commit()
                        file.close()
                        # str2=recvcip.msg_encrypt(str1)
                        # client.send(str1.encode("ascii"))

                else:
                    if (choice == "M"):
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="Vatsalya@4A",
                            database="FASTCHAT"
                        )
                        mycursor = mydb.cursor(buffered=True)
                        if (z != ""):
                            encz = recvcip.msg_encrypt(z)
                            myquery2 = "INSERT INTO OFFLINE (sender, reciever, message) VALUES (%s, %s, %s)", (
                                nickname, rname, encz)
                            mycursor.execute(*myquery2)
                            mydb.commit()
                        msg = input()
                        encmsg = recvcip.msg_encrypt(msg)
                        myquery = "INSERT INTO OFFLINE (sender, reciever, message) VALUES (%s, %s, %s)", (
                            nickname, rname, encmsg)
                        mycursor.execute(*myquery)
                        mydb.commit()

                    elif (choice == "I"):
                        if str1 != "":
                            # client.send(str(count-1).encode("ascii"))
                            file = open(imgName, 'rb')
                            img_data = file.read()
                            str1 = base64.encodebytes(img_data)
                            str1 = str(str1, "utf-8")
                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="Vatsalya@4A",
                                database="FASTCHAT"
                            )
                            myquery = "INSERT INTO IMAGES (sender, reciever, message) VALUES (%s, %s, %s)", (
                                nickname, rname, str1)
                            mycursor.execute(*myquery)
                            mydb.commit()
                            file.close()

                        imgName = input("Enter name of the image: ")
                        # client.send(str(count-1).encode("ascii"))
                        file = open(imgName, 'rb')
                        img_data = file.read()
                        str1 = base64.encodebytes(img_data)
                        str1 = str(str1, "utf-8")
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="Vatsalya@4A",
                            database="FASTCHAT"
                        )
                        myquery = "INSERT INTO IMAGES (sender, reciever, message) VALUES (%s, %s, %s)", (
                            nickname, rname, str1)
                        mycursor.execute(*myquery)
                        mydb.commit()
                        file.close()

                xinp2 = input("Enter X to exit")

                if xinp2 == "X":

                    # global rname
                    # c=input("You want to close the App (C) or Chat with another person (R)")
                    # if c=="R":
                    #     rname=input("Enter Name of Person u want to chat with now: ")
                    while True:
                        rname = input(
                            "Enter Name of Person u want to chat with now:(X for closing)  ")
                        if (rname != "X"):
                            check2 = 0
                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="Vatsalya@4A",
                                database="FASTCHAT"
                            )
                            mycursor = mydb.cursor(buffered=True)
                            # porttoconnect = 0
                            mycursor.execute("SELECT name FROM CLIENTS")
                            myresult = mycursor.fetchall()
                            for y in myresult:
                                # print(y)
                                if (y[0] == name2):

                                    check2 = 1
                                    break
                            if (check2 == 1):
                                # x1 = "Exiting chat"
                                # client.send(x1.encode("ascii"))
                                break
                        else:
                            # print("CLosing the CLients")
                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="Vatsalya@4A",
                                database="FASTCHAT"
                            )
                            mycursor = mydb.cursor(buffered=True)
                            sql = "update CLIENTS set port=%s where name=%s"
                            close = -1
                            val = (close, nickname,)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            # x2 = "X"
                            client.send(rname.encode("ascii"))
                            notexit=1
                            break
                            # print("Closing the App")
                            # closing="CLOSE"
                            # client.send(closing.encode("ascii"))
    # print("Before receiving thread")
    r_thread = Thread(target=recieve)
    # print("initialized rec thread")
    r_thread.start()
    # print("Started rec thread")

    # sending thread
    # print("before send thread init")
    s_thread = Thread(target=send)
    # print("init send thread")
    s_thread.start()
    #
    # CHANGE ITS PORT NUMBER TO -1
    #
    #

    # print("started send thread")
    # while notexit==0:
    #     pass

    # z=input("WANT TO EXIT THE WHILE LOOP")
    # CHANGE PORT TO -1 BEFORE CLOSING THE SERVER
elif type2=="GR":
    type1 = input(
    "ENTER C: CREATE GROUP || G: MESSAGE/ADD/DELETE MEMBERS IN GROUP || X: LEAVE CHAT")
    if type1 == "C":
        name1 = input("Enter Name of Group")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vatsalya@4A",
            database="FASTCHAT"
        )

        mycursor = mydb.cursor(buffered=True)
        sql = ("INSERT INTO group1 (groupname, admin, member) VALUES (%s, %s, %s)",
            (name1, nickname, nickname))
        mycursor.execute(*sql)
        mydb.commit()

        while True:
            # while True:
            a = input("Enter Name of Group Member (ENTER X TO FINISH)")
            if (a != "X"):
                d = 0
                mycursor.execute("SELECT name FROM CLIENTS")
                myresult = mycursor.fetchall()

                for x in myresult:
                    # print(x)
                    if (x[0] == a):
                        d = 1
                        break
                if (d == 1):
                    sql = (
                        "INSERT INTO group1 (groupname, admin, member) VALUES (%s, %s, %s)", (name1, nickname, a))
                    mycursor.execute(*sql)
                    mydb.commit()
                else:
                    print("User Doesnt Exist")
            else:
                break
    elif type1 == "G":
        ###
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vatsalya@4A",
        database="FASTCHAT"
        )

        mycursor = mydb.cursor(buffered=True)
        s2 = "select pkey from CLIENTS where name=%s"  # start
        mycursor.execute(s2, (nickname,))
        res = mycursor.fetchall()
        mykey = res[0][0]
        # print(mykey)
        sendcip = AESCipher(mykey)  # end

        s1 = "select * from OFFLINE where reciever = %s"

        offline = (nickname, )

        mycursor.execute(s1, offline)

        myresult = mycursor.fetchall()
        # print("======PENDING CHATS=======")
        for x in myresult:
            print(x[0], " : ", sendcip.msg_decrypt(x[2]))
            print()

        s2 = "DELETE FROM OFFLINE WHERE reciever = %s"
        offline2 = (nickname, )
        mycursor.execute(s2, offline2)
        mydb.commit()

        ####
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vatsalya@4A",
            database="FASTCHAT"
        )

        mycursor = mydb.cursor(buffered=True)

        s3 = "select * from IMAGES where reciever = %s"

        off = (nickname, )

        mycursor.execute(s3, off)

        myresult2 = mycursor.fetchall()

        for x in myresult2:
            print("Image from ", x[0])
            msg2 = bytes(x[2], "utf-8")
            msg3 = base64.decodebytes(msg2)
            file = open("ReceivedImg.jpg", "wb")
            file.write(msg3)
            file.close()
            from PIL import Image
            img = Image.open("ReceivedImg.jpg")
            img.show()

            print()

        s4 = "DELETE FROM IMAGES WHERE reciever = %s"
        offline3 = (nickname, )
        mycursor.execute(s4, offline3)
        mydb.commit()
        ###
        # name1=input("Enter Name of Group")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vatsalya@4A",
            database="FASTCHAT"
        )

        mycursor = mydb.cursor(buffered=True)
        sql = "SELECT * from group1 where member=%s"
        adr = (nickname, )
        mycursor.execute(sql, adr)
        r = mycursor.fetchall()
        # for i in r:
        #     print(i[0])
        groupinfo = ""
        while True:
            a = input("Enter Name of group you want to chat with: (Enter X is exist) ")
            grpexist = False
            for i in r:
                if a == i[0]:
                    groupinfo = i
                    grpexist = True
                    break
            if (grpexist):
                break
            elif(a=="X"):
                break
            else:
                print("Invalid Group")
        isadmin = 0
        if(groupinfo==""):
            pass
        
        elif (groupinfo[1] == nickname):
            while True:

                ###############
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Vatsalya@4A",
                    database="FASTCHAT"
                )

                mycursor = mydb.cursor(buffered=True)
                s2 = "select pkey from CLIENTS where name=%s"  # start
                mycursor.execute(s2, (nickname,))
                res = mycursor.fetchall()
                mykey = res[0][0]
                # print(mykey)
                sendcip = AESCipher(mykey)  # end

                s1 = "select * from OFFLINE where reciever = %s"

                offline = (nickname, )

                mycursor.execute(s1, offline)

                myresult = mycursor.fetchall()
                # print("======PENDING CHATS=======")
                for x in myresult:
                    print(x[0], " : ", sendcip.msg_decrypt(x[2]))
                    print()

                s2 = "DELETE FROM OFFLINE WHERE reciever = %s"
                offline2 = (nickname, )
                mycursor.execute(s2, offline2)
                mydb.commit()

                ####
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Vatsalya@4A",
                    database="FASTCHAT"
                )

                mycursor = mydb.cursor(buffered=True)

                s3 = "select * from IMAGES where reciever = %s"

                off = (nickname, )

                mycursor.execute(s3, off)

                myresult2 = mycursor.fetchall()

                for x in myresult2:
                    print("Image from ", x[0])
                    msg2 = bytes(x[2], "utf-8")
                    msg3 = base64.decodebytes(msg2)
                    file = open("ReceivedImg.jpg", "wb")
                    file.write(msg3)
                    file.close()
                    from PIL import Image
                    img = Image.open("ReceivedImg.jpg")
                    img.show()

                    print()

                s4 = "DELETE FROM IMAGES WHERE reciever = %s"
                offline3 = (nickname, )
                mycursor.execute(s4, offline3)
                mydb.commit()
                ##############

                k = input(
                    "A to add member || D to delete member || M to send message || X to exit")
                if (k == "A"):
                    while True:
                        w = 0
                        nameUser = input("Enter name of user to add: ")
                        for i in r:
                            if (i[0] == groupinfo[0] and i[2] == nameUser):
                                w = 1
                                break
                        if (w):
                            print("User already exists in the group")
                        else:
                            d = 0
                            mycursor.execute("SELECT name FROM CLIENTS")
                            myresult = mycursor.fetchall()

                            for x in myresult:
                                if (x[0] == a):
                                    d = 1
                                    break
                            if (d == 1):
                                s1 = "insert into group1 (groupname, admin, member) VALUES (%s, %s, %s)", (
                                    groupinfo[0], groupinfo[1], nameUser)
                                mycursor.execute(*s1)
                                mydb.commit()
                                break
                            else:
                                print("User does not exist Try Again...")
                elif (k == "D"):
                    while True:
                        w = 0
                        nameUser = input("Enter name of user to remove: ")
                        for i in r:
                            if (i[0] == groupinfo[0] and i[2] == nameUser):
                                w = 1
                                s1 = "delete from group1 where groupname=%s and member=%s"
                                g1 = (groupinfo[0], nameUser, )
                                mycursor.execute(s1, g1)
                                mydb.commit()
                                break
                        if (w):
                            break
                        else:
                            print("Invalid UserName")
                elif (k == "M"):
                

                    msg = input("Enter message: ")
                    q1 = "select * from group1 where groupname = %s"
                    s2 = (groupinfo[0], )
                    mycursor.execute(q1, s2)
                    r1 = mycursor.fetchall()
                    for i in r1:
                        receiver = i[2]
                        # a=nickname
                        sender = groupinfo[0]+"::"+nickname
                        if (nickname != receiver):
                            q2="SELECT pkey from CLIENTS where name=%s"
                            mycursor.execute(q2,(receiver,))
                            r3=mycursor.fetchall()
                            b4=AESCipher(r3[0][0])
                            query = "INSERT into OFFLINE (sender, reciever, message) VALUES (%s, %s, %s)", (
                                sender, receiver, b4.msg_encrypt(msg))
                            mycursor.execute(*query)
                            mydb.commit()
                elif (k == "X"):
                    break
                else:
                    print("Invalid input, Try again")
        else:
            while True:
                #####
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Vatsalya@4A",
                    database="FASTCHAT"
                )

                mycursor = mydb.cursor(buffered=True)
                s2 = "select pkey from CLIENTS where name=%s"  # start
                mycursor.execute(s2, (nickname,))
                res = mycursor.fetchall()
                mykey = res[0][0]
                # print(mykey)
                sendcip = AESCipher(mykey)  # end

                s1 = "select * from OFFLINE where reciever = %s"

                offline = (nickname, )

                mycursor.execute(s1, offline)

                myresult = mycursor.fetchall()
                # print("======PENDING CHATS=======")
                for x in myresult:
                    print(x[0], " : ", sendcip.msg_decrypt(x[2]))
                    print()

                s2 = "DELETE FROM OFFLINE WHERE reciever = %s"
                offline2 = (nickname, )
                mycursor.execute(s2, offline2)
                mydb.commit()

                ####
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Vatsalya@4A",
                    database="FASTCHAT"
                )

                mycursor = mydb.cursor(buffered=True)

                s3 = "select * from IMAGES where reciever = %s"

                off = (nickname, )

                mycursor.execute(s3, off)

                myresult2 = mycursor.fetchall()

                for x in myresult2:
                    print("Image from ", x[0])
                    msg2 = bytes(x[2], "utf-8")
                    msg3 = base64.decodebytes(msg2)
                    file = open("ReceivedImg.jpg", "wb")
                    file.write(msg3)
                    file.close()
                    from PIL import Image
                    img = Image.open("ReceivedImg.jpg")
                    img.show()

                    print()

                s4 = "DELETE FROM IMAGES WHERE reciever = %s"
                offline3 = (nickname, )
                mycursor.execute(s4, offline3)
                mydb.commit()
                #####


                k = input("M to message || X to exit || L to leave group")
                if (k == "M"):
                    msg = input("Enter message: ")
                    q1 = "select * from group1 where groupname = %s"
                    s2 = (groupinfo[0], )
                    mycursor.execute(q1, s2)
                    r1 = mycursor.fetchall()
                    for i in r1:
                        receiver = i[2]
                        sender = groupinfo[0]+"::"+nickname
                        if (nickname != receiver):
                            q2="SELECT pkey from CLIENTS where name=%s"
                            mycursor.execute(q2,(receiver,))
                            r3=mycursor.fetchall()
                            b4=AESCipher(r3[0][0])
                            query = "INSERT into OFFLINE (sender, reciever, message) VALUES (%s, %s, %s)", (
                                sender, receiver, b4.msg_encrypt(msg))
                            mycursor.execute(*query)
                            mydb.commit()
                elif (k == "L"):
                    s = "delete from group1 where groupname=%s and member=%s"
                    g = (groupinfo[0], groupinfo[2], )
                    mycursor.execute(s, g)
                    mydb.commit()
                    break
                elif (k == "X"):
                    break
                else:
                    print("Invalid input, Try again")
elif (type2 == "X"):
    print("Exit")

# f.close()
