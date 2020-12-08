#from http.server import HTTPServer, BaseHTTPRequestHandler
import sys, os, socket
from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
#from http.server import HTTPServer, CGIHTTPRequestHandler
import socket
from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import urllib.parse

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created")

host = socket.gethostname()
class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass
#socket.SOCK_STREAM indicates TCP
#serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serversocket.bind(("localhost", 8888))

#port = 8888
class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        message_parts = [
                'CLIENT VALUES:',
                'client_address=%s (%s)' % (self.client_address,
                                            self.address_string()),
                'command=%s' % self.command,
                'path=%s' % self.path,
                'real path=%s' % parsed_path.path,
                'query=%s' % parsed_path.query,
                'request_version=%s' % self.request_version,
                '',
                'SERVER VALUES:',
                'server_version=%s' % self.server_version,
                'sys_version=%s' % self.sys_version,
                'protocol_version=%s' % self.protocol_version,
                '',
                'HEADERS RECEIVED:',
                ]
        for name, value in sorted(self.headers.items()):
            message_parts.append('%s=%s' % (name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return

class RouteHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/season/':
            self.path = '/season/season.html'

        elif self.path == '/winter/':
            self.path = '/winter/winter.html'

        elif self.path == '/spring/':
            self.path = '/spring/spring.html'

        elif self.path == '/autumn/':
            self.path = '/autumn/autumn.html'

        elif self.path == '/summer/':
            self.path = '/summer/summer.html'

        elif self.path == '/?/':
            return GetHandler.do_GET(self)
        else:
            super(RouteHandler, self).do_GET()

        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

if __name__ == '__main__':
    '''
    This sets the listening port, default port 8888
    '''
    if sys.argv[1:]:
       port = int(sys.argv[1])
    else:
       port = 8888

    '''
    This sets the working directory of the HTTPServer, defaults to directory where $
    '''
    if sys.argv[2:]:
       os.chdir(sys.argv[2])
       CWD = sys.argv[2]
    else:
       CWD = os.getcwd()

    #server = ThreadingSimpleServer(('', PORT), SimpleHTTPRequestHandler)
    from http.server import HTTPServer
    server = HTTPServer(('', port), RouteHandler)
    print('Starting server, use <Ctrl-C> to stop')
    #server.serve_forever()

    print("Serving HTTP traffic from", CWD, "on", host, "using port", port)
    server.serve_forever()
    try:
      while 1:
        sys.stdout.flush()
        server.handle_request()
    except KeyboardInterrupt:
      print("\nShutting down server per users request.")


#httpd = HTTPServer(('', port), Serv)
#httpd.serve_forever()
