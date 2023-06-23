## IN THIS TOTURIAL YOU WILL LEARN HOW TO DISCOVER AND SCAN FOR DEVICES ON A NETWORK WITH ARP/NETDISCOVER. (sudo netdiscover -p)


STEP 0:  first spoof your mac address

STEP 1:  arp -a

STEP 2:  sudo apt install arp-scan  

STEP 3:  sudo arp-scan -h 

STEP 4:  sudo arp-scan -l (by using this anyone can know that we are using arp request as this is a noisy technique)

STEP 5:  man netdiscover

STEP 6:  sudo netdiscover (by using this anyone can know that we are using arp request as this is a noisy technique)

STEP 7:  sudo netdiscover -p (this will not get detected by another person and they will not know that we are doing arp requests)
