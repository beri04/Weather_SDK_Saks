import pytest
from weather_sdk.weather import Weather


# #Just checking the printing of data 
# sdk = Weather("400626402097ea8eb43010bebd5de507")

# print(sdk.get_current_weather("Delhi"))


class DummyResponse:
    def __init__(self, json_data):
        self._json = json_data
    def json(self):
        return self._json

def test_get_current_weather(monkeypatch):
    def mock_get(*args, **kwargs):
        return DummyResponse({
            "cod": 200,
            "name": "Delhi",
            "main": {"temp": 30, "humidity": 70},
            "weather": [{"description": "clear sky"}]
        })
    monkeypatch.setattr("requests.get", mock_get)

    # Checking for the City named DELHI
    sdk = Weather("fake_key")
    result = sdk.get_current_weather("Delhi")
    result1 = sdk.get_forecast_weather("Chandigarh")
    assert result["city"] == "Delhi"
    assert result["temperature"] == 30


def test_get_forecast_weather(monkeypatch):
    def mock_get_for(*args,**kwargs):
        return DummyResponse({
            "cod":"200",
            "name":"Chandigarh",
            "list":[
                {
                    "dt_txt":"2025-8-29 15:00:00",
                    "main":{"temp":28.5,"humidity":60},
                    "weather":[{"description":"few clouds🌥️"}]
                },
                {
                    "dt_txt":"2025-8-30 13:00:00",
                    "main":{"temp":30,"humidity":63},
                    "weather":[{"description":"cloudy☁️"}]
                },
                {
                    "dt_txt":"2025-8-31 8:00:00",
                    "main":{"temp":25,"humidity":55},
                    "weather":[{"description":"rainy💦"}] 
                },
                {
                    "dt_txt":"2025-9-1 14:00:00",
                    "main":{"temp":25,"humidity":55},
                    "weather":[{"description":"thunderstorm⛈️"}] 
                },
                {
                    "dt_txt":"2025-9-2 12:00:00",
                    "main":{"temp":25,"humidity":55},
                    "weather":[{"description":"sunny☀️"}] 
                }
            ]
        })
    monkeypatch.setattr("requests.get",mock_get_for)

    # Checking for the City named CHANDIGARH
    sdk = Weather("fake key")
    result = sdk.get_forecast_weather("Chandigarh")
    assert result['city'] == "Chandigarh"
    assert len(result['forecast']) == 5
    assert result["forecast"][1]["condition"] == "cloudy☁️"
