def hsv(HSV, num):
    for i in range(0, num, 16):
        numcol = (255, i, 0)
        hexcol = '#%02x%02x%02x' % numcol
        HSV.append(hexcol)

    for i in range(0, num, 16):
        numcol = (255 - i, 255, 0)
        hexcol = '#%02x%02x%02x' % numcol
        HSV.append(hexcol)

    for i in range(0, num, 16):
        numcol = (0, 255, i)
        hexcol = '#%02x%02x%02x' % numcol
        HSV.append(hexcol)

    for i in range(0, num, 16):
        numcol = (0, 255 - i, 255)
        hexcol = '#%02x%02x%02x' % numcol
        HSV.append(hexcol)

    for i in range(0, num, 16):
        numcol = (i, 0, 255)
        hexcol = '#%02x%02x%02x' % numcol
        HSV.append(hexcol)

    for i in range(0, num, 16):
        numcol = (255, 0, 255 - i)
        hexcol = '#%02x%02x%02x' % numcol
        HSV.append(hexcol)