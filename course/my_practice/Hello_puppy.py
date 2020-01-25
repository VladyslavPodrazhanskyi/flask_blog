from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'


@app.route('/information')
def info():
    return '<h1>Puppies are cute!</h1>'

@app.route('/user/')
@app.route('/user/<name>')
def hello_user(name=None):
    if name:
        return f'<h1>Hello, {name[:5].title()} </h1>'
    return '<h1>Hello, Stranger</h1>'


if __name__ == '__main__':
    app.run(debug=True)