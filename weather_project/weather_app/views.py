import requests
from django.shortcuts import render
# Create your views here.

def weather_view(req):
    weather_data = {}
    error_message = None
    if req.method=='POST':
        city=req.POST.get('city')
        API_KEY="0a624d6b6b1499872f08f29e4fbfa25f"
        urls = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"

        try:
            response=req.get(urls, timeout=5)
            data=response.json()
            
            if response.status_code==200:
                """status_code == 200 ka matlab "success" isliye hota hai kyunki yeh HTTP protocol ka ek international standard (rule) hai.
                Internet par jab bhi koi browser ya code kisi server ko request bhejta hai, toh server uske jawab mein ek Status Code wapas bhejta hai taaki pata chale ki request ka kya hua."""
                weather_data = {
                    'city':city.title(), #.title(): A Python string method that capitalizes the first letter of the city name (e.g., changes "mumbai" to "Mumbai").
                    'description': data['weather'][0]['description'].title(), #The "weather" key holds a list (array) of weather conditions. The first item in that list is at index [0].
                    'temperature': data['main']['temp'],#temperature is nested inside a container called "main". You look inside "main", and then grab the value labeled "temp".
                    'humidity': data['main']['humidity'],
                }
            else:
                error_message = data.get('message', 'City not found.')
        except req.exceptions.RequestException:
            error_message='Network ERROR'
    return render(req, 'core/dashboard.html', {'weather': weather_data, 'error': error_message})



            
        

     

        
    

"""1xx (Informational): Server request le raha hai, process chal raha hai.
2xx (Success): Request poori tarah successful rahi aur server ne sahi data wapas bhej diya.
3xx (Redirection): Page doosri jagah move ho gaya hai.
4xx (Client Error): User ki taraf se koi galti hai (jaise page nahi mila toh 404 Not Found).
5xx (Server Error): Server ke andar koi technical kharabi aa gayi hai.
"""