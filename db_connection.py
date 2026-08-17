import mysql.connector
from mysql.connector import Error

#python -m pip install mysql-connector-python
def getConnection():
    try:
        connection = mysql.connector.connect(
                host = "localhost",
                port= 3306,
                database="javatrainingpro",
                user = "root",
                password = "Vignesh333#"
        )
        if connection.is_connected():
            print("Connection established successfully")
            return connection
    except Error as e:
        print("Error while acquiring connection", e)
        return None

def closeConnection(connection, cursor=None):
    if cursor:
        cursor.close()

    if connection and connection.is_connected():
        connection.close()
        print("connection closed successfully")