import mysql.connector  

connect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "ranjip",
    database = "Task_manager"
)
print(connect)
if connect.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")