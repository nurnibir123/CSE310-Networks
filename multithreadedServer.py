from socket import *
import threading
from threading import Thread
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

port = 8080
serverSocket.bind(('localhost', port))
serverSocket.listen()

def client_handler(connection_socket, connection_addr):
    message = connection_socket.recv(1024)
    message = message.decode()
    print('New connection from client at: ', connection_addr[0], connection_addr[1])
    print('Handled on: ', threading.currentThread())
    print(message.split())
    filename = message.split()[1].replace('/', '')
    print(filename)
    try:
        f = open(filename)
        outputdata = f.read()

        headerline = 'HTTP/1.1 200 OK\r\n\r\n'
        connection_socket.send(headerline.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        error = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(error.encode())
        newHTML = '<html><body>404 Not Found</body></html>'
        for c in newHTML:
            connectionSocket.send(c.encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()


threads = []

keepGoing = True
while keepGoing:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        newThread = Thread(target = client_handler, args=(connectionSocket, addr))
        threads.append(newThread)
        newThread.start()    
    except KeyboardInterrupt:
        keepGoing = False  

serverSocket.close()
for t in threads: 
    t.join() 
sys.exit() 