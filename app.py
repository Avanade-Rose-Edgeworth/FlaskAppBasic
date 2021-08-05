from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello to Rose and Rose only !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'


if __name__ == '__main__':
    app.run()
