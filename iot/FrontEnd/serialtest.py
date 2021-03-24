import time
import serial

Serial = serial.Serial('/dev/ttyUSB0', 9600) # Establish the connection on a specific port
counter = 32 # Below 32 everything in ASCII is gibberish
while True:
     ArduinoIn = str(Serial.readline()) #
     ArduinoCut = ArduinoIn[2:-5]
     print(ArduinoCut)
     #print()
     time.sleep(0.5) # Delay for one tenth of a second
     if counter == 255:
        counter = 32
