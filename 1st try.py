import mysql.connector
import datetime
import RPi.GPIO as GPIO

def dbinit():
    mydb = mysql.connector.connect(
        host="hostname",
        user="rfid2",
        password="ad",
        database="rfid-project"
    )
    mycursor = mydb.cursor()

def readcard():
    uid = ""
    while True:
        if GPIO.input(7) == 1:
            uid = input("Scan RFID card: ")
            print (uid)
            break
    return uid
def gettime():
    now = datetime.now()
    time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return time_stamp
	
def	GetStatusState(): 
    sql = "SELECT binary_value FROM rfid_cards WHERE uid = %s"
    val = (uid,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result

def statusflip():
    if result[0] == 0:
        new_value = 1
    else:
        new_value = 0
    return new_value

def insertflip():
    sql = "UPDATE rfid_cards SET binary_value = %s WHERE uid = %s"
    val = (new_value, uid)
    mycursor.execute(sql, val)
    mydb.commit()