import streamlit as st
import datetime
import requests


'''
# GGGGET YOUR TAXI FARE ESTIMATE
'''

st.markdown('''
On this page, you can receive an educated guess about potential cab prices in NYC. It is very useful.
''')
'''
## Please enter the details of your ride
'''
"Time of your ride:"
d = st.date_input(
    "What date do you want to be picked up?",
    datetime.date(2023, 2, 6))
t = st.time_input(
    "What time?",
    datetime.time(12, 15))
"Where do you want to be picked up?"
lat = st.number_input('Latitude?')
lon = st.number_input('Longitude?')
"Where do you want to go? "
lat2 = st.number_input('Dropoff Latitude?')
lon2 = st.number_input('Dropoff Longitude?')
"How many friends do you have?"
passengers = st.number_input('Passengers?')
passengers = int(passengers)

"Your pick up is scheduled:"
st.write('Your pickup-date is:', d)
st.write('Your pickup-time is:', t)
st.write('Latitude ', lat)
st.write('Longitude ', lon)
st.write('Passengers ', passengers)

x = datetime.datetime.combine(d, t)

## Once we have these, let's call our API in order to retrieve a prediction

query = f"https://taxifare.lewagon.ai/predict?pickup_datetime={x}&pickup_longitude={lon}&pickup_latitude={lat}&dropoff_longitude={lon2}&dropoff_latitude={lat2}&passenger_count={passengers}"

# load response from url and test whether multiple responses given (max 10)
response = requests.get(query).json()

output = response["fare"]

"This is your estimated price"
st.write('Fare ', output)



'''
2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
