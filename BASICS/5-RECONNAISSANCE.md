### RECONNAISSANCE

Reconnaissance, also known as information gathering, is arguably the most important of the four phases we will discuss. 
The more time you spend collecting information on your target, the more likely you are to be successful in the later phases.
Ironically, recon is also one of the most overlooked, underutilized, and misunderstood steps in PT methodologies today.

To be successful at reconnaissance, you must have a strategy. Nearly all facets 
of information gathering leverage the power of the Internet. A typical strategy 
needs to include both active and passive reconnaissance.

## Active reconnaissance includes interacting directly with the target. It is important 
to note that during this process, the target may record our IP address and log 
our activity.

## Passive reconnaissance makes use of the vast amount of information available on the web. 
When we are conducting passive reconnaissance, we are not interacting directly with the target and as such, 
the target has no way of knowing, recording, or logging our activity.
_______________________________________________________________________________________________________________________________________________________________________________


### MALTEGO 

Maltego is one of the most capable OSINT frameworks for personal and organizational
reconnaissance. It is a GUI tool that provides the capability to gather information on any
individual by extracting information that is publicly available on the internet by various
methods. It is also capable of enumerating the DNS, brute forcing the normal DNS, and
collecting the data from social media in an easily readable format.

The easiest way to access this application is to type ""maltegoce"" in the terminal.

_______________________________________________________________________________________________________________________________________________________________________________


### GOOGLE-CACHES

If something has been deleted from the internet, it does not mean it has been deleted from
Google. Every page that is visited by Google is backed up as a snapshot in Google cache
servers. Typically, it is intended to see whether Google can serve you the best available
page based on your search query.

The following links are
the first level of harvesting past data:
http://cachedview.com/
http://webcache.googleusercontent.com/search?q=cache:cyberhia.com
http://web.archive.org/web/*/

_______________________________________________________________________________________________________________________________________________________________________________
### Shodan and censys.io

Often, attackers utilize existing vulnerabilities to gain access to the system without much effort,
so one of the easiest ways to do so is to search in Shodan. Shodan is one of the craziest search engines that lets anyone
on the internet find devices connected to the internet using a variety of filters. 

It can be accessed by visiting: 
                                 https://www.shodan.io/.

Similar to Shodan attackers, now, we can also utilize the scans.io API for relevant
information gathering or Censys.io.

_______________________________________________________________________________________________________________________________________________________________________________



### HTTrack: Website Copier

$-> apt-get install webhttrack
 
 _______________________________________________________________________________________________________________________________________________________________________________



### GOOGLE-DORKING/Google directives

$-> site: = This allows you to filter Google search results only to the site
$-> allintitle: = This allows a search on all keywords at a time in the title
$-> inurl: = This allows you to search the keyword in the URL
$-> cache:example.com
$-> filetype: = This allows you to search for a particular extension or file type
$-> intitle: = This allows page title keyword search
$-> allintext: = This allows keyword search for all number of occurences
$-> link: = This allows external link searches on a page
$-> inanchor: = inanchor

_______________________________________________________________________________________________________________________________________________________________________________

 
### The Harvester: discovering and leveraging e-mail addresses

$->  ./theHarvester.py (to run the tool)

Using theHarvester is relatively simple as there are only a few command switches to set.
The options available are as follows:

-d: This identifies the domain to be searched – usually the domain or target's
website.

-b: This identifies the source for extracting the data. It must be one of the
following: Bing, BingAPI, Google, Google-Profiles, Jigsaw, LinkedIn, People123,
PGP, or All.

-l: This limit option instructs theHarvester to only harvest data from a
specified number of returned search results.

-f: This option is used to save the final results to an HTML and an XML file. If
this option is omitted, the results will be displayed on the screen and not saved.
_______________________________________________________________________________________________________________________________________________________________________________



### WHOIS LOOKUP

$:->  whois target_domain

We can conduct a further whois search by following the link provided in the 
“Referral URL:” field. You may have to search the webpage for a link to their 
Whois service. By using Safename’s whois service, we can extract a significantly 
larger amount of information

_______________________________________________________________________________________________________________________________________________________________________________



### NETCRAFT

Another great source of information is Netcraft. You can visit their site at 
http://news.netcraft.com. Start by searching for your target in the “What’s that 
site Running?”

_______________________________________________________________________________________________________________________________________________________________________________



### Host

