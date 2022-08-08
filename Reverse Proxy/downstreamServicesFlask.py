from flask import Flask
import random
app = Flask(__name__)


#PORT = 9090
HOST = ["10.0.0.1","10.0.0.2"]

@app.route('/')
def index():
    return "Flask is running"

@app.route('/hw1')
def helloWorld():
    return "Hello World 1"

@app.route('/hw2')
def helloWorld2():
    return 'Hello, World2'

@app.route('/hw3')
def hello_world3():
    return "Hello World 3"



if __name__ == '__main__':
    #app.run(port=PORT, host=HOST[random.randrange(0,2)])  #not able to assign that ip address // not able to simulate this on my on laptop
    app.run()  