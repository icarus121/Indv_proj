import socket

#client_socket = socket.socket()
def client_program():
    #host = socket.gethostname()  # as both code is running on same pc
    client_socket = socket.socket()
    host = '192.168.0.103'
    port = 8080  # socket server port number

    print('Waiting for connection')
    try:
      client_socket.connect((host, port))
    except socket.error as e:
      print(str(e))

    #client_socket = socket.socket()  # instantiate
    #client_socket.connect((host, port))  # connect to the server

    #message = input(" -> ")  # take input

    Response = client_socket.recv(1024)
    print(Response)
    while True:
      Input = input(' -> ')
      client_socket.send(str.encode(Input))
      Response = client_socket.recv(1024)
      print(Response.decode('utf-8'))

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()


