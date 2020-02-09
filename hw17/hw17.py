#! /usr/bin/env python3

import sys
import hw16
from PIL import Image
from PIL.ExifTags import TAGS

image = sys.argv[1]
mydict = Image.open(image)._getexif()

gps = mydict.get(34853)
if len(gps) != 0:
    latitude = gps[2][0][0]/gps[2][0][1] + gps[2][1][0]/gps[2][1][1]/60
    longitude = gps[4][0][0]/gps[4][0][1] + gps[4][1][0]/gps[4][1][1]/60
    print(hw16.run((latitude, longitude)))
else:
    print('Фотография не содержит геоданных')
