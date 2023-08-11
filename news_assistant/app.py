from flask import Flask, flash, request, render_template, session, redirect

from helpers.news_api_helper import *
from helpers.audio_helper import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Tech')
def tech():
    url = from_tech_crunch()
    generate_news(url)
    return render_template('index.html', showAudio=True)

@app.route('/RSA')
def rsa():
    url = from_news24()
    generate_news(url)
    return render_template('index.html', showAudio=True)

@app.route('/USBiz')
def usbiz():
    url = business_new_from_usa()
    generate_news(url)
    return render_template('index.html', showAudio=True)

# app.route('/Search')
# def search():
#     return render_template('search.html')

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def generate_news(url):
    res = send_request(url)
    f_res = filter_response(res)
    text_to_mp3(f_res)

if __name__ == '__main__':
    app.run(debug=True)
