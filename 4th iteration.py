from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
# Connect to MySQL database
def connect_to_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="rfid2",
        password="ad",
        database="rfid2"
    )
    return mydb
# A function to Create RFID reader object and read card ID
def get_all_cards():
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    sql = "SELECT card_id, binary_value, timestamp, name FROM card_states"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    cards = []
    for card in result: #create a 
        cards.append({ 
            'card_id': card[0],
            'binary_value': card[1],
            'timestamp': card[2],
            'name': card[3]
        })  
    return cards

@app.route('/')
def index():
    cards = get_all_cards() #get all cards from database
    return render_template('index.html', cards=cards) #pass cards to the web interface


app.run(debug=True, host='0.0.0.0') #run the web interface, binding to all interfaces