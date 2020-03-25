# RP NMAP
#### IP address 10.10.183.82

###### NMAP Scan
```
root@hackers:/home/kowama/Documents/tryhackme/rpnmap# nmap -sC -sV 10.10.183.82
Starting Nmap 7.80 ( https://nmap.org ) at 2020-03-25 16:54 +01
Nmap scan report for 10.10.183.82
Host is up (0.19s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 ad:6d:1f:e8:78:8e:55:fb:a1:f5:fd:33:94:6f:fd:5b (DSA)
|   2048 45:e6:64:1a:4b:2c:5e:24:29:8d:0c:30:67:57:e7:a8 (RSA)
|   256 73:61:6a:23:f7:ef:f2:65:01:68:8c:8e:12:b7:1f:cb (ECDSA)
|_  256 12:50:20:4d:5d:98:87:b8:cf:c0:dd:a4:0a:93:ad:fb (ED25519)
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.7 (Ubuntu)
| http-title: Login :: Damn Vulnerable Web Application (DVWA) v1.10 *Develop...
|_Requested resource was login.php
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
* Vuln scan
```
root@hackers:/home/kowama/Documents/tryhackme/rpnmap# nmap -vv --script vuln  10.10.183.82
Starting Nmap 7.80 ( https://nmap.org ) at 2020-03-25 17:06 +01
NSE: Loaded 105 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 17:06
Completed NSE at 17:06, 10.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 17:06
Completed NSE at 17:06, 0.00s elapsed
Initiating Ping Scan at 17:06
Scanning 10.10.183.82 [4 ports]
Completed Ping Scan at 17:06, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 17:06
Completed Parallel DNS resolution of 1 host. at 17:06, 0.07s elapsed
Initiating SYN Stealth Scan at 17:06
Scanning 10.10.183.82 [1000 ports]
Discovered open port 80/tcp on 10.10.183.82
Discovered open port 22/tcp on 10.10.183.82
Increasing send delay for 10.10.183.82 from 0 to 5 due to 89 out of 295 dropped probes since last increase.
Increasing send delay for 10.10.183.82 from 5 to 10 due to max_successful_tryno increase to 4
Completed SYN Stealth Scan at 17:07, 26.43s elapsed (1000 total ports)
NSE: Script scanning 10.10.183.82.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 17:07
NSE Timing: About 98.52% done; ETC: 17:07 (0:00:00 remaining)
NSE Timing: About 98.52% done; ETC: 17:08 (0:00:01 remaining)
NSE Timing: About 98.52% done; ETC: 17:08 (0:00:01 remaining)
NSE Timing: About 98.52% done; ETC: 17:09 (0:00:02 remaining)
NSE Timing: About 98.52% done; ETC: 17:09 (0:00:02 remaining)
NSE Timing: About 98.52% done; ETC: 17:10 (0:00:03 remaining)
NSE Timing: About 98.52% done; ETC: 17:10 (0:00:03 remaining)
NSE Timing: About 98.52% done; ETC: 17:11 (0:00:04 remaining)
NSE Timing: About 98.52% done; ETC: 17:11 (0:00:04 remaining)
NSE Timing: About 98.52% done; ETC: 17:12 (0:00:05 remaining)
Completed NSE at 17:12, 310.89s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 17:12
Completed NSE at 17:12, 0.82s elapsed
Nmap scan report for 10.10.183.82
Host is up, received echo-reply ttl 63 (0.19s latency).
Scanned at 2020-03-25 17:06:39 +01 for 339s
Not shown: 998 closed ports
Reason: 998 resets
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack ttl 63
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
80/tcp open  http    syn-ack ttl 63
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|       httponly flag not set
|   /login.php: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|   /login.php: Possible admin folder
|   /robots.txt: Robots file
|   /config/: Potentially interesting directory w/ listing on 'apache/2.4.7 (ubuntu)'
|   /docs/: Potentially interesting directory w/ listing on 'apache/2.4.7 (ubuntu)'
|_  /external/: Potentially interesting directory w/ listing on 'apache/2.4.7 (ubuntu)'
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_      http://ha.ckers.org/slowloris/
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php

```
