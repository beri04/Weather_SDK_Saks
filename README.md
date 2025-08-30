# Weather SDK File 

# 📥 Installation 

git clone : https://github.com/beri04/Weather_SDK_Saks.git
cd Weather_SDK_Saks
pip install -r requirements.txt


# 👩‍💻EXAMPLE CODE 
```python 

from weather_sdk.weather import Weather

sdk = Weather("fake key")
print(sdk.get_current_weather("Delhi"))