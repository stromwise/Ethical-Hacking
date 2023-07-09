# To disable the Windows Defender Firewall on both Windows 10 and Windows 11 - 


- netsh advfirewall set allprofiles state off


and to create the bat file we will write 


- copy con disablefirewall.bat 


- netsh advfirewall set allprofiles state off


- ctrl + Z


--------------------------------------------------

- Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False

- Set-MpPreference -DisableRealtimeMonitoring $true

- Stop-Service -DisplayName "Norton AntiVirus"

- Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Privacy" -Name "EnablePrivacySettings" -Value 0 -Type DWord

- netsh advfirewall set allprofiles state off

- Set-MpPreference -EnableControlledFolderAccess Disabled

- sc stop WinDefend

- 










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


