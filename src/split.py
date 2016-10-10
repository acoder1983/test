import os
import sys
import time


def splitFile(filePath, beg, end):
    fsize = os.path.getsize(filePath)
    beg = fsize * beg / 100
    end = fsize * end / 100
    f = open(filePath, 'rb')
    bname=os.path.basename(filePath)
    newPath=filePath[:len(filePath)-len(bname)]+str(int(time.time()))+bname[bname.index('.'):]
    o = open(newPath, 'wb')
    f.seek(beg)
    length = end - beg
    cut = 1024
    while length > 0:
        b = f.read(cut)
        if len(b) < length:
            o.write(b)
        else:
            o.write(b[:length])
        length -= len(b)
    f.close()
    o.close()

if __name__ == '__main__':
    # splitFile(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    f = open('split.config', 'r')
    filePath = f.readline()
    beg = f.readline()
    end = f.readline()
    print os.path.getsize(filePath)
