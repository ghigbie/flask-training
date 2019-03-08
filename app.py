from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Home Page</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

@app.route('/contact')
def contact():
    return '<h1>Contact Page</h1>'

@app.route('/cute')
def cute():
    return '<h1><Puppies are Cute!/h1>'

@app.route('/puppy/<name>')
def puppy(name):
    return f'<h1>This is the puppy name: {name.upper()}'

if __name__ == '__main__':
    app.run(debug=True)

