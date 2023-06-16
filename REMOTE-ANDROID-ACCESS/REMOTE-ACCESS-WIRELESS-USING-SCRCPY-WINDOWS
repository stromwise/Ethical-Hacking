# REMOTE-ACCESS-WIRELESS-USING-SCRCPY-ON-SAME-NETWORK
_________________________________________________________________________________________________________________________________________________________________

# REQUIREMENTS:
ADB 
CMD
SCRCPY
ANDROID DEVICE 
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Download the ADB binary for Windows from the official Android SDK Platform-Tools page: https://developer.android.com/studio/releases/platform-tools

Extract the downloaded ZIP file to a folder on your computer. For example, you can extract it to C:\adb.

Open Command Prompt:

Press the Windows key.
Type "cmd".
Click on "Command Prompt" or "Command Prompt (Admin)" to open the Command Prompt window.
Navigate to the folder where you extracted the ADB files. In our example, you would use the following command:


=>  cd C:\adb
Connect your Android device to your computer using a USB cable.

Enable USB debugging on your Android device:

Go to "Settings" on your Android device.
Scroll down and tap on "About phone" or "About device."
Locate "Build number" and tap it seven times to enable Developer options.
Go back to the main settings menu and find "Developer options" or "Developer settings."
Enable "USB debugging" or "Android debugging."
Test if ADB is working by running the following command in Command Prompt:

=>  adb devices
If you see a device listed with a device ID, it means ADB is successfully installed and recognized your Android device.

You can now use ADB commands in Command Prompt to interact with your Android device, such as installing apps, transferring files, and executing various commands.
_________________________________________________________________________________________________________________________________________________________________________________________________________________

If you encounter the error "'adb' is not recognized as an internal or external command, operable program or batch file" when running the adb devices command, it means that the ADB executable is not found in the system's PATH.

To resolve this issue, you can try the following steps:

Make sure you have extracted the ADB files to the correct folder (e.g., C:\adb).

Open the Start menu and search for "Environment Variables."

Click on "Edit the system environment variables."

In the System Properties window, click on the "Environment Variables" button.

In the Environment Variables window, under the "System variables" section, scroll down and find the "Path" variable.

Select the "Path" variable and click on the "Edit" button.

In the Edit Environment Variable window, click on the "New" button.

Enter the path to the ADB folder (e.g., C:\adb), and click "OK" to add it to the list of paths.

Click "OK" in the Environment Variables window and then "OK" in the System Properties window to save the changes.

Close and reopen Command Prompt, and try running the adb devices command again.

Now, the adb command should be recognized, and you should be able to use ADB to interact with your Android device.
___________________________________________________________________________________________________________________________________________________________________________________________________________________
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
