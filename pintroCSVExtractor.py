from struct import *
import csv

fIn = open("pintro.dat", "rb")
fOut = open('pintro.csv','w')
csv_out = csv.writer(fOut)

# define the structure
dataFormat = "40s"

try:
    # each intro block has 40 bytes
    for i in range(0,201):
        fIn.seek(i * 40, 0)
        # read 40 bytes
        dataRecordAllBytes = fIn.read(40)
        
        dataRecordUnPacked = unpack(dataFormat, dataRecordAllBytes)

        csv_out.writerow(dataRecordUnPacked)
        
        
finally:
    fIn.close()
    fOut.close()
