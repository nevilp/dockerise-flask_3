from flask import Flask,Response

app = Flask(__name__)

@app.route("/")
def hello():
    return Response('Hello World')


if __name__ == '__main__':
    app.run('127.0.0.1',port=80)