from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Home Page</h1>'

if __name == '__main__':
    app.run()

