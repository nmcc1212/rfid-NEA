import mysql.connector #used for reading and writing to the database
import RPi.GPIO as GPIO #used for controlling the GPIO pins
from datetime import datetime #used for getting the current date and time
from mfrc522 import SimpleMFRC522 #used for reading the RFID card
import atexit #used for cleaning up GPIO on exit

atexit.register(GPIO.cleanup) #clean up GPIO on exit

# Connect to MySQL database
def connect_to_database():
    mydb = mysql.connector.connect(
      host="localhost",
      user="rfid2",
      password="ad",
      database="rfid2"
    )
    return mydb

# Set up RFID reader and read card ID
def read_card_id():
    reader = SimpleMFRC522()
    card = ""
    while True:
        card, text = reader.read()
        break
    return card

# Retrieve current binary value from database
def get_current_value(mydb, card):
    mycursor = mydb.cursor()
    sql = "SELECT binary_value FROM card_states WHERE card_id = %s"
    val = (card,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result:
        return result[0]
    else:
        return None
# Retrieve name from database
def get_name(mydb, card):
    mycursor = mydb.cursor()
    sql = "SELECT name FROM card_states WHERE card_id = %s"
    val = (card,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result:
        return result[0]
    else:
        return None


# Flip binary value
def flip_value(value):
    if value == 0:
        new_value = 1
    else:
        new_value = 0
    return new_value

# Get the current date and time
def get_time_stamp():
    now = datetime.now()
    time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return time_stamp

# Update database with new value and timestamp
def update_database(mydb, card, new_value, time_stamp):
    mycursor = mydb.cursor()
    sql = "UPDATE card_states SET binary_value = %s, timestamp = %s WHERE card_id = %s"
    val = (new_value, time_stamp, card)
    mycursor.execute(sql, val)
    mydb.commit()
# Add new card to database
def add_new_card(mydb, card):
    mycursor = mydb.cursor()
    name = input("Enter name: ")
    sql = "INSERT INTO card_states (card_id, binary_value, timestamp, name) VALUES (%s, %s, %s, %s)"
    val = (card, 0, get_time_stamp(), name)
    mycursor.execute(sql, val)
    mydb.commit()
    return name

# Main function
def main():
    mydb = connect_to_database()
    card = read_card_id()
    current_value = get_current_value(mydb, card)
    if current_value is None:
        name = add_new_card(mydb, card)
    else:
        name = get_name(mydb, card)
    new_value = flip_value(current_value)
    time_stamp = get_time_stamp()
    update_database(mydb, card, new_value, time_stamp)
    print("Card ID:", card)
    print("Binary value updated to:", new_value)
    print("Time Stamp:", time_stamp)
    print("Name:", name)


main()
