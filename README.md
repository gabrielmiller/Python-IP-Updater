# Python-IP-Updater
## About
This is a script that updates two files on my public webserver to reflect the current external IP address of my private webserver. Since I have a DSL internet connection my IP address changes periodically, such as when I restart my router. In order to keep my friends with my up-to-date IP address I wrote this script.

Two files are created, one redirects directly to my local webserver, while the other simply prints the server's external IP address.

##Technologies
This script is made in Python. It scrapes my IP address from http://curlmyip.com with urllib2, connects to my webserver through ssh with the module Paramiko, and writes the results to PHP files on my public webhost.
