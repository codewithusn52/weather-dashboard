import requests
from django.shortcuts import render
# Create your views here.

def weather_view(request):
    weather_data = {}
    error_message = None
    if request.method=='POST':
        city=request.POST.get('city')
        API_KEY="0a624d6b6b1499872f08f29e4fbfa25f"
        urls = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
        