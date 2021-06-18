from flask import Flask

app=Flask(__name__)


@app.route('/')
@app.route('/index')
def homepage():
    return '<h1>Heroku Deploy update</h1>'

if __name__ == '__main__':
    app.run(debug=True)
