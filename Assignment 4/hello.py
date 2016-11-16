from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#set FLASK_APP=hello.py
#flask run

if __name__ == "__main__":
    app.run(debug=True)