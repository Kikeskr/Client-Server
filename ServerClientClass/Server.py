import socket
import random as r
d1 = r.randint(1000, 9999)
d2 = r.randint(1000, 9999)
d3 = r.randint(1000, 9999)
d4 = r.randint(1000, 9999)
codes = [d1, d2, d3, d4]
print("server is started")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1027))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")

    if len(codes) > 1:
        clientsocket.send(bytes(f"Welcome to the server!\nYour unique code is {codes.pop()}", "utf-8"))

        gg=(address)
        print(gg)
        def saveit():
            codefile = open("servercodes", "w")
            codefile.write(f"address is {gg}")
            codefile.close()
        saveit()
    else:
        clientsocket.send(bytes(f"Welcome to the server.\nToday's code has been exhausted!", "utf-8"))


s.close()