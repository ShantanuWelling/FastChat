import socket
from threading import Thread
import mysql.connector
import load

#creating a object of ServerBalance class from file load.py
SB= load.ServerBalance()

#connecting to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Vatsalya@4A"
)

#creating database FASTCHAT
mycursor1 = mydb.cursor(buffered=True)
mycursor1.execute("SHOW DATABASES")
mycursor1.execute("CREATE DATABASE IF NOT EXISTS FASTCHAT")

#connecting to database
mydb2 = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Vatsalya@4A",
  database="FASTCHAT"
)
mycursor = mydb2.cursor(buffered=True)

#creating required tables
mycursor.execute("CREATE TABLE IF NOT EXISTS CLIENTS (name VARCHAR(255) PRIMARY KEY, password VARCHAR(255), port int, pkey longtext)")
mycursor.execute("CREATE TABLE IF NOT EXISTS OFFLINE (sender VARCHAR(255), reciever VARCHAR(255), message longtext)")
mycursor.execute("CREATE TABLE IF NOT EXISTS IMAGES (sender VARCHAR(255), reciever VARCHAR(255), message longtext)")
mycursor.execute("CREATE TABLE IF NOT EXISTS GROUP1 (groupname VARCHAR(255), admin VARCHAR(255), member longtext)")
mycursor.execute("CREATE TABLE IF NOT EXISTS TIME (message longtext, time VARCHAR(255))")

# local host and port
host = "127.0.0.1"
#TAKING PORT NUMBER FORM LOAD BALANCER
port =  SB.PortAllocation()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("127.0.0.1", port))
# print("BIDNING")
server.bind((host, port))
# print("LISTING ")
server.listen()
# print("STARTING")

clients = []
nicknames = []

def broadcast(message):
    """This function is used to broadcast messages to all the clients.

    :param message: This is the message which is to be broadcasted to the clients.
    :type message: string
    """
    for client in clients:
        # print("SENDING MESSAGE TO A CLIENT")
        client.send(message)

def sender(message,name):
    """
    This function is used to send message to a particluar client.

    :param message: This is the message which is to be sent to the client.
    :type message: string
    :param name: Name of the client to which we want to send message.
    :type name: string
    """
    i=0
    # print("STARTING FOR LOOP")
    for client in clients:
        # print("h17")
        if(nicknames[i]==name):
            # print("h18")
            client.send(message)
        i=i+1



def handle(client):
    """
    This function Handles a client at a time. It recieves a message from a client and then calls the send function to send the message to another client. The message can be image or text. Both cases are handeled differently. It can also close the connection.

    :param client: Used to send and recieve the message from/to the clients.
    :type client: socket
    """
    while True:
        # print("Handle Function Started")
        try:
            r2 = client.recv(1024).decode("ascii")
            if(r2=="X"):
                raise Exception
            while True:
                message = client.recv(1024)
                if(message.decode("ascii")=="Image is incoming"):
                    
                    # print("Image message came to server")
                    # print("recieving image into server")
                    s2=client.recv(1048576)
                    sender(message,r2)
                    sender(s2,r2)
                else:
                    # print("RECIEVING MESSAGE FROM CLIENT")
                    # name=client.recv(1024)
                    
                    # print("BROADCASTING MES")
                    sender(message,r2)
                    # print("DISPLAYED")

                next=client.recv(1024).decode("ascii")
                # print("NEXT CHECKED")
                if(next=="Exiting chat"):
                    # print("Breaking")
                    break
                elif(next=="Closing chat"):
                    raise Exception
                elif(next=="X"):
                    raise Exception
                else:
                    pass
                # print("Over")
        except Exception as e:
            # print("Inside Excepton of Handle")
            index = clients.index(client)
            # print("Index is : ",index)
            clients.pop(index)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            # broadcast(f"{nickname} has left the chat!".encode("ascii"))
            
            break

def receive():
    """
    Recieves connection requests from the clients. Also starts the connection with the client if a new client joins.
    """
    # print("STARTING RECIEVE")
    while True:
        # print("INSIDE RECIENCE TRUE")
        client, address = server.accept()
        # print("ACCEPTING FROM SERVER")
        print("Connected with {}".format(str(address)))
        # print("SENDING TO CLIENT")

        client.send("TESTNAME".encode("ascii"))
        # print("SENT")
        nickname =  client.recv(1024).decode("ascii")
        # print("RECEIVING TESTNAME")
        nicknames.append(nickname)
        # print("NICKNAME ADDED")
        clients.append(client)
        # print("CLIENT ADDED")

        print(f"Name of the client  is {nickname}!")
        # print("MESSAGE BROADCASTING")
        # broadcast(f"{nickname} joined the chat!".encode("ascii"))
        # print("BROADCASTED")
        # client.send("Connected to the server!".encode("ascii"))
        # print("CONNECTION COMPLETE")

        # starting a thread for each user
        t = Thread(target=handle, args=(client,))
        t.start()

if __name__ == "__main__":
    receive()
