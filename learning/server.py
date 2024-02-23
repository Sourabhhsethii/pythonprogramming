import socket

# Create Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
ip_address_server = "127.0.0.1"
port = 5003
s.bind((ip_address_server,port))

# Listen for the request
s.listen()

# Accept the connection of the client
# Connection - connection established by the client
conn, addr = s.accept()
print("Connected by", addr)

# Receive the data from the client
data_receive = conn.recv(1024)

response = bytes("Hello World! - Server Here, I have received the data ".encode("utf-8")  + data_receive)
conn.sendall(response)

# 2 sockets - s, connection
conn.close()
s.close()

# TCP 127.0.0.1: 56790 -> 127.0.0.1:5003
# 56790
