# Ha Joker CTF

## Reconnaissance

IP addr : 10.10.222.221

## Scanning & Enumeration

### Nmap Scanning

open ports are 22(ssh), 80(http), 8080(http).
scan result is [here](nmap/initial)

### Directory Bruteforcing

```shell
ffuf -u http://10.10.222.221/FUZZ  -w /usr/share/wordlists/dirb/common.txt -e ".php, .txt"
```

We use ffuf :

- secret.txt
- phpinfo.php

using the hint in secret.txt we brute force <http://10.10.222.221:8080/>  to find login credentials

### http(8080) enumeration

- joomla cms installation
- backup.zip file
containing a db dump

