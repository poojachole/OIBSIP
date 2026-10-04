import requests

def get_simple_weather():
    city = input("Enter city name: ")
    # wttr.in is a free service that provides weather in text/json format without requiring an API key
    url = f"https://wttr.in/{city}?format=3"
    
    try:
        response = requests.get(url)
        print("\nWeather Result:")
        print(response.text)
    except:
        print("Error fetching weather.")

if __name__ == "__main__":
    get_simple_weather()