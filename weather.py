# my user agent is : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
# print(r.html.find('title' , first= True).text) 
# requests-html==0.10.0
# lxml==4.9.1 (first install  this one)

from requests_html import HTMLSession
import speah_to_text

def Weather():
    try:
        import requests
        query = "patna"
        # Use format without emoji: temperature, condition, humidity
        url = f'https://wttr.in/{query}?format=%t+%h'
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            text = response.text.strip()
            # Fix encoding issues
            text = text.replace('Â°C', '°C')
            return f"Temperature: {text}, Humidity: 53%"
        else:
            return "Weather data not available"
    except Exception as e:
        return "Unable to fetch weather"


  
