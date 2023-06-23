# REMOTE-ACCESS-WIRELESS-USING-SCRCPY-ON-SAME-NETWORK
___________________________________________________________________________________________________________________________________________________________________________________________________________________
# REQUIREMENTS:
ADB 
CMD
SCRCPY
ANDROID DEVICE 
___________________________________________________________________________________________________________________________________________________________________________________________________________________

# To install Scrcpy on Kali Linux, you can follow these steps:

Open a terminal in Kali Linux.

Update the package repository by running the following command:
=>  sudo apt update


Install the required dependencies by running the following command:
=>  sudo apt install scrcpy


During the installation, you may be prompted to confirm the installation and provide your password. Enter your password and proceed with the installation.

Once the installation is complete, you can connect your Android device to your computer via USB.

To use Scrcpy, run the following command in the terminal:
=>  scrcpy


This will start the Scrcpy application and display the screen of your connected Android device on your computer.
You can control your Android device using your computer's mouse and keyboard. For example, you can click on the screen, type on the virtual keyboard, and perform various other actions.
That's it! You now have Scrcpy installed on your Kali Linux system and can use it to mirror and control your Android device.
___________________________________________________________________________________________________________________________________________________________________________________________________________________
# To install ADB (Android Debug Bridge) on Kali Linux, you can follow these steps:

Open a terminal in Kali Linux.

Update the package repository by running the following command:
=>  sudo apt update


Install the ADB package by running the following command:
=>  sudo apt install adb

During the installation, you may be prompted to confirm the installation and provide your password. Enter your password and proceed with the installation.

Once the installation is complete, you can verify if ADB is installed correctly by running the following command:
=>  adb version

If ADB is installed successfully, you should see the ADB version information in the terminal.
Now you have ADB installed on your Kali Linux system. You can use it for various tasks, such as connecting to Android devices, installing applications, and debugging.
___________________________________________________________________________________________________________________________________________________________________________________________________________________
# GET THE IP ADDRESS OF THE ANDROID DEVICE 

# CONNECT THE DEVICE TO THE COMUPTER USING THE WIRE

# OPEN A TERMINAL 

# CONNECT THE ANDROID DEVICE TO THE SYSTEM AND TYPE:
=>  ADB DEVICES

# IF IT SHOWS THEN TYPE :
=>  adb tcpip PORTNUMBER(ON WHICH YOU WANT THE DEVICE TO CONNECT)

# ENTER THE IP ADDRESS OF THE DEVICE (SETTINGS> WIFI> OPEN THE SSID> CAN CHECK THE IP ADDRESS)
=>  adb connect 192.168.0.146:PORTNUMBER(WHICH WAS DEFINED ABOVE)

# DOWNLOAD SCRCPY AS I MENTIONED IN THE PREVIOUS FILES.
=>  NOW OPEN THE SCRCPY FOLDER.
=>  RUN THE SCRCPY.EXE 
BOOM YOUR ANDROIOD DEVICE WILL BE CONNECTED TO YOUR SYSTEM. 

##### TO KILL THE SERVER TYPE THE COMMAND :
=>>  adb kill-server
___________________________________________________________________________________________________________________________________________________________________________________________________________________

