#! /usr/bin/env python3
import os, socket, pickle

DNS_FILE_PATH = 'dns_data.pickle'
IP_ADDRESS = 'localhost'
PORT = 5354

if os.path.isfile(DNS_FILE_PATH):
    with open(DNS_FILE_PATH, 'rb') as f:
        dns_dict = pickle.load(f)
else:
    dns_dict = {}
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((IP_ADDRESS, PORT))
print("DNS started on %s:%d" % (IP_ADDRESS, PORT))
while True:
    data, address = server.recvfrom(512)
    name = data.decode('utf-8')
    if len(name.split()) == 2:
        line = name.split()
        if line[0] == 'ADD':
            dns_line = line[1].split(':')
            if len(dns_line) == 2:
                dns_dict[dns_line[0]] = dns_line[1]
                server.sendto(bytes("Added record %s:%s" % (dns_line[0], dns_line[1]), encoding='utf-8'), address)
            else:
                server.sendto(bytes("Incorrect format: 'ADD domain.name:0.0.0.0'", encoding='utf-8'), address)    
    elif name == 'EXIT':
        with open(DNS_FILE_PATH, 'wb') as f:
            pickle.dump(dns_dict, f)
        break
    elif name in dns_dict:
        server.sendto(bytes(dns_dict.get(name), encoding='utf-8'), address)
    else:
        server.sendto(bytes("Can't resolve the name", encoding='utf-8'), address)
