﻿import requests
import openai
import json
import os

def get_openai_api_key():
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        return "API key not found"
    else:
        return api_key
    
def get_temperature(city, api_key):
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    return temp
  else:
    return "Error: Unable to fetch data"

def chat_with_openai(prompt, openai_api_key):
    openai.api_key = openai_api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)
    
def main():
  weather_api_key = 'your_openweathermap_api_key'
  openai_api_key = get_openai_api_key()

  user_input = input("Ask a general question or about the weather: ")
  openai_response = chat_with_openai(user_input, openai_api_key)

  try:
      # Parse the response as JSON and call the relevant function
      function_call = json.loads(openai_response)
      if function_call.get("action") == "get_temperature":
          city = function_call.get("parameters", {}).get("city")
          if city:
              temperature = get_temperature(city, weather_api_key)
              print(f"The temperature in {city} is {temperature}°C")
          else:
              print("City not specified.")
      else:
          print("No action to perform.")
  except json.JSONDecodeError:
      # If response is not JSON, just print it
      print("Response:", openai_response)

if __name__ == "__main__":
    main()
