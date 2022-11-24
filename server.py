import socket

server = socket.socket()
ip = "localhost"
port = 12345

server.bind((ip,port))
server.listen(5)
client , client_address = server.accept()
print(client,client_address)
client.send("Test Message MERHABA !".encode())

server.close()