import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1027))
msg=s.recv(1024)
print(msg.decode("utf-8"))
s.close()