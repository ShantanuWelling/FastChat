import socket
from threading import Thread
import mysql.connector
import load

SB= load.ServerBalance()
# local host and port

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Vatsalya@4A"
)

mycursor1 = mydb.cursor(buffered=True)
mycursor1.execute("SHOW DATABASES")
mycursor1.execute("CREATE DATABASE IF NOT EXISTS FASTCHAT")

mydb2 = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Vatsalya@4A",
  database="FASTCHAT"
)
mycursor = mydb2.cursor(buffered=True)

mycursor.execute("CREATE TABLE IF NOT EXISTS CLIENTS (name VARCHAR(255) PRIMARY KEY, password VARCHAR(255), port int, pkey longtext)")
mycursor.execute("CREATE TABLE IF NOT EXISTS OFFLINE (sender VARCHAR(255), reciever VARCHAR(255), message longtext)")


host = "127.0.0.1"
port =  SB.PortAllocation()#TAKING PORT NUMBER FORM LOAD BALANCER

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("BIDNING")
server.bind((host, port))
print("LISTING ")
server.listen()
print("STARTING")

clients = []
nicknames = []

def broadcast(message):
    print("STARTING FOR LOOP")
    """
    Broadcasts messages.
    """
    for client in clients:
        print("SENDING MESSAGE TO A CLIENT")
        client.send(message)

def sender(message,name):
    """
    Broadcasts messages.
    """
    i=0
    print("STARTING FOR LOOP")
    for client in clients:
        print("h17")
        if(nicknames[i]==name):
            print("h18")
            client.send(message)
        i=i+1

def handle(client):
    """
    Handles a client at a time.
    """
    while True:
        print("Handle Function Started")
        try:
            for i in nicknames:
                print("list of Nicknames",i)
            r2 = client.recv(1024).decode("ascii")
            if(r2=="X"):
                raise Exception
            while True:

                print("RECIEVING MESSAGE FROM CLIENT")
                # name=client.recv(1024)
                message = client.recv(1024)
                print("BROADCASTING MES")
                sender(message,r2)
                print("DISPLAYED")
                next=client.recv(1024).decode("ascii")
                print("NEXT CHECKED")
                if(next=="Exiting chat"):
                    print("Breaking")
                    break
                elif(next=="Closing chat"):
                    raise Exception
                elif(next=="X"):
                    raise Exception
                else:
                    pass
                print("Over")
        except Exception as e:
            print("Inside Excepton of Handle")
            index = clients.index(client)
            print("Index is : ",index)
            clients.pop(index)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f"{nickname} has left the chat!".encode("ascii"))
            
            break

def receive():
    """
    Recieves messages.  
    """
    print("STARTING RECIEVE")
    while True:
        print("INSIDE RECIENCE TRUE")
        client, address = server.accept()
        print("ACCEPTING FROM SERVER")
        print("Connected with {}".format(str(address)))
        print("SENDING TO CLIENT")

        client.send("NICK".encode("ascii"))
        print("SENT")
        nickname =  client.recv(1024).decode("ascii")
        print("RECEIVING NICKNAME")
        nicknames.append(nickname)
        print("NICKNAME ADDED")
        clients.append(client)
        print("CLIENT ADDED")

        print(f"Name of the client  is {nickname}!")
        print("MESSAGE BROADCASTING")
        # broadcast(f"{nickname} joined the chat!".encode("ascii"))
        print("BROADCASTED")
        # client.send("Connected to the server!".encode("ascii"))
        print("CONNECTION COMPLETE")

        # starting a thread for each user
        t = Thread(target=handle, args=(client,))
        print("h34")
        t.start()

if __name__ == "__main__":
    print("INSIDE MAIN")
    print("Server is listening...")
    print("STARTING RECIEVE")
    receive()
    print("h37")