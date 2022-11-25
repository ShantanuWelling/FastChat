import mysql.connector
class ServerBalance:
    """This is the implementation of the server balancer. |br|
    The member functions are: |br|
    1. Intializing Constructor |br|
    2. PortAllocation
    """
    def __init__(self):
        """This is the constructor of the class. It creates a table in MySQL called PORTS which keep records of the number of ports a server is connected to. If the table is initally empty it creates 5 ports.
        """
        mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harshit123@",
        database="FASTCHAT"
        )
        mycursor = mydb2.cursor(buffered=True)

        mycursor.execute("CREATE TABLE IF NOT EXISTS PORTS (portnumber int PRIMARY KEY, numcon int, connected varchar(255))")

        s5="select portnumber from PORTS"
        mycursor.execute(s5)
        re=mycursor.fetchall()
        if len(re)==0:
            for i in range(5):
                num=6924+i
                con=0
                connected="F"
                myquery2 = "INSERT INTO PORTS (portnumber, numcon , connected) VALUES (%s, %s, %s)",(num, con, connected)
                mycursor.execute(*myquery2)
                mydb2.commit()

    # list1=[6958,6957,6956,6955,6954]


    def PortAllocation(self):
        """It finds a port which is not yet connected to any client. It fetches this portnumber from the tables created.

        :return: The port number which is not yet connected to any client.
        :rtype: int
        """
        mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harshit123@",
        database="FASTCHAT"
        )
        mycursor = mydb2.cursor(buffered=True)
        s1="select portnumber from PORTS where connected=%s"
        f="F"
        adr=(f, )
        mycursor.execute(s1,adr)
        result=mycursor.fetchall()
        number=0
        for x in result:
            number=x[0]
            break
        sql = "update PORTS set connected=%s where portnumber=%s"
        t="T"
        adr2=(t,number, )
        mycursor.execute(sql, adr2)
        mydb2.commit()
        return number
        
        

class ClientBalance:
    """This is implementation of client balancer. If a new client is registered then it is connected to a server with the minimum number of ports to balance the load. |br|
    The member functions are: |br|
    1. Addconn |br|
    2. delconn |br|
    3. incrementconn
    """
    def Addconn(self):
        """This function finds a port with number of connections in the Table and updates it by adding one as new client will be connected to this port.

        :return: port at which a new client has to be connected
        :rtype: int
        """
        mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harshit123@",
        database="FASTCHAT"
        )
        mycursor = mydb2.cursor(buffered=True)
        s1="select * from PORTS where connected=%s"
        t="T"
        a=(t, )
        mycursor.execute(s1,a)
        result=mycursor.fetchall()
        num=101
        port=0
        for x in result:
            if(x[1]<=num):
                num=x[1]
                port=x[0]

        sql2 = "update PORTS set numcon=%s where portnumber=%s"
        
        adr3=(num+1,port, )
        mycursor.execute(sql2, adr3)
        mydb2.commit()
        return port

    def delconn(self,portnum):
        """This function is implemented to delete a connection at a server.

        :param portnum: The port number at which a connection has to be deleted
        :type portnum: int
        """
        mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harshit123@",
        database="FASTCHAT"
        )
        mycursor = mydb2.cursor(buffered=True)
        s1="select numcon from PORTS where portnumber=%s"
        a=(portnum, )
        mycursor.execute(s1,a)
        result=mycursor.fetchall()
        con=0
        for x in result:
            con=x[0]
            break
        sql2 = "update PORTS set numcon=%s where portnumber=%s"
        
        adr3=(con-1,portnum, )
        mycursor.execute(sql2, adr3)
        mydb2.commit()
        return 

    def incrementconn(self, portnum):
        """This function is implemented to add a connection to a port.

        :param portnum: The port number at which a connection has to be inserted.
        :type portnum: int
        """
        mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harshit123@",
        database="FASTCHAT"
        )
        mycursor = mydb2.cursor(buffered=True)
        s1="select numcon from PORTS where portnumber=%s"
        a=(portnum, )
        mycursor.execute(s1,a)
        result=mycursor.fetchall()
        con=0
        for x in result:
            con=x[0]
            break
        sql2 = "update PORTS set numcon=%s where portnumber=%s"
        
        adr3=(con+1,portnum, )
        mycursor.execute(sql2, adr3)
        mydb2.commit()
        return 
