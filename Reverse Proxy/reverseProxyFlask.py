#1. It listens to HTTP requests and forwards them to one of the instances
#   of a downstream service that will process the requests.

# https://docs.python.org/3/library/socketserver.html
# https://wiki.python.org/moin/BaseHttpServer
# https://docs.python.org/3/library/http.server.html
#https://docs.python.org/3/library/socketserver.html

#In Python 3, BaseHTTPServer was moved to http.server
#https://medium.com/customorchestrator/simple-reverse-proxy-server-using-flask-936087ce0afb
#https://requests.readthedocs.io/en/latest/user/quickstart/



from flask import Flask,request,Response
import requests
app = Flask(__name__)
NAME = 'http://localhost:8080'
PORT='8080'

 
@app.route('/')
def index():
    return 'Flask is running'

#The purpose of the method created bellow the decorator is to 
# forward all http "GET" requests towards the downstream services
@app.route('/<path:path>' ,methods=['GET'])
def proxyHandler(path):
    if request.method=='GET':
        r = requests.get(f'{NAME}{path}')
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        #I have used list comprehension to filter what is inside the r.raw.headers dictionary
        #key,value pair used to iterate through the dictionary.items()
        #excluded_headers list is used to remove those headers from the forwarded message 

        headers = [(name, value) for (name, value) in     r.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(r.content, r.status_code, headers)
    return response

if __name__ == '__main__':
    app.run(port=PORT)