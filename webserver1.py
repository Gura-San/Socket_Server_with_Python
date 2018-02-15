# importing low level networking interface https://docs.python.org/2/library/socket.html
import socket

# specifying the port number for connection
HOST, PORT = '', 3000
# Python interface is a straightforward transliteration of the Unix system call
# and library interface for sockets to Pythons object-oriented style
# Function socket.socket creates a socket
# and returns a socket descriptor which can be used in other socket related functions

# Code below will create a socket with the following properties:
# Address Family : AF_INET (this is IP version 4 or IPv4)
# Type : SOCK_STREAM (this means connection oriented TCP protocol)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to a public host,
# and a well-known port
listen_socket.bind((HOST, PORT))
# Listen for the incoming connections on the socket
listen_socket.listen(1)
# Welcome message after the connection
print 'Serving HTTP on port %s ...' % PORT
# Accept all connections on the specified socket
# and send back "Hello World" responce for each request
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()
