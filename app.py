from flask import Flask
from flask import request

app = Flask(__name__)

@app.get('/welcome')
def say_welcome():
    """Return 'welcome' greeting"""


    html = "<html><body><h1>Welcome</h1></body></html>"
    return html

@app.get('/welcome/home')
def say_welcome_home():
    """Return 'welcome home' greeting"""

    html = "<html><body><h1>Welcome Home</h1></body></html>"
    return html

@app.get('/welcome/back')
def say_welcome_back():
    """Return 'welcome back' greeting"""

    html = "<html><body><h1>Welcome Back</h1></body></html>"
    return html