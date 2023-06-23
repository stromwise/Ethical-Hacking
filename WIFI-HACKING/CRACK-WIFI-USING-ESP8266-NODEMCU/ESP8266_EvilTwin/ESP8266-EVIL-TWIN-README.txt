# IN THIS TUTORIAL YOU WILL LEARN HOW TO CREATE AND USE ESP8266 WIFI MODULE TO CREATE EVIL-TWIN ACCORDING TO VICTIM WIFI.

### SSID -> WHITE
### PASSWORD -> White@00

# Download latest release.bin file from here :->  https://deauther.com/


STEP 1:->  connect the NODEMCU with the pc/laptop

STEP 2:->  open device manager -> select the port and update the drivers automatically 

STEP 3:->  open https://deauther.com follow the instructions to download the release.bin file and the drivers.

STEP 4:->  download the nodemcu flasher

STEP 5:->  run the flasher and select the port 

STEP 6:->  open conf -> slect the release.bin file 

STEP 7:->  select advanced -> select BAUDRATE according to your node mcu(look at its back)

STEP 8:->  then click flash

STEP 9:->  now open arduino

STEP 10:->  and open the evil-twin file 

STEP 11:->  and you can make changes for BSSID/PASSWORD according to you. Currently it is set to 

STEP 12:->  BSSID :-> WHITE

STEP 13:->  PASSWORD :-> White@00

STEP 14:->  192.168.4.1

STEP 15:->  now select the taget you want to clone 

STEP 16:->  click clone/evil-twin at the top 

STEP 18:->  now run the second ESP8266 module for deauthing the target 

STEP 19:->  now once the target will put the correct wifi password in the cloned wifi then only you will be able to log back in to your evil-
twin

STEP 20:->  once victim enters the password the cloned wifi will be automatically closed.

STEP 21:->  and just refresh the page and you will see the passwod of the victim's wifi
