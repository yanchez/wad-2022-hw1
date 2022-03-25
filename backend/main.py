from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("mainpage.html") 

@app.route('/info')
def info():
    return app.send_static_file('cat.jpg')

#@app.route('/info')
#def info():
#    return render_template("info.html")

app.run(host="localhost", port=5001, debug=True)