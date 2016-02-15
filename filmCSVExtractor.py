from struct import *
import csv

fIn = open("film.pgm", "rb")
fOut = open('film.csv','w')
csv_out = csv.writer(fOut)

# define the structure
dataFormat = "18shhh16siiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
descFormat = "96s"

try:
    # 251 for movie, 95 for desc
    for i in range(0,3000):
        fIn.seek(i * 252, 0)
        # read 252 bytes
        dataRecordAllBytes = fIn.read(252)
        
        dataRecordUnPacked = unpack(dataFormat, dataRecordAllBytes)
        
        # ensure unused
        if dataRecordUnPacked[1] != 0: 
            print dataRecordUnPacked[1]
        if dataRecordUnPacked[2] != 0: 
            print dataRecordUnPacked[2]
        if dataRecordUnPacked[3] != 0: 
            print dataRecordUnPacked[3]            

        
        # also seek the desc
        fIn.seek(0x001ec300 + (i * 96), 0)
        descRecordAllBytes = fIn.read(96)
        
        descRecordUnPacked = unpack(descFormat, descRecordAllBytes)
        
        
        allRecordUnPacked = dataRecordUnPacked + descRecordUnPacked
        csv_out.writerow(allRecordUnPacked)
        
        
finally:
    fIn.close()
    fOut.close()
