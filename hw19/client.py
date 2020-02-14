#! /usr/bin/env python3

IP_ADDRESS = 'localhost'
PORT = 5354

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = input("Type a message(EXIT for exit): ")
    client.sendto(bytes(data, encoding = 'utf-8'),(IP_ADDRESS, PORT))
    if data == 'EXIT':
        break
    else:
        recvdata, address = client.recvfrom(512)
        print("Received from %s: %s" % (address, recvdata.decode('utf-8')))

