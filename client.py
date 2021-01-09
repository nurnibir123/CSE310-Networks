from socket import *
import sys
import time

def run_client(server_name, server_port, fileName):
    fileName = 'GET ' + fileName
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    sent = client_socket.send(fileName.encode('utf-8'))
    client_socket.send('\r\n'.encode())
    
    keepRecieving = True
    modified_message = ''
    while keepRecieving:
        newMessage = client_socket.recv(1024)
        if not newMessage:
            keepRecieving = False
        else:
            modified_message += newMessage.decode()

    print('From Server: ', modified_message)
    print('AT: ', client_socket.getpeername())
    client_socket.close()

if __name__ == '__main__':
    serverName = 'localhost'
    port = 8080
    sn = sys.argv[1] if len(sys.argv) > 1 else serverName
    sp = int(sys.argv[2]) if len(sys.argv) > 2 else port
    fileToSend = sys.argv[3]
    print(sn, sp, fileToSend)
    run_client(sn, sp, fileToSend)

    
    
    