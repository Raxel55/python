#! /usr/bin/env python3

from PIL import Image
import sys

if len(sys.argv)!=3:
    print("Enter a size argument and filename")
else:
    if (sys.argv[1].isdigit()):
        size = (int(sys.argv[1]), int(sys.argv[1]))
        try:
            img = Image.open(sys.argv[2])
            img.thumbnail(size)
            img.save("thumb-" + sys.argv[2])
        except(Exception):
            print("Can't open the file")
    else:
        print("Size need be integer")
