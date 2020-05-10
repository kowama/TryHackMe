
import socket
 
class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):

        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 1024):

        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)
 
    def read_until(self, data):

        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024)
 
        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]
 
        return rval
 
    def write(self, data):

        self.socket.send(data)
    
    def close(self):

        self.socket.close()


if __name__ == "__main__":
    nc=Netcat("34.245.127.255",19001)

    i=1
    while i < 1002 :    
        data= nc.read_until(">")
        word=data.split('\n')[-2]
        out = '[+'+str(i)+'] submit :'+word
        print(out)
        nc.write(word+"\n")
        i+=1

    s = ""
    print("[!] Finished")
    while True:
        data = nc.read()
        if data == "":
            break
        print(data)
        
    nc.close()
