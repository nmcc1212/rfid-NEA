import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from mfrc522 import SimpleMFRC522 # Import the MFRC522 module

reader = SimpleMFRC522() # Create a reader object

# create an endless loop
try:
        id, text = reader.read() # read the card
        print(id) # print the card id
        print(text) # print the card text
finally:
        GPIO.cleanup() # clean up the GPIO pins on exit