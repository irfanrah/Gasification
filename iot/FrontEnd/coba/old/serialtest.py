import time
import serial

Serial = serial.Serial('/dev/ttyUSB0', 9600) # Establish the connection on a specific port
counter = 32 # Below 32 everything in ASCII is gibberish

def CalcBH(x):
	return round((-1.836351 + 0.08916699*x - 0.0002387275*x**2 + 4.100465e-7*x**3),0)
	
def CalcBP(x):
	return round((1.281323 + 0.02583632*x + 0.0001022204*x**2 - 1.164421e-7*x**3),0)
	
def CalcSF(x):
	return round((0.6508039 + 0.01766357*x + 0.00026934*x**2 - 5.791206e-7*x**3),0)
     
     
while True:
     ArduinoIn = str(Serial.readline()) #
     ArduinoCut = ArduinoIn[2:-5]
     ArduinoList = ArduinoCut.split(",")
     print(CalcBP(float(ArduinoList[2])))
     #print()
     time.sleep(0.1) # Delay for one tenth of a second
     if counter == 255:
        counter = 32
