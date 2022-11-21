import socket
from threading import Thread
import mysql.connector
print("Entered program")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client initialized")
nickname = input("Enter a nickname: ")
print("Entered nickname")
# password=input("Enter password")
while True:
    name2= input("Enter Receiver's Name")
    print("Entered receiver name")

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="--",
    database="FASTCHAT"
    )
    mycursor = mydb.cursor()
    porttoconnect=0
    while True:
        password=input("Enter password")
        mycursor.execute("SELECT name FROM FASTCHAT")

        myresult = mycursor.fetchall()
        check=0

        for x in myresult:
            print(x)
            if(x==nickname):
                check=1
                break
        check2=0
        for y in myresult:
            if(y==name2):
                check2=1
                break
        
        if(check2==1):
            mycursor.execute("SELECT port FROM FASTCHAT where name=%s")
            adr = (name2, )
            mycursor.execute(mycursor, adr)
            myresult = mycursor.fetchall()
            port=0
            for x in myresult:
                port=x
                porttoconnect=x
            if(check==0 ):

                sql = "INSERT INTO customers (name, address,port) VALUES (%s, %s, %s)"
                val = (nickname, password, port)
                mycursor.execute(sql, val)
                break
            else:
                mycursor.execute("SELECT password FROM FASTCHAT where name=%s")
                adr = (nickname )
                mycursor.execute(mycursor, adr)
                myresult = mycursor.fetchall()
                pwd=""
                for x in myresult:
                    pwd=x
                if(pwd==password):
                    print("User Entered")
                    sql="update FASTCHAT set port=%s where name='%s"
                    val=(port,nickname)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    break
                else:
                    print("Wrong Password Entered")
        else:
            name2= input("Enter Receiver's Name")

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
                client.close()
                break


    def send():
        print("Entered into send func")
        # while True:
        #     name2=input("Enter 2nd user: ")
        #     print("entered user2")
        client.send(name2.encode("ascii"))
        while True:
                print("Entered while loop of send func")
                message = f"{nickname}: {input()}"
                print("Took msg from user")
                client.send(message.encode("ascii"))
                print("Sent mssg")
                xinp=input("Enter X to exit")
                if xinp=="X": 
                    x1="Exiting chat"
                    client.send(x1.encode("ascii"))
                    break
                else:
                    x1="Continue"
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
    print("started send thread")