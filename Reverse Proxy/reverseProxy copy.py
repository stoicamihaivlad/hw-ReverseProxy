#1. It listens to HTTP requests and forwards them to one of the instances
#   of a downstream service that will process the requests.

# https://docs.python.org/3/library/socketserver.html
# https://wiki.python.org/moin/BaseHttpServer
# https://docs.python.org/3/library/http.server.html
#https://docs.python.org/3/library/socketserver.html

#In Python 3, BaseHTTPServer was moved to http.server



from http.server import BaseHTTPRequestHandler, HTTPServer   
NAME = "my-service"
PORT = 8080

# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        #TypeError: a bytes-like object is required, not 'str'
        #self.wfile.write("<body><p>This is my first proxy.</p>")
        self.send_response(200)
        self.end_headers()
        #self.send_resp_headers(req_header,11)
        
    
if __name__ == '__main__':
    socket = ('127.0.0.1',PORT)
    httpd = HTTPServer(socket,Handler)
    print ('proxy is up and waiting for traffic')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()