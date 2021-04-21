import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import random
import socket
import struct
import re

def decoding():
    msg = sock.recv(64)
    msgd = msg.decode("utf-8")
    digilist =  re.findall('\d+', msgd )
    Motor = digilist[0:4]
    Temperature = digilist[4:8]
    count = digilist[8]
    return Motor,Temperature,count

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin = firebase_admin.initialize_app(cred, {'databaseURL': 'https://communicationdb-edd6e-default-rtdb.firebaseio.com/'})

BH = db.reference( "Gasifier/BH" )
BP = db.reference( "Gasifier/BP" )
VG = db.reference( "Gasifier/VG" )
SF = db.reference( "Gasifier/SF" )

Temp1 = db.reference( "Gasifier/Drying" )
Temp2 = db.reference( "Gasifier/Pyrolisis" )
Temp3 = db.reference( "Gasifier/Combustion" )
Temp4 = db.reference( "Gasifier/Reduciton" )

while (True):

    BH.set(random.randint(0, 50) )
    BP.set(random.randint(20, 100))
    VG.set(random.randint(150, 1000))
    SF.set(random.randint(100, 2000) )
    
    Temp1.set(random.randint(0, 50) )
    Temp2.set(random.randint(20, 100))
    Temp3.set(random.randint(150, 1000))
    Temp4.set(random.randint(100, 2000) )
    time.sleep(1)
