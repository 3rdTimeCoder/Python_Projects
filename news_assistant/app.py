from flask import Flask, flash, request, render_template, session, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Tech')
def tech():
    return render_template('tech.html')

@app.route('/RSA')
def rsa():
    return render_template('rsa.html')

@app.route('/USBiz')
def usbiz():
    return render_template('usbiz.html')

app.route('/Search')
def search():
    return render_template('search.html')

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
