import socket

server = socket.socket()
ip = "localhost"
port = 12345  #65536 max

server.connect((ip,port))
print("BAĞLANTI SAĞLANDI")

message = server.recv(1024) # 2pow
print(message.decode())

server.close()