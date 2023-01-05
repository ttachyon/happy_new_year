# happy_new_year
create_resolutions_list function was created so that the user can enter their plans for 2023. The programm prompts the user for plans and creates a json file containing the user's resolutions for each month.

We use json and io libraries to run the function.

First, the user is asked for the number of plans they want to add (n = int(input)).

Then he enters the month number (int) and plans separated by commas (str)

After the user has entered all plans, the input window closes.

The user sees an blue painted inscription 'Hurray! Your list of resolutions was created!' and a New Year's picture via a link from the Web.

The user's plans are added to the dictionary, where the key is the name of the month, the value is the plans for this month.

This dictionary is added to the file named resolutions2023.json. 
