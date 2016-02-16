from struct import *
import csv

fIn = open("plotint.mft", "rb")
fOut = open('plotint.csv','w')
csv_out = csv.writer(fOut)

# define the structure
dataFormat = "i"

try:
    # each block has 4 bytes
    for i in range(0,1560):
        fIn.seek(i * 4, 0)
        # read 4 bytes
        dataRecordAllBytes = fIn.read(4)
        
        dataRecordUnPacked = unpack(dataFormat, dataRecordAllBytes)

        csv_out.writerow(dataRecordUnPacked)
        
        
finally:
    fIn.close()
    fOut.close()
