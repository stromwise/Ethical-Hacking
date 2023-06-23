### creating open wrt using raspberry pi model 4-B

# download wrt and install it on the raspberry pi 

# connect it with a lan cable and connect the lan cable to the computer

# nOw change the ethernet settings in control panel



Step 1 :->  click ethernet

Step 2 :->  properties

Step 3 :->  IPv4 properties

Step 4 :->  manual IP and enter these details

Step 5 :->  192.168.1.10

Step 6 :->  255.255.255.0

Step 7 :->  192.168.1.1



## open cmd 



Step 1 :->  ssh root@192.168.1.1

Step 2 :->  yes

Step 3 :->  passwd (set a password)

Step 4 :->  cd /etc/config

Step 5 :->  ls

Step 6 :->  cp firewall.bk

Step 7 :->  cp network.bk

Step 8 :->  cp wireless.bk

Step 9 :->  vi network

Step 10 :->  change lan ip. (press I key to insert)

Step 11 :->  10.28.28.1 (you have to give the ip which you want your wrt to be on)

Step 12 :->  option force_link '1' (add this line at last of CONFIG LAN)

Step 13 :->  add a new line

Step 14 :->  config interface 'wwan'

Step 15 :->  option proto 'dhcp'

Step 16 :->  option peer dns '0'

Step 17 :->  option dns '1.1.1.1 8.8.8.8'

Step 18 :->  give a line space 

Step 19 :->  config interface 'vpnclient'

Step 20 :->  option ifname 'tun0'

Step 21 :->  option proto 'none'

Step 22 :->  to save click ESC then colon(:) then type wq then enter

Step 23 :->  now type 

Step 24 :->  vi firewall

Step 25 :->  under option zon [wan] change option input  REJECT to ACCEPT

Step 26 :->  then save and exit

Step 27 :->  reboot

Step 28 :->  now go back to control panel and reset the ethernet settings back to normal which we 

changed at the begining of the tutorial.

Step 29 :->  open cmd

Step 30 :->  ssh root@ipaddress which you provided earlier in this case we provided (10.28.28.1)

Step 31 :->  yes => password you set earlier

Step 32 :->  vi /etc/config/wireless  {changes will be made to radio 0}

Step 33 :->  option channel = 7

Step 34 :->  option bang = number g

Step 35 :->  option htmode = HT20

Step 36 :->  add one line = option short_gi_40 'O'

Step 37 :->  option disabled '0'

Step 38 :->  save & exit

Step 39 :->  uci commit wireless

Step 40 :->  wifi

Step 41 :->  now open web browser & type the IPAddress you assigned earlier 10.28.28.1

Step 42 :->  now login with the ID & PASSWORD you set for WRT (this is the gui of wrt to connect to 
wifi)

Step 43 :->  click NETWORK => Wireless

Step 44 :->  click radio 0 SCAN

Step 45 :->  connect to the free/any network (wifi) you want to connect 

Step 46 :->  click wireless configuration replace check box

Step 47 :->  then enter the password for the wifi 

Step 48 :->  submit

Step 49 :->  save => save & apply

Step 50 :->  get back to cmd

Step 51 :->  ping google.com

Step 52 :->  CTRL + C

Step 53 :->  opkg update

Step 54 :->  opkg install kmod-rt2800-lib kmod-rt2800-usb kmod-rt2x00-lib kmod-rt2x00-usb kmod-usb-core 
kmod-usb-uhci kmod-usb-ohci kmod-usb2 usbutils openvpn-openssl luci-app-openvpn nano

Step 55 :->  lsusb

Step 56 :->  connect the network adapter

Step 57 :->  lsusb

Step 58 :->  ifconfig wlan1up

Step 59 :->  ifconfig

Step 60 :->  open web browser log back in gui of wrt

Step 61 :->  network => wireless => enable the adapter

Step 62 :->  open cmd back

Step 63 :->  nano /etc/config/wireless

Step 64 :->  now you will see radio 1 it is the adapter

Step 65 :->  change option disabled = '0'

Step 66 :->  chane SSID = 'White_travel' (or any name you want to give to your wrt wifi)

Step 67 :->  option encryption = 'psk2'

Step 68 :->  add this line => option key 'WHite@00' (this will be the password for your wrt wifi)

Step 69 :->  save and exit

