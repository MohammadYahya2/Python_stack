from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def say_dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_hello(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:count>/<word>')
def repeat_word(count, word):
    return word * count

if __name__ == '__main__':
    app.run(debug=True)
