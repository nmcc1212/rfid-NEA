from flask import Flask, render_template
import mysql.connector
import RPi.GPIO as GPIO
from datetime import datetime
from mfrc522 import SimpleMFRC522

app = Flask(__name__)

@app.route("/")
def get_card_status():
    mydb = mysql.connector.connect(
      host="localhost",
      user="rfid2",
      password="ad",
      database="rfid2"
    )
    mycursor = mydb.cursor()

    reader = SimpleMFRC522()
    card = ""
    while True:
        card, text = reader.read()
        break

    sql = "SELECT binary_value FROM card_states WHERE card_id = %s"
    val = (card,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        current_value = result[0]
    else:
        current_value = None

    return render_template("3rd-iteration.html", current_value=current_value, card_id=card)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
