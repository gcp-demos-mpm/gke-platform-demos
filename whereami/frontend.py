import streamlit as st
import requests

st.title("Where Am I?")

api_url = "http://your-service.com/api/location"  # Replace with your actual API URL

try:
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for bad status codes

    location_data = response.json()
    city = location_data.get("city", "Unknown")
    country = location_data.get("country", "Unknown")

    st.write(f"You are in **{city}**, **{country}**")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching location: {e}")
