
def ArduRead():
     Serial = serial.Serial('/dev/ttyUSB0', 9600) # Establish the connection on a specific port
     ArduinoIn = str(Serial.readline()) 
     ArduinoCut = ArduinoIn[2:-5]
     time.sleep(0.5) 
     return ArduinoCut
