import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title('my parents new healthy diet')

streamlit.header(' Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

# New Section to display furityvice api response
streamlit.header('Fruiyvice Fruit Advice!')
fruit_choice = stremlit.text_input('What Fruit would loke information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)
                
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it
streamlit.dataframe(fruityvice_normalized)

