# flask-starter


### Installing Flask

Install Flask using the command below:

```python
pip install Flask
```


### Flask hello world app

Create a file called hello.py

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
    def hello():
        return "Hello World!"

if __name__ == "__main__":
    app.run()
```

Finally run the web app using this command:

```python
python hello.py
```

### Static Files

```python
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
```