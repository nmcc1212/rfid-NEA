## Add new card function

Add function for adding new cards to the database

![Text Description automatically generated with medium
confidence](./imgs/iteration3/media/image1.png){width="6.268055555555556in"
height="0.96875in"}

![](./imgs/iteration3/media/image2.png){width="6.268055555555556in"
height="0.7284722222222222in"}

The exit() instead now calls the add_new_card() function

\--

## Add support for Names

Add to database

ALTER TABLE card_states

ADD COLUMN name VARCHAR(255);

Add to the add_new_cards() functrion

![Text Description automatically
generated](./imgs/iteration3/media/image3.png){width="6.268055555555556in"
height="1.073611111111111in"}

\--

## Name missing in SQL INSERT

![Text Description automatically
generated](./imgs/iteration3/media/image4.png){width="6.268055555555556in"
height="2.4916666666666667in"}

Didn't add names to the sql insert command

![](./imgs/iteration3/media/image5.png){width="6.268055555555556in"
height="0.32222222222222224in"}

Now becomes

![](./imgs/iteration3/media/image6.png){width="6.268055555555556in"
height="0.32222222222222224in"}

\--

## New get name function

![](./imgs/iteration3/media/image7.png){width="6.268055555555556in"
height="0.4708333333333333in"}

The get_current_value() function was not update to also get the name
from the database, meaning when the script tried to print the name it
didn't know it. This only occurred for when the add_new_card() function
was not used, as if it was the name would have been provided then

I created a new function get_name() to get the name from the database

![Text Description automatically
generated](./imgs/iteration3/media/image8.png){width="6.268055555555556in"
height="1.9881944444444444in"}

Then I changed the IF statement that is used to determine if the user is
in the database or not. Now if the user is already in the database the
new get_name() function is called, if the user is not in the database,
the add_new_card() function is called, which asks for the name already

![Graphical user interface, text, application, chat or text message
Description automatically
generated](./imgs/iteration3/media/image9.png){width="6.268055555555556in"
height="1.9881944444444444in"}

\-\--

Final work

The database is
empty![](./imgs/iteration3/media/image10.png){width="6.268055555555556in"
height="0.32222222222222224in"}

Now the card is scanned

![Text Description automatically
generated](./imgs/iteration3/media/image11.png){width="6.268055555555556in"
height="0.9152777777777777in"}

This can now be seen in the database

![Text Description automatically
generated](./imgs/iteration3/media/image12.png){width="6.268055555555556in"
height="0.9152777777777777in"}

Now the same card is scanned again

![Text Description automatically
generated](./imgs/iteration3/media/image13.png){width="6.268055555555556in"
height="0.9826388888888888in"}