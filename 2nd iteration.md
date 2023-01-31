![Text Description automatically
generated](./imgs/iteration2/media/image1.png)

Using

([https://github.com/nmcc1212/rfid2/blob/d627b2f2af4d4ee86963e30932556b7870d28e62/1st%20try.py](https://github.com/nmcc1212/rfid2/blob/d627b2f2af4d4ee86963e30932556b7870d28e62/1st%20try.py))
for reading cards didn't work, now using SimpleMFRC522

\-\--

![A screen shot of a computer Description automatically generated with
low
confidence](./imgs/iteration2/media/image2.png)

A reader object was missing

\-\--

![Text Description automatically
generated](./imgs/iteration2/media/image3.png)

Didn't handle error if the RFID UID was not in the database, fix

```
if result:
	return result\[0\]
else:
	return None
```


\--

![img](./imgs/iteration2/media/image4.png)

The GPIO pins showed as still in use after closing and relaunching the
program fixed by adding the "atexit" library which runs a predefined
script (GPIO.cleanup) when the program exits

--

![img](./imgs/iteration2/media/image5.png)

It looks as if the script works even though the card is not in the
database, fixed by checking if None is returned, if it is printing an
Error and then exiting

![img](./imgs/iteration2/media/image6.png)

\--

Now adding the RFID card to the DB manually,

`INSERT INTO rfid2.card_states (card_id, binary_value, timestamp) VALUES (770381256117, 0, \"2023-01-01 00:00:00\");`

Imgs of 1st iteration (adding users manually )

![A screenshot of a computer Description automatically generated with
low
confidence](./imgs/iteration2/media/image7.png)

The card has just been added

![img](./imgs/iteration2/media/image8.png)



The card has been tapped![Text Description automatically generated with
medium
confidence](./imgs/iteration2/media/image9.png)



This is now reflected in the database![img](./imgs/iteration2/media/image10.png)

Again, the card has been tapped![Graphical user interface, text
Description automatically generated with medium
confidence](./imgs/iteration2/media/image11.png)

Again, reflected in the database
