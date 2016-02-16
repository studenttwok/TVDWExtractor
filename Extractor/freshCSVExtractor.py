from struct import *
import csv

fIn = open("fresh.tab", "rb")
fOut = open('fresh.csv','w')
csv_out = csv.writer(fOut)

# define the structure
dataFormat = "i"

try:
    # each fresh block has 4 bytes
    for i in range(0,96):
        fIn.seek(i * 4, 0)
        # read 4 bytes
        dataRecordAllBytes = fIn.read(4)
        
        dataRecordUnPacked = unpack(dataFormat, dataRecordAllBytes)

        csv_out.writerow(dataRecordUnPacked)
        
        
finally:
    fIn.close()
    fOut.close()
