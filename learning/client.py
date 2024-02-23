import socket

# Create Socket
# Client needs to communicate with server
# establishing a connection
# socker creation - ip layer, transport layer protocol
# SOCK_STREAM -> TCP protocol
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to server
ip_address_server = "127.0.0.1"
port = 5003
s.connect((ip_address_server,port))

# Send the data to the server
#
# while(!completed_data_sent)
#     send_current_data
#     send_next_1024_byte

data_to_send = bytes("Sourabh Here!".encode("utf-8"))
s.sendall(data_to_send)

# Recevies the data
# 1024 is the buffer size.
data_to_receive = s.recv(1024)
print(data_to_receive)

s.close()