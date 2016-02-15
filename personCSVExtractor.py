from struct import *
import csv

fIn = open("person.dat", "rb")
fOut = open('person.csv','w')
csv_out = csv.writer(fOut)

# define the structure
dataFormat = "7sBiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"

try:
    # every person block is 144 byte long
    for i in range(0,201):
        fIn.seek(i * 144, 0)
        # read 144 bytes
        dataRecordAllBytes = fIn.read(144)
        
        dataRecordUnPacked = unpack(dataFormat, dataRecordAllBytes)

        csv_out.writerow(dataRecordUnPacked)
        
        
finally:
    fIn.close()
    fOut.close()
