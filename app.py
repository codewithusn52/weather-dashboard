import os
import requests 
from flask import Flask,request
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("API_KEY")
@app.route("/",methods="GET", "POST"])