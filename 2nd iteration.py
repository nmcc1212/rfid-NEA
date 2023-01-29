import mysql.connector
import RPi.GPIO as GPIO
from datetime import datetime
from mfrc522 import SimpleMFRC522
import atexit

atexit.register(GPIO.cleanup)

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
    global name
    mycursor = mydb.cursor()
    sql = "SELECT binary_value, name FROM card_states WHERE card_id = %s"
    val = (card,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result:
        return result[0]
        name = result[1]
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
    new_value = flip_value(current_value)
    time_stamp = get_time_stamp()
    update_database(mydb, card, new_value, time_stamp)
    print("Card ID:", card)
    print("Binary value updated to:", new_value)
    print("Time Stamp:", time_stamp)
    print("Name:", name)


main()
