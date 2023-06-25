# In this tutorial you will learn how to Catch USB Rubber Duckies on Your Computer with USBRip.

Step 1:  python

step 2:  apt install python3-venv p7zip-full -y

step 3:  cd

step 4:  nano /etc/rsyslog.conf

step 5:  After it opens, scroll down and comment out the line that says: add a #comment before this line below

         #$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat

step 6:  now save and exit 

step 7:  echo '$ActionFileDefaultTemplate RSYSLOG__FileFormat' | tee /etc/rsyslog.d/usbrip.conf

         $ActionFileDefaultTemplate RSYSLOG__FileFormat

step 8:  rm -f /var/log/syslog* /var/log/messages*

step 9:  systemctl restart rsyslog



## Install USBRip

step 1:  git clone https://github.com/snovvcrash/usbrip.git
  
step 2:  cd usbrip

step 3:  chmod +x ./installers/install.sh

step 4:  sudo -H ./installers/install.sh -s

step 5:  cd

step 6:  usbrip -h

step 7:  usbrip



## Search Entire USB Event History


step 1:  usbrip events history

step 9:  usbrip events history -n 20 --table   (We can narrow down the request to the last 20 USB events and format it as a condensed table instead of a list.)










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


