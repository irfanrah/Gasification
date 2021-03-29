import xlsxwriter
import time
from time import strftime 
import os
from datetime import datetime
import random


try :
	os.mkdir("Data")
except OSError:
	print("Folder Created")

path = "Data/"
waktu = strftime("%H:%M:%S")
tanggal = strftime("%d-%m-%Y")

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(os.path.join(path , str(waktu)+'.xlsx'))
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
worksheet.write(1, 2, 'Time')

worksheet.write(1, 3, 'Blower Hisap')
worksheet.write(1, 4, 'Blower Primer')
worksheet.write(1, 5, 'Vibrating Grate')
worksheet.write(1, 6, 'Screw Feeder')

worksheet.write(1, 8, 'Drying')
worksheet.write(1, 9, 'Pyrolisis')
worksheet.write(1, 10, 'Combustion')
worksheet.write(1, 11, 'Reduction')



# Start from the first cell. Rows and columns are zero indexed.
row = 2
col = 2

try:
	for sby in range(1,1000):
		for sbx in range(1,1000):
			print("q")
			waktuUpdate = strftime("%H:%M:%S")
			worksheet.write(row, col, waktuUpdate)
			
			###

			worksheet.write(row, col + 1, sbx) # row, col , val
			worksheet.write(row, col + 2, random.randint(1,100)) # row, col , val
			worksheet.write(row, col + 3, random.randint(1,1000)) # row, col , val
			worksheet.write(row, col + 4, random.randint(1,10000)) # row, col , val
			worksheet.write(row, col + 5, random.randint(1,100000)) # row, col , val
			###
			row += 1
			time.sleep(0.3)

except KeyboardInterrupt:
    workbook.close()
