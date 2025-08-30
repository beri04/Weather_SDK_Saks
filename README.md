# 🌦️ Weather SDK

[![Run tests](https://github.com/beri04/Weather_SDK_Saks/actions/workflows/test.yml/badge.svg)](https://github.com/beri04/Weather_SDK_Saks/actions/workflows/test.yml)
A simple Python SDK to fetch **current weather** and **5-day forecast** using the [OpenWeather API](https://openweathermap.org/api).

---

## 📥 Installation

Clone this repo and install dependencies:

```bash
git clone https://github.com/beri04/Weather_SDK_Saks.git
cd Weather_SDK_Saks
pip install -r requirements.txt


👩‍💻 EXAMPLE CODE 
```python 

from weather_sdk.weather import Weather


#TO check the weather of any city
#For example - DELHI

sdk = Weather("your api_key here")

# Current weather in Delhi
print(sdk.get_current_weather("Delhi"))

# 5-day forecast for Chandigarh
print(sdk.get_forecast_weather("Chandigarh"))
