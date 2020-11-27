
import streamlit as st
import pandas as pd
import datetime

import requests
# import streamlit.components.v1 as components

'''
# TaxiFareModel front

This front queries the [taxi fare model](https://taxifaremodelapi.herokuapp.com/predict_fare?key=2012-10-06%2012:10:20.0000001&pickup_datetime=2012-10-06%2012:10:20%20UTC&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6413111&dropoff_latitude=-73.7803331&passenger_count=2) Flask API
'''




key = '2012-10-06 12:10:20.0000001'
pickup_date = st.date_input('pickup datetime', value=datetime.datetime.now())
pickup_time = st.time_input('pickup datetime', value=datetime.datetime.now())
pickup_datetime = f'{pickup_date} {pickup_time}UTC'
pickup_longitude = st.number_input('pickup longitude', value=-73.9798156)
pickup_latitude = st.number_input('pickup latitude', value=40.7614327)
dropoff_longitude = st.number_input('dropoff longitude', value=-73.7803331)
dropoff_latitude = st.number_input('dropoff latitude', value=40.6413111)
passenger_count = st.number_input('passenger_count', min_value=1, max_value=8, step=1, value=1)

def get_map_data():
    print('get_map_data called')
    lati = [pickup_latitude, dropoff_latitude]
    longi = [pickup_longitude, dropoff_longitude]
    df = pd.DataFrame(data={'latitude': lati, 'longitude': longi})
    return df

df = get_map_data()
st.map(df)
# enter here the address of your flask api
url = 'https://taxifaremodelapi.herokuapp.com/predict_fare'

params = dict(
    key=key,
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count)

response = requests.get(url, params=params)

prediction = response.json()

pred = prediction['prediction']

pred


