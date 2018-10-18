import mysql.connector
#Enter the Database credentials here
dbusername = "root"
dbpassword = "Hughrocks1"

def initiate():

    mydb = mysql.connector.connect(

        host = "localhost",
        user = dbusername,
        passwd = dbpassword

    )
    dbcursor = mydb.cursor()
    dbcursor.execute("CREATE DATABASE IF NOT EXISTS Innovaccerdb")

    mydb.close()

# Reinitiating connection to the mysql with database database

    mydb = mysql.connector.connect(

        host="localhost",
        user=dbusername,
        passwd=dbpassword,
        database= "Innovaccerdb"

    )
    dbcursor = mydb.cursor()
    dbcursor.execute("CREATE TABLE IF NOT EXISTS showstable (email VARCHAR(50), show1 VARCHAR(50))")
    dbcursor.close()
    return mydb