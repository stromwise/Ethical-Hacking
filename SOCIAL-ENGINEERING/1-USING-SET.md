# Using Social Engineering Toolkit (SET)
The Social Engineering Toolkit (SET) is an open-source Python-driven tool designed for pentesting. The SET is specifically designed to perform advanced attacks against human by exploiting their behavior. The attacks built into the toolkit are designed to be targeted and focused attacks against a person or organization used during a penetration test.

*SET Manual by TrustedSec: https://github.com/trustedsec/social-engineer-toolkit/raw/master/readme/User_Manual.pdf*


### Objectives
* Clone a website
* Obtain username and password 
* Generate reports for conducted pentesting

### Requisites
* Kali Linux virtual machine
* Any Windows virtual machine

## Launch SET

Log in to Kali Linux; Remember every Kali version comes with pre installed SET, to launch _(on Kali 2019.4)_ go to **Kali Menu > 13 - Social Engineering Tools > SET (Social Engineering Toolkit).** 

Accept the Terms of Services by typing **y**.

## Clone a Website


On the SET Main menu, select the first option **1) Social-Engineering Attacks** by typing the number:

```
 Select from the menu:

   1) Social-Engineering Attacks
   2) Penetration Testing (Fast-Track)
   3) Third Party Modules
   4) Update the Social-Engineer Toolkit
   5) Update SET configuration
   6) Help, Credits, and About

  99) Exit the Social-Engineer Toolkit
```

Next, choose **2) Website Attack Vectors**:
```
 Select from the menu:

   1) Spear-Phishing Attack Vectors
   2) Website Attack Vectors
   3) Infectious Media Generator
   4) Create a Payload and Listener
   5) Mass Mailer Attack
   6) Arduino-Based Attack Vector
   7) Wireless Access Point Attack Vector
   8) QRCode Generator Attack Vector
   9) Powershell Attack Vectors
  10) Third Party Modules

  99) Return back to the main menu.
```
The **Web Attack Vector** is a unique way of utilizing multiple web-based attacks in order to compromise the intended target. 

In the next menu, select **3) Credential Harvester Attack Method**.

```
   1) Java Applet Attack Method
   2) Metasploit Browser Exploit Method
   3) Credential Harvester Attack Method
   4) Tabnabbing Attack Method
   5) Web Jacking Attack Method
   6) Multi-Attack Web Method
   7) HTA Attack Method

  99) Return to Main Menu
```
The Credential Harvester Method will utilize web cloning of a website that has a login input(username and password field) and harvest all the information posted to the website.

Next, select the **2) Site Cloner**:
```
   1) Web Templates
   2) Site Cloner
   3) Custom Import

  99) Return to Webattack Menu
```
The site cloner is used to clone a website of your choice.

Next, type the **IP address of Kali Linux** and the URL to be cloned, on this example we will use _facebook.com_ as shown below:



After that, leave this terminal tab running.

## Send a Crafted Email
Now you must send the **IP address** of your **Kali** machine to a target, and trick him to click.

For this demo, we will use **Gmail**; Launch the web browser on your Kali and login to a Gmail account to compose an email.

This example will demonstrate just the technical aspect of this technique.



To create a proper link, click **edit link** and first type the actual address under **Link to**, and then type the fake URL in the **Text to display** field. 



You can verify the fake URL by clicking one time, it will display the actual URL.



## Log in to the Cloned Website
Log in to **Windows** as a victim, launch the web browser and sign in to your email (the account that you sent the phishing email).



When the victim clicks the URL, will be presented with a replica of facebook.com. The victim will be prompted to enter his/her username and password into the form fields. After the victim enters the Username and Passwords and clicks log in, it does not allow logging in; instead, it redirects to the legitimate Facebook login page, observe the URL.

## Obtain the Credentials
The **SET** on Kali Linux fetches the typed **username** and **password**, which can be used by the attacker to gain unauthorized access to the victim's account.











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


