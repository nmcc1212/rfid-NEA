import mysql.connector

# connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="rfid",
  password="ad"
)

print(mydb)

x=1 

while x == 1:
    print ("1")