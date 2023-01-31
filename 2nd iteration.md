![Text Description automatically
generated](./imgs/iteration2/media/image1.png){width="6.268055555555556in"
height="1.2715277777777778in"}

Using
(<https://github.com/nmcc1212/rfid2/blob/d627b2f2af4d4ee86963e30932556b7870d28e62/1st%20try.py>)
for reading cards didn't work, now using SimpleMFRC522

\-\--

![A screen shot of a computer Description automatically generated with
low
confidence](./imgs/iteration2/media/image2.png){width="6.268055555555556in"
height="1.2715277777777778in"}

A reader object was missing

\-\--

![Text Description automatically
generated](./imgs/iteration2/media/image3.png){width="6.268055555555556in"
height="1.2715277777777778in"}

Didn't handle error if the RFID UID was not in the database, fix

if result:

return result\[0\]

else:

return None

\--

![](./imgs/iteration2/media/image4.png){width="6.268055555555556in"
height="0.5902777777777778in"}

The GPIO pins showed as still in use after closing and relaunching the
program fixed by adding the "atexit" library which runs a predefined
script (GPIO.cleanup) when the program exits

\--

![](./imgs/iteration2/media/image5.png){width="6.268055555555556in"
height="0.5902777777777778in"}

It looks as if the script works even though the card is not in the
database, fixed by checking if None is returned, if it is printing an
Error and then exiting

![](./imgs/iteration2/media/image6.png){width="6.268055555555556in"
height="0.3861111111111111in"}

\--

Now adding the RFID card to the DB manually,

INSERT INTO rfid2.card_states (card_id, binary_value, timestamp) VALUES
(770381256117, 0, \"2023-01-01 00:00:00\");

Imgs of 1^st^ iteration (adding users manually )

![A screenshot of a computer Description automatically generated with
low
confidence](./imgs/iteration2/media/image7.png){width="6.268055555555556in"
height="1.0708333333333333in"}

The card has just been added

![](./imgs/iteration2/media/image8.png){width="6.268055555555556in"
height="0.60625in"}

The card has been tapped![Text Description automatically generated with
medium
confidence](./imgs/iteration2/media/image9.png){width="6.268055555555556in"
height="1.0631944444444446in"}

This is now reflected in the
database![](./imgs/iteration2/media/image10.png){width="6.268055555555556in"
height="0.5826388888888889in"}

Again, the card has been tapped![Graphical user interface, text
Description automatically generated with medium
confidence](./imgs/iteration2/media/image11.png){width="6.268055555555556in"
height="0.96875in"}

Again, reflected in the database
