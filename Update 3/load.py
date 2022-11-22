import mysql.connector
class ServerBalance:

    def __init__(self):

        mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vatsalya@4A",
        database="FASTCHAT"
        )
        mycursor = mydb2.cursor(buffered=True)

        mycursor.execute("CREATE TABLE IF NOT EXISTS PORTS (portnumber int PRIMARY KEY, numcon int, connected varchar(255))")

        s5="select portnumber from PORTS"
        mycursor.execute(s5)
        re=mycursor.fetchall()
        if len(re)==0:
            for i in range(5):
                num=6944+i
                con=0
                connected="F"
                myquery2 = "INSERT INTO PORTS (portnumber, numcon , connected) VALUES (%s, %s, %s)",(num, con, connected)
                mycursor.execute(*myquery2)
                mydb2.commit()

    # list1=[6958,6957,6956,6955,6954]


    def PortAllocation(self):
        mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vatsalya@4A",
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

    def Addconn(self):
        mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vatsalya@4A",
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
        mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vatsalya@4A",
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
        mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vatsalya@4A",
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

        




    

