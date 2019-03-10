from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = "Buddy"
    letters = list(name)
    pup_dictionary = {'pup_name': 'Sammy', 'pup_type': 'Laborador'}
    return render_template('home.html', name=name, letters=letters, pup_dictionary=pup_dictionary)

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
    if name[-1] != 'y':
        name = name + "y"
    else:
        name = name[0:-1] + "iful"
    return f'<h1>This is the puppy name: {name}'

if __name__ == '__main__':
    app.run(debug=True)

