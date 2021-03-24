#!/usr/bin/env python3
import pyfirmata
import time
if __name__ == '__main__':
    board = pyfirmata.Arduino('/dev/ttyUSB0')
    print("Communication Successfully started")
    it = pyfirmata.util.Iterator(board)
    it.start()
    board.analog[0].enable_reporting()
    board.analog[1].enable_reporting()
    #board.analog[2].enable_reporting()
    board.analog[5].enable_reporting()
    while True:
        print("SF : " + str(board.analog[0].read()))
       #print("VG : " + str(board.analog[1].read()))
        print("BP : " + str(board.analog[1].read()))
        print("BH : " + str(board.analog[5].read()))
        time.sleep(1)