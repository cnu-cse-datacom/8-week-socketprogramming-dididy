import socket
import time
import sys
import os.path 
import os
import hashlib

FLAGS = None
class ClientSocket():
    
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.buf = 1024
        self.addr = (FLAGS.ip, FLAGS.port)

    def socket_send(self):
        file_name = FLAGS.filename
        self.socket.sendto(file_name.encode(), self.addr)
        self.socket.sendto(str(os.path.getsize(file_name)).encode(), self.addr)
    
        
        file_size = int(os.path.getsize(file_name))
        print(file_size)	
        print("%s is sending now" % file_name)

        f = open(file_name,"rb")

        filehash = hashlib.md5()
        filehash.update(open(file_name, "rb").read())


        self.socket.sendto(filehash.hexdigest().encode('utf-8'), self.addr)
        i = 0

        data = f.read(self.buf)
        get_percent = 0
        while (data):
            if(self.socket.sendto(data, self.addr)):
                hash_data = hashlib.md5(data)
                print ("dst:" + FLAGS.ip + " file_name:" + file_name)
                self.socket.sendto(hash_data.hexdigest().encode('utf-8'), self.addr)
                time.sleep(0.02)
	
                data = f.read(self.buf)
                
                if(self.buf <= file_size):
                    get_percent = (self.buf * i / file_size * 100)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\r[{0}] {1}%'.format('#'*(int(get_percent/2)), get_percent))
                    print("current_size / total_size =", self.buf * i, "/", file_size) 
                    i = i + 1


        os.system('cls' if os.name == 'nt' else 'clear')
        print('\r[{0}] {1}%'.format('#'*(int(get_percent/2)), 100))
        print("current_size / total_size =", file_size, "/", file_size) 
        print(file_name, "send completely!")
        print("md5: ",filehash.hexdigest())
        self.socket.close()
        f.close()
    
    def value_is_int(self, value):
        if (value -  int(value) < 1):
            return True
        else:
            return False

    def main(self):
        self.socket_send()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', type=str, default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=1234)
    parser.add_argument('-f', '--filename', type=str, default='test.txt')


    FLAGS, _ = parser.parse_known_args()

    client_socket = ClientSocket()
    client_socket.main()
