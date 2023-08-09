import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        database="my_list",
        user="root",
        password='2047'
    )
    my_cursor = conn.cursor()
    print("You are Connected to Database 1 Successfully")

except Exception as ex:
    print('Connection Error', ex)

#finally:
    #conn.close()
    #print("Connection Closed")