import pytest
from weather_sdk.weather import Weather

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

    sdk = Weather("fake_key")
    result = sdk.get_current_weather("Delhi")
    assert result["city"] == "Delhi"
    assert result["temperature"] == 30