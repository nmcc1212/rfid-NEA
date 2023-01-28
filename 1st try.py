import mysql.connector
import RPi.GPIO as GPIO
from datetime import datetime

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
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN)

    card = ""
    while True:
        if GPIO.input(7) == 1:
            card = input("Scan RFID card: ")
            break
    return card

# Retrieve current binary value from database
def get_current_value(mydb, card):
    mycursor = mydb.cursor()
    sql = "SELECT binary_value FROM card_states WHERE card_id = %s"
    val = (card,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result[0]

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

# Main function
def main():
    mydb = connect_to_database()
    card = read_card_id()
    current_value = get_current_value(mydb, card)
    new_value = flip_value(current_value)
    time_stamp = get_time_stamp()
    update_database(mydb, card, new_value, time_stamp)
    print("Card ID:", card)
    print("Binary value updated to:", new_value)
    print("Time Stamp:", time_stamp)


main()
