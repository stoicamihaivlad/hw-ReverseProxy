#1. It listens to HTTP requests and forwards them to one of the instances
#   of a downstream service that will process the requests.

# https://wiki.python.org/moin/BaseHttpServer
# https://docs.python.org/3/library/http.server.html

#https://docs.python.org/3/library/urllib.request.html



from http.server import SimpleHTTPRequestHandler, HTTPServer   #In Python 3, BaseHTTPServer was moved to http.server
import http.server

#import urllib.request

PORT = 8080

class reverseProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        #print(self.headers.items())
        print(self.headers['User-Agent'])
        print(type(self.headers))

        # self.copyfile(urllib.request.urlopen(f'https://127.0.0.1{self.path}'), self.wfile)
        self.end_headers()

    

Handler = http.server.SimpleHTTPRequestHandler

socket = ('127.0.0.1',PORT)
httpd = HTTPServer(socket,reverseProxy)
print("serving at port", PORT)
httpd.serve_forever()