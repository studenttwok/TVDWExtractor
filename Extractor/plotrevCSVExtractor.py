from struct import *
import csv

fIn = open("plotrev.mft", "rb")
fOut = open('plotrev.csv','w')
csv_out = csv.writer(fOut)

# define the structure
dataFormat = "i"

try:
    # each block has 4 bytes
    # after 952 there is some random info???
    for i in range(0,952):
        fIn.seek(i * 4, 0)
        # read 4 bytes
        dataRecordAllBytes = fIn.read(4)
        
        dataRecordUnPacked = unpack(dataFormat, dataRecordAllBytes)

        csv_out.writerow(dataRecordUnPacked)
        
        
finally:
    fIn.close()
    fOut.close()
