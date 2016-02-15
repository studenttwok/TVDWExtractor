from struct import *
import csv

fIn = open("script.pgm", "rb")
fOut = open('script.csv','w')
csv_out = csv.writer(fOut)

# define the structure
dataFormat = "18sBBBBBB9sBBBBBBBiiiiiiiiiiiiiiiiiiiii"

try:
    # every script block is 124 byte long
    for i in range(0,800):
        fIn.seek(i * 124, 0)
        # read 124 bytes
        dataRecordAllBytes = fIn.read(124)
        
        dataRecordUnPacked = unpack(dataFormat, dataRecordAllBytes)

        csv_out.writerow(dataRecordUnPacked)
        
        
finally:
    fIn.close()
    fOut.close()
