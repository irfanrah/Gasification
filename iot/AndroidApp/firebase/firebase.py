import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import random

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin = firebase_admin.initialize_app(cred, {'databaseURL': 'https://communicationdb-edd6e-default-rtdb.firebaseio.com/'})

Motor1 = db.reference( "Gasifier/Motor1" )
Motor2 = db.reference( "Gasifier/Motor2" )
Motor3 = db.reference( "Gasifier/Motor3" )
Motor4 = db.reference( "Gasifier/Motor4" )

while (True):

    Motor1.set(random.randint(0, 50) )
    Motor2.set(random.randint(20, 100))
    Motor3.set(random.randint(150, 1000))
    Motor4.set(random.randint(100, 2000) )
    time.sleep(1)