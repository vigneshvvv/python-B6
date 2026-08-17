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


fetch_users()