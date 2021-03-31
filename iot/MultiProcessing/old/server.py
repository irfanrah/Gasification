import socket
import time


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.close
s.bind((socket.gethostname(), 1210))
s.listen(5)
counting = 0
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"{address} has been established.")
    while True:
        time.sleep(1)
        msg = "hitung : " + str(counting)

        print(msg)

        clientsocket.send(bytes(msg,"utf-8"))
        counting = counting + 1
