# In this tutorial you will learn how to CREATE A KALI LINUX RUNNING MACHINE ON HEADLESS RASPBERRY-PI. 

STEP 1:  Download Kali Linux Image for the Raspberry Pi

STEP 2:  Flash the Image to the Micro SD Card

STEP 3:  Boot into Kali Linux

STEP 4:  Update Kali Linux

- apt-get update

- apt-get upgrade

- apt-get dist-upgrade



STEP 5:   passwd root    (Then enter a new password for your Kali Linux system.)

STEP 6:  Install OpenSSH Server

- apt-get install openssh-server

- update-rc.d -f ssh remove

- update-rc.d -f ssh defaults

The default keys represent a huge vulnerability since anyone can guess them. Let's change them immediately by running the following commands:

- cd /etc/ssh/

- mkdir insecure_old

- mv ssh_host* insecure_old

- dpkg-reconfigure openssh-server

This backs up the old SSH keys in another folder and generates new keys. Problem solved! Now let's make sure we can log in via root by typing:

- nano /etc/ssh/sshd_config

This will open your SSH configuration folder. Change this line:

- PermitRootLogin without-password

To this line instead:

- PermitRootLogin yes

And type Ctrl O to save the changes. If it already is correct, you don't need to change anything.

- sudo service ssh restart

- update-rc.d -f ssh enable 2 3 4 5

- sudo service ssh status

- sudo service ssh start
____________________________________________________________________________________________________________________________________________





## Create a Custom MOTD (message of the day)


STEP 1:  Nano /etc/motd

STEP 2:  Delete the contents and paste whatever you want to show up each time you log in.

____________________________________________________________________________________________________________________________________________


## Test Login via SSH


STEP 1:  ifconfig

STEP 2:  sudo apt-get install net-tools

On your personal computer, type:


STEP 3:  ssh root@(your IP address)

____________________________________________________________________________________________________________________________________________



## Configure Autologin for Headless Operation

STEP 1:  useradd -m WHT -G sudo -s /bin/bash         (create a new user named WHT (or whatever you like) with root permission)

STEP 2:  passwd WHT

STEP 3:  nano /etc/lightdm/lightdm.conf

STEP 4:  And delete the # before these lines:

- autologin-user=root

- autologin-user-timeout=0

STEP 5:  Save and exit with Ctrl X. Next, type:

STEP 6:  nano /etc/pam.d/lightdm-autologin

STEP 7:  And you'll need to change this starting on line 11:

#Allow access without authentication
auth required pam_succeed_if.so user != root quiet_success
auth required pam_permit.so

To this:

#Allow access without authentication
###auth required pam_succeed_if.so user != root quiet_success
auth required pam_permit.so

STEP 8:  Save and exit, and type "reboot" into terminal to restart your Pi to test.




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

