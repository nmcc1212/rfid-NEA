from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="rfid2",
        password="ad",
        database="rfid2"
    )
    return mydb

def get_all_cards():
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    sql = "SELECT card_id, binary_value, timestamp, name FROM card_states"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    cards = []
    for card in result:
        cards.append({
            'card_id': card[0],
            'binary_value': card[1],
            'timestamp': card[2],
            'name': card[3]
        })  
    return cards

@app.route('/')
def index():
    cards = get_all_cards()
    return render_template('index.html', cards=cards)


app.run(debug=True, host='0.0.0.0')