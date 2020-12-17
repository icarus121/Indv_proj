import socket
import sys
import os
from _thread import *
import urllib.parse

def server_program():
    # get the hostname
    #host = socket.gethostname()
    host = ''
    port = 8080  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    print("Socket bind to: " + str(port))
    # look closely. The bind() function takes tuple as argument
    #server_socket.bind((host, port))  # bind host address and port together

    ThreadCount = 0
    try:
       server_socket.bind((host, port))
    except socket.error as e:
       print(str(e))

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    def threaded_c(connection):
       connection.send(str.encode("Welcome to the server"))
       #conn, address = server_socket.accept()  # accept new connection
       print("Connection from: " + str(address))

       while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
         data = connection.recv(1024)
         data = data.decode('utf-8')
         if not data:
            # if data is not received break
             break
         elif data == 'index':
            file = open('index/index.html', 'r')
            message = file.read()
            #connection.send(str.encode(message))  # send data to the client

         elif data == 'function':
            file = open('function/function.html', 'r')
            message = file.read()

         else:
           message = "Not Found."
           #connection.send(str.encode("Not found"))
         #print("from connected user: " + str(data))
         #data = input('What do you want to accesss -> ')
         #connection.send(str.encode(input))  # send data to the client
         #reply = 'Server says: ' + data.decode('utf-8')
         #connection.sendall(str.encode(reply))

         connection.send(str.encode(message))
       connection.close()  # close the connection

    while True:
       Client, address = server_socket.accept()
       print('Connected to: ' + address[0] + ':' + str(address[1]))
       start_new_thread(threaded_c, (Client, ))
       ThreadCount += 1
       print('Thread Number: ' + str(ThreadCount))

#server_socket.close()

if __name__ == '__main__':
    server_program()

