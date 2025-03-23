import requests
import streamlit as st


st.set_page_config(page_title="Weather App")
st.title("🌡️ Weather App")

API_KEY = st.secrets["WEATHER_API_KEY"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Get city name from user
city = st.text_input("Enter city name: ").strip().lower()

# Construct the API request URL
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

if st.button("Get Weather", use_container_width=True):
    # Make the API request Fetch weather data
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        condition = data['weather'][0]['main']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        st.write(f"\n🌍 Weather in {city}:")
        st.success(f"🌡 Temperature: {temperature}°C")
        st.success(f"☁ Condition: {condition.capitalize()}")
        st.success(f"💧 Humidity: {humidity}%")
        st.success(f"🌬 Wind Speed: {wind_speed} km/h")
    else:
        st.error("❌ Error: City not found or API request failed!")