Oftentimes, our reconnaissance efforts will result in host names rather than IP 
addresses. When this occurs, we can use the “host” tool to perform a translation for us. The host tool is built into Backtrack. We can access it by opening a 
terminal and typing:

root@bt~# host target_hostname

root@bt~# host ns1.dreamhost.com (EXAMPLE)

The host command can also be used in reverse. It can be used to translate IP 
addresses into host names. To perform this task, simply enter:

root@bt~# host IP address

_______________________________________________________________________________________________________________________________________________________________________________



### Extracting information from DNS
_______________________________________________________________________________________________________________________________________________________________________________

## NS Lookup :

NS Lookup is a tool that can be used to query DNS servers and potentially obtain records about 
the various hosts of which it is aware. 

root@bt~# man nslookup
root@bt~# nslookup

By issuing the “nslookup” command, we start the NS Lookup tool from the 
operating system. After typing “nslookup” and hitting enter, your usual “#”
prompt will be replaced with a “>” prompt. At this point you can enter the 
additional information required for NS Lookup to function.
We begin feeding commands to NS Lookup by entering the “server” keyword 
and an IP address of the DNS server you want to query. An example follows:

server 8.8.8.8

NS Lookup will simply accept the command and present you with another “>” 
prompt. Next, we specify the type of record we are looking for. During the reconnaissance process, there are many types of records that you may be interested in. 
For a complete listing of the various DNS record types and their description, you 
can use your newly acquired Google skills! If you are looking for general information, you should set the type to any by using the keyword “any”:

set type  any

If you are looking for specific information from the DNS server such as the IP 
address of the mail server that handles e-mail for the target organization, we 
would use the “set type 5 mx”

We wrap up our initial DNS interrogation with NS Lookup by entering the target domain after the next “>” prompt
_______________________________________________________________________________________________________________________________________________________________________________



### Dig

Another great tool for extracting information from DNS is “dig.” To work with 
dig, we simply open a terminal and enter the following command:
dig @target_ip

Recall that a zone transfer is used to pull multiple 
records from a DNS server. In some cases, a zone transfer can result in the target DNS server sending all the records it contains. This is especially valuable if 
your target does not distinguish between internal and external IPs when conducting a zone transfer. We can attempt a zone transfer with dig by using the 

“–t AXFR” switch.

If we wanted to attempt a zone transfer against a fictitious DNS server with an 
IP address of 192.168.1.23 and a domain name of “example.com” we would 
issue the following command in a terminal window:

dig @192.168.1.23 example.com –t AXFR

_______________________________________________________________________________________________________________________________________________________________________________



### Profiling users for password lists

Lists of commonly used passwords are available for download, and are stored locally on
Kali in the directory.

= /usr/share/wordlists directory. 

_______________________________________________________________________________________________________________________________________________________________________________

## Common User Password Profiler (CUPP)

Fortunately, Common User Password Profiler (CUPP) allows the tester to generate a word
list that is specific to a particular user. CUPP was present on Backtrack 5r3; however, it will
have to be downloaded for use on Kali. To obtain CUPP, enter the following command:

git clone https://github.com/Mebus/cupp.git

This will download CUPP to the local directory.
CUPP is a Python script and can be simply invoked from the CUPP directory by entering
the following command:

root@kali:~# python cupp.py -i

_______________________________________________________________________________________________________________________________________________________________________________

## CeWL
Using CeWL to map a website




CeWL is a Ruby app that spiders a given URL to a specified depth, optionally following
external links, and returns a list of words, which can then be used for password crackers,
such as John the Ripper

_______________________________________________________________________________________________________________________________________________________________________________

____________________________________________________________________________________________________________________________________________
▶ Name: StromWise
____________________________________________________________________________________________________________________________________________
▶ Role: Creator
____________________________________________________________________________________________________________________________________________
▶ Location: Unknown
____________________________________________________________________________________________________________________________________________
▶ GitHub: https://github.com/stromwise 
____________________________________________________________________________________________________________________________________________
▶ Instagram: https://www.instagram.com/stromwise/ 
____________________________________________________________________________________________________________________________________________
▶ Facebook: https://www.facebook.com/profile.php?id=100093706328777
____________________________________________________________________________________________________________________________________________
▶ Youtube: https://www.youtube.com/channel/UC-tafc0TqgZNnQio8Gj-hjg 
____________________________________________________________________________________________________________________________________________
▶ Twitter: https://twitter.com/StromWise 
____________________________________________________________________________________________________________________________________________
