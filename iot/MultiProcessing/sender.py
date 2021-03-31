# SENDER

import socket
import time

group = '224.1.1.1'
port = 5004

# 2-hop restriction in network
ttl = 2
count = 0

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP,
                socket.IP_MULTICAST_TTL,
                ttl)
while True:
	chat = bytes("i heard hello world : " + str(count), "utf-8")
	print("i sent hello world : " + str(count))
	sock.sendto(chat , (group, port))
	count = count + 1
	time.sleep(0.5)
