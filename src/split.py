import os
import sys


def splitFile(filePath, beg, end):
    fsize = os.path.getsize(filePath)
    beg = fsize * beg / 100
    end = fsize * end / 100
    f = open(filePath, 'rb')
    o = open('1.rmvb', 'wb')
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
