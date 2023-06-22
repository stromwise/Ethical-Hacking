#!/usr/bin/env python3

import socket

print("-----------------------------------------")
host_ip = input("Enter the host IP\n>> ")

known_ports = int(input("Enter the port range limit: \n - Known ports 0-1024 (+1)\n - Registered ports 1024-49151\n - Dynamic/Private ports 49152-65535\n>> "))

for port in range(1, known_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host_ip, port))
    if 0 == result:
        print("Port {} -> Open".format(port))
    sock.close()