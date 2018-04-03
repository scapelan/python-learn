from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("interface.html")

@app.route('/add', methods = ['POST'])
def add():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')

    return '{"status":0, "result":%d}' % (int(num1) + int(num2))

app.run()
    
