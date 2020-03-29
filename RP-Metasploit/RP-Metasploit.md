# RP Metasploit
---
* #### Intro
* #### Inittializing
* #### Rock 'em to the core [Commands]
* #### Modules for Every Occasion
msf architecture

![msf architecture](img/arch.png "msf architecture")

* #### Move that shell !
##### IP Address : 10.10.209.78
db_nmap scan 
```
msf5 > db_nmap -sV 10.10.209.78
[*] Nmap: Starting Nmap 7.80 ( https://nmap.org ) at 2020-03-29 10:18 +01
[*] Nmap: Nmap scan report for 10.10.209.78
[*] Nmap: Host is up (0.17s latency).
[*] Nmap: Not shown: 988 closed ports
[*] Nmap: PORT      STATE SERVICE      VERSION
[*] Nmap: 135/tcp   open  msrpc        Microsoft Windows RPC
[*] Nmap: 139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
[*] Nmap: 445/tcp   open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
[*] Nmap: 3389/tcp  open  tcpwrapped
[*] Nmap: 5357/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
[*] Nmap: 8000/tcp  open  http         Icecast streaming media server
[*] Nmap: 49152/tcp open  msrpc        Microsoft Windows RPC
[*] Nmap: 49153/tcp open  msrpc        Microsoft Windows RPC
[*] Nmap: 49154/tcp open  msrpc        Microsoft Windows RPC
[*] Nmap: 49158/tcp open  msrpc        Microsoft Windows RPC
[*] Nmap: 49159/tcp open  msrpc        Microsoft Windows RPC
[*] Nmap: 49160/tcp open  msrpc        Microsoft Windows RPC
[*] Nmap: Service Info: Host: DARK-PC; OS: Windows; CPE: cpe:/o:microsoft:windows
[*] Nmap: Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
[*] Nmap: Nmap done: 1 IP address (1 host up) scanned in 72.39 seconds

```

For more detail go to [ice](/ice)

* #### We're in, now What?

For more detail go to [ice](/ice)

* #### Makin ' Cisco Proud

Routing trough machine to discover network

```
module : post/multi/manage/autoroute

```
proxy tunnel [here](https://www.offensive-security.com/metasploit-unleashed/proxytunnels/)

---