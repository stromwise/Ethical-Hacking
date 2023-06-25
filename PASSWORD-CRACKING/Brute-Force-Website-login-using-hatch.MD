# In this tutorial you will learn how to Brute-Force Nearly Any Website Login with Hatch. 

Step 1:  python2

STEP 2:  pip2 install selenium

STEP 3:  pip2 install requests



## Install the Chrome Driver


STEP 1: Next, we'll need to install the driver that allows us to control Chrome from the Python program. To do so, we will download a file from the Chrome Driver website (https://chromedriver.chromium.org/downloads), and then create a folder called webdrivers on your C drive. Move the downloaded file into this folder. While you can place it in another directory, you would need to modify the Python code.


## Download Hatch & Install

STEP 1:  git clone https://github.com/nsgodshall/Hatch.git

STEP 2:  cd Hatch

STEP 3:  python2 main.py -h

We can see the main options for Hatch here. To start, let's pick a target on our local network to attack.

A good device on your local network to test this on would be something like a router, a printer, or some other device with a login page on the network. You can select this by running an Nmap scan on the network to find any IP addresses that have port 80 open. While port 80 is the most common page for web access, you can also search for ports 81, 8080, 8081, 443 to locate the login pages of various devices.

Next, we'll need to find the subnet range so that we can scan the local network. To find this, you can use ipcalc to calculate your subnet range after finding your computer's local IP address. If your computer, for example, has an IP address of 192.168.0.3, you can run ipcalc 192.168.0.3 to get the IP range for all possible IP addresses on that network. In this case, that would be 192.168.0.0/24.

Once you know the range, run the following Nmap scan on your network, with the iprange portion changed to add the IP range of your network.

STEP 4:  sudo nmap -p 80,8080,81,8081,443 iprange

STEP 5:  python2 main.py

Enter the URL to the target website's login page into the first prompt from Hatch. It will check to make sure the website exists and can be accessed. Next, we'll need to identify the login and password elements of the website we're attacking.

STEP 6:  On our target login page, right-click on the "Username" element, then click on "Inspect." Next, click on the ellipsis (•••) to the left of the window, and a drop-down menu will appear. Click on "Copy," and then "Copy selector" to copy what Hatch will need to select and interact with this element. It should look something like "#username." 

STEP 7:  Enter the username selector into Hatch, and then repeat the process with the "Password" selector.

STEP 8:  Finally, right-click on the "Login" button to get the selector information, and add that to Hatch as well.

STEP 9:  Now that we have the elements selected, we'll set the username that we're trying to brute-force. In this case, we'll just type admin. The final step will be to select the default list that comes with Hatch. This is "passlist.txt" by default, so we'll use this list in our first attack.

