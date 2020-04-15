# Advent of Cyber 
## Introduction

<p align="center">
    <img src="img/tree.png">
</p>

---
## [Day 1] Inventory Management

Web app comprehension

---
## [Day 2] Arctic Forum

```
gobuster dir -u http://10.10.57.35:3000/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt 
```
---
## [Day 3] Evil Elf

Packet analysis with wireshark

Hashcat to crak buddy pass

```
 hashcat -m 1800 -a 0 pass.hash /usr/share/wordlists/rockyou.txt --force
```

---
## [Day 4] Training

find file with containt the text password

```
find /$(pwd) -type f -exec grep -l "password" {} \; 
```

find IP address inside file
```
 grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' -rns $(pwd)

```

calculate sha1 of file

```
[mcsysadmin@ip-10-10-17-213 ~]$ sha1sum file1 
ce805be9ce8e6f4f69b7be621bba7d1c9d785b6d  file1
```
find user password hash : looling for shadow.bak
```
find / 2>>/dev/null | grep "shadow.bak"
```

---

## [Day 5] Ho-Ho-Hosint
Image meta-data
```
exiftool
```
web archive

---

## [Day 6] Data Elf-iltration

Analyse packet to detect data exfiltration 
stenegraphique  image

```steghide extract -sf <filename>
```

crack zip file password

```
fcrackzip -v -b -D -p /usr/share/wordlists/rockyou.txt <filename.zip>

```
---

## [Day 7] Skilling Up

basicaly a nmap scan 

---
## [Day 8] SUID Shenanigans

---
## [Day 9] Training

---

## [Day 10] Training

---
## [Day 4] Training

---
## [Day 4] Training

---
## [Day 4] Training

---
## [Day 4] Training

---

