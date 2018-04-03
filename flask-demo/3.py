from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("hello.html")

@app.route('/test-get', methods = ['get'])
def test_get():
    return "It's a GET method!"

@app.route('/test-post', methods = ['post'])
def test_post():
    return "It's a POST method!"

app.run()
