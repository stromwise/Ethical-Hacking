Bypass windows login screen using Kali linux live bootable media/ using chntpw

Lets start:-

Create a kali linux live usb bootable media using Rufus.

Then insert the usb and restaqrt the system.

Enter the boot mnenu using F10 / F8 / F12 / F9 whatever your system has.

then staret the kali live system (First option).

once you boot into kali then open the drives containing windows file(C:) shown on the desktop.

open WINDOWS folder.

Open SYSTEM32 folder.

Open CONFIG folder.

search for SAM file.

now right click anywher in the folder and open the CONFIG folder as ROOT.

now again right click in the folder and open a TERMINAL here.

Now thype this command:-

chntpw -i SAM 

press ENTER.

now type 1 to select EDIT USER DATA AND PASSWORD

now type the id of the user you are targeting for bypassing (example = 3e8).

chosse the option to clear the password that is option !1

now type q for QUITTING THE UTILITY 

again TYPE q 

then TYPE y to save the changes.

then shut down thew kali linux live and remove the usb bootable media and restart the windows pc the user password will be removed.











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
