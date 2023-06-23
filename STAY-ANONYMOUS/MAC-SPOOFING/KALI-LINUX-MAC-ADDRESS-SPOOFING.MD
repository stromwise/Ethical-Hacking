### HOW TO CHANGE RANDOM MAC ADDRESS OF A WIFI/NETWORK 

STEP 1-  sudo ip a 

STEP 2-  sudo ifconfig wlan0 down  (type the interface of the network card of which you want to change mac address)

STEP 3-  sudo macchanger -r wlan0  (-r = to change the mac address randomly)

STEP 4-  sudo ifconfig wlan0 up


### Changing MAC address manually (Kali)

STEP 1-  Turn off the Network adapter:

ifconfig wlan0 down

STEP 2-  Change the address using hw ether option from ifconfig using any MAC address you want:

ifconfig wlan0 hw ether 00:11:22:33:44:55

STEP 3-  Enable the interface:

ifconfig wlan0 up

STEP 4-  Check the changes of the network adapter:

ifconfig

