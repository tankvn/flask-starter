from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Home!"

@app.route("/hello")
def hello():
    return "Hello"

@app.route("/hello/<string:name>/")
def hello_user(name):  
    return "Hello, %s" % name

if __name__ == "__main__":
    app.run()