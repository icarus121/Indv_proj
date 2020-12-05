from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
#import request
import socket
#import SimpleHTTPServer

#msg = input("Message:")
#print(output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created")
#socket.SOCK_STREAM indicates TCP
#serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serversocket.bind(("localhost", 8888))

port = 8888
#host = socket.gethostname()
#s.bind(('', port))

#s.listen(5)
#print("socket bind to " + str(port))

#msg =open('index.html', 'r')
#message = msg.read()
#print(type(msg))

#while True:
#    c, addr = s.accept()
#    print("Got Connection from" + str(addr))

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index/index.html'
        elif self.path == '/goodbye/':
            self.path = '/goodbye/goodbye.html'

        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
        #while True:
        #c, addr = s.accept()
        #print("Got Connection from" + str(addr))

#os.chdir('.')
httpd = HTTPServer(('', port), Serv)
httpd.serve_forever()
