import scapy.all as scapy 
  
request = scapy.ARP() 
print("-----------------------------------------")
host_ip = input("Enter the host IP range [e.g: 192.168.1.1/24]\n>> ")
request.pdst = host_ip
broadcast = scapy.Ether() 
broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
request_broadcast = broadcast / request 
clients = scapy.srp(request_broadcast, timeout = 1)[0] 
print("IP\t\t\tMAC Address\n-----------------------------------------")
for element in clients: 
    print(element[1].psrc + "      " + element[1].hwsrc) 