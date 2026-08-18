from db_connection import getConnection, closeConnection

def fetch_users():
    connection = getConnection()

    if connection is None:
        print("Failed to Establish connection")
        return
    cursor = None

    try:
        cursor = connection.cursor(dictionary= True)
        query = "select * from students"
        cursor.execute(query)
        rows = cursor.fetchall()

        print(rows)
        # for row in rows:
        #     print(row)
    except Exception as e:
        print("Error occurred", e)
    finally:
        closeConnection(connection, cursor)

def fetchUserById(id,name):
    connection = getConnection()

    if connection is None:
        print("Failed to connect ot DataBase")
        return
    cusror = connection.cursor(dictionary= True)
    cusror.execute("select * from students where student_id = %s and student_name = %s", (id,name,))
    data= cusror.fetchone()
    print(data)
    closeConnection
    return data

def insertData(data):
    connection = getConnection()
    if connection is None:
            print("Failed to connect ot DataBase")
            return

    cursor = connection.cursor()
    query = "INSERT INTO students VALUES (%s, %s, %s)"
    values = (data["student_id"], data["student_name"], data["department"])
    cursor.execute(query, values)
    connection.commit()
    print("Inserted data")
    closeConnection(connection, cursor)

fetch_users()
# fetchUserById(2, "Arun")

# insertData({
#     "student_id": 6,
#     "student_name": "Sathish",
#     "department": "IT"
# })
