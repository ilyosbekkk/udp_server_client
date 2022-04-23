from socket import *

# create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# bind ip address and port for the server
serverSocket.bind(('localhost', 12000))

# program runs infinite times,when it receives request from client it sends the response
while True:

    message, address = serverSocket.recvfrom(1024)
    serverSocket.sendto(message, address)