Step 70 :->  uci commit wireless

Step 71 :->  wifi

Step 72 :->  open web browser & log back in

Step 73 :->  network => wireless

Step 74 :->  enable the adapter

Step 75 :->  save & apply



### BOOM 



## NOW YOU CAN CONNECT TO WHITE_TRAVEL SO WHENEVER YOU GO OUT JUST CONNECT TO THE WIFI YOU WANT TO USE AND THEN CONNECT YOUR DEVICES TO THE WHITE_TRAVEL AND USE THE WIFI SEEMLESSLY AND SAFELY



### ADD VPN SERVICE TO YOUR WRT



Step 1 :->  first create a NORD VPN account

Step 2 :->  then open web browser and  search nordvpn/servers/

Step 3 :->  choose one according to your region

Step 4 :->  click show available protocols

Step 5 :->  download open vpn udp config file from there

Step 6 :->  open another cmd

Step 7 :->  cd to the folder where udp file is downloaded

Step 8 :->  scp filename root@10.28.28.1:/etc/openvpn/client.conf

Step 9 :->  enter password for wrt raspberry pi

Step 10 :->  open wrt cmd back

Step 11 :->  cd /etc/openvpn

Step 12 :->  ls (client.conf must be there)

Step 13 :->  install packages

Step 14 :->  opkg update

Step 15 :->  opkg install luci-app-openvpn

Step 16 :->  /etc/init.d/rpcd restart



# configuration parameters



Step 1 :->  OVPN_DIR = "/etc/openvpn"

Step 2 :->  OVPN_ID = "client"

Step 3 :->  OVPN_USER = "Nord VPN username" (enter the username for the nord vpn service)

Step 4 :->  OVPN_PASS = "Nord VPN password" (enter the password for the nord vpn service)

Step 5 :->  save username and password credintials

Step 6 :->  umask go =

Step 7 :->  cat << EOF >>${OVPN_DIR}/${OVPN_ID}.auth

Step 8 :->  ${OVPN_USER}

Step 9 :->  ${OVPN_PASS}

Step 10 :->  EOF



## CONFIGURE VPN SERVICES :-



Step 11 :->  sed -i -e "/^auth-user-pass/s/^/#/\$a auth-user-pass ${OVPN_ID}.auth/^redirect-gateway /s/^/#/\$a redirect-gateway def1 ipv6"${OVPN_DIR}/$ {OVPN_ID}.conf/etc/init.d/openvpn restart



## provide VPN management in web GUI 



Step 18 :->  ls /etc/openvpn/*.conf \

Step 19 :->  | while read -r OVPN_CONF

Step 20 :->  do

Step 21 :->  OVPN_ID = "$(basename ${OVPN_CONF%.*} | sed -e "s/\w/_/g")"

Step 22 :->  uci -q delete openvpn.$ {OVPN_ID}

Step 23 :->  uci set openvpn.${OVPN_ID}="openvpn"

Step 24 :->  uci set openvpn.${OVPN_ID}.enabled = "1"

Step 25 :->  uci set openvpn.${OVPN_ID}.config="${OVPN_CONF}"

Step 26 :->  done

Step 27 :->  uci commit openvpn

Step 28 :->  uci commit openvpn

Step 29 :->  /etc/init.d/openvpn restart



### configure firewall



Step 30 :->  uci rename firewall.@ZONE [0] = "lan"

Step 31 :->  uci rename firewall.@ZONE [1] = "wan"

Step 32 :->  uci del_list firewall.wan.device = "tun +"

Step 33 :->  uci add_list firewall.wan.device = "tun +"

Step 34 :->  uci commit firewall

Step 35 :->  /etc/init.d/firewall restart



### configure hotplug 



Step 36 :->  mkdir -h /etc/hotplug.d/online

Step 37 :->  cat << " EOF " >> /etc/hotplug.d/online/00-openvpn/etc/init.d/openvpn restart

Step 38 :->  EOF

Step 39 :->  cat << " EOF " >> /etc/sysupgrade.conf/etc/hotplug.d/online/00-openvpn

Step 40 :->  EOF



### OPEN WEB BROWSER AND LOGIN TO WRT GUI AGAIN



Step 41 :->  click VPN => click OPENVPN

Step 42 :->  click CLIENT => YES => CONNECTED

Step 43 :->  save and apply

