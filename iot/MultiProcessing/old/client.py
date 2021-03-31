import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1210))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        msgd = msg.decode("utf-8")
        print(msgd)
