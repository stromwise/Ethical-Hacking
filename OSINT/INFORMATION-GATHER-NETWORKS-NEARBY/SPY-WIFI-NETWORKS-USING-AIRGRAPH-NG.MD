## IN THIS TOTURIAL YOU WILL LEARN HOW TO SPY ON NETWORKS USING AIRGRAPH-NG IN GRAPHICAL FORM.



STEP 1:  ifconfig

STEP 2:  sudo airmon-ng start wlan1  

STEP 3:  airodump-ng wlan1mon -w 'path of the file where you want to save/filename' (the file will be saved in .csv format) 

STEP 4:  hit enter and once you have a pretty good list of networks then press CNTRL+C

STEP 5:  now go to the file location you provided earlier and check that the file with filename.csv is created

STEP 6:  airgrapg-ng -i 'input file path filename.csv' -o 'output filename/path' -g capr (-i=drag and drop the .csv file it will give the file path, 
-o=drag and drop the file once again and change the fil name so the new graph file will be saved there only,   -g capr= we want graph to show the devices that are connected to the clients.)

STEP 7:  go to the file location and see there must be a png file with the filename you provided earlier and open it and you will see all the networks in a graph format which will be easier to work with.



# airgraph-ng -h (to show all type of graphs which can be used)

# -g cpg  (will show hat the device have connected to the wifi in the past)

# airodump-ng wlan1mon -w 'path of the file where you want to save/filename' -c 0 (-c= to spy on the specific channel only )











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


