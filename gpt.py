import mysql.connector
import RPi.GPIO as GPIO
from datetime import datetime

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="hostname",
  user="username",
  password="password",
  database="database_name"
)

# Set up RFID reader
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Read RFID UID
UID = ""
while True:
    if GPIO.input(7) == 1:
        UID = input("Scan RFID tag: ")
        print UID
        break

# Retrieve current binary value from database
mycursor = mydb.cursor()
sql = "SELECT binary_value FROM rfid_tags WHERE tag_id = %s"
val = (UID,)
mycursor.execute(sql, val)
result = mycursor.fetchone()

# Flip binary value
if result[0] == 0:
    new_value = 1
else:
    new_value = 0

# Get the current date and time
now = datetime.now()
time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Update database with new value and timestamp
sql = "UPDATE rfid_tags SET binary_value = %s, timestamp = %s WHERE tag_id = %s"
val = (new_value, time_stamp, tag)
mycursor.execute(sql, val)
mydb.commit()

print("Tag ID:", tag)
print("Binary value updated to:", new_value)
print("Time Stamp:", time_stamp)