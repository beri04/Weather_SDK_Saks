import requests
class Weather :
    def __init__(self,api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"


    def get_current_weather(self,city):
        url = f"{self.base_url}/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url).json()

        if response.get('cod') != 200:
            return {'error':response.get("message","Something Went Wrong")}
        
        return{
            'city': response['name'],
            'temperature':response['main']['temp'],
            'humidity':response['main']['humidity'],
            'condition':response['weather'][0]['description']
        }
    


    def get_forecast_weather(self,city):
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url).json()
        if response.get('cod') != "200":
            print(response.get('cod'))
            return {'error':response.get('message','Something went wrong')}
        
        forecast_list = []
        for entry in response['list'][:5]:
            forecast_list.append({
                    'datetime': entry['dt_txt'],
                    'temperature':entry['main']['temp'],
                    'humidity':entry['main']['humidity'],
                    'condition':entry['weather'][0]['description']
            })


        return{
            'city':city,
            'forecast':forecast_list
        }   