def ChainCode_to_BoundingBox(line):

    values=list(map(int, line.split()))

    x = values[0]
    y = values[1]

    chaincode = values[2:]

    xmin = x
    xmax = x
    ymin = y
    ymax = y

    for i in chaincode:
        if i == 0:
            y = y - 1
        elif i == 1:
            x = x + 1
            y = y - 1
        elif i == 2:
            x = x + 1
        elif i == 3:
            x = x + 1
            y = y + 1
        elif i == 4:
            y = y + 1
        elif i == 5:
            x = x - 1
            y = y + 1
        elif i == 6:
            x = x - 1
        elif i == 7:
            x = x - 1
            y = y - 1

        if x > xmax:
            xmax = x
        if x < xmin:
            xmin = x
        if y > ymax:
            ymax = y
        if y < ymin:
            ymin = y

    return xmin,xmax,ymin,ymax


#Get BOUNDARY from OVERLAY file and pass line in function
ret = ChainCode_to_BoundingBox('50 60 6 5 3 1')
#xmin = ret[0]
#xmax = ret[1]
#ymin = ret[2]
#ymax = ret[3]
#print(ret[0],ret[1],ret[2],ret[3])
