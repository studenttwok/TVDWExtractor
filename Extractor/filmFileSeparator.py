f = open("film.pgm", "rb")
try:
    # 251 for movie, 95 for desc
    prefix = "data"
    fileLimit = 251
    count = 0
    fileNo = 1
    fout = open(prefix + str(fileNo), "wb")
    while True:
        byte = f.read(1)
        if byte != "":
            # write the output
            fout.write(byte)
            
            # increase the counter
            if count == fileLimit:
                count = 0
                fileNo += 1
                fout.close()
                
                if fileNo == 8001:
                    fileLimit = 95
                    prefix = "desc"
                    fileNo = 1
                
                # open new file...
                fout = open(prefix + str(fileNo), "wb")                    
                
            else :
                count+=1
            
        else:
            break
    fout.close()
finally:
    f.close()