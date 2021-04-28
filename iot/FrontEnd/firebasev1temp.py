#!/usr/bin/python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import random
import socket
import struct
import re


MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5004

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


def decoding():
    msg = sock.recv(64)
    msgd = msg.decode("utf-8")
    digilist =  re.findall(r'[\d\.\d]+', msgd )
    Motor = digilist[0:4]
    Temperature = digilist[4:8]
    count = digilist[8]
    return Motor,Temperature,count

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin = firebase_admin.initialize_app(cred, {'databaseURL': 'https://communicationdb-edd6e-default-rtdb.firebaseio.com/'})


Temp1 = db.reference( "Gasifier/Drying" )
Temp2 = db.reference( "Gasifier/Pyrolisis" )
Temp3 = db.reference( "Gasifier/Combustion" )
Temp4 = db.reference( "Gasifier/Reduction" )

cnt = 0

while (True):
    Motor, Temperature,count = decoding()
    
    if cnt ==  5:
        Temp1.set(Temperature[0])
        Temp2.set(Temperature[1])
        Temp3.set(Temperature[2])
        Temp4.set(Temperature[3])
        cnt = 0
        
    print(count)
    cnt = cnt+ 1
