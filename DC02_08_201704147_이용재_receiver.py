import socket
import sys
import time
import os
import hashlib

FLAGS = None
class ClientSocket():

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((FLAGS.ip, FLAGS.port))
        self.buf = 1024
        self.timeout = 3

    def socket_send(self):
        while True:
            data, addr = self.socket.recvfrom(self.buf)
            data_size, addr = self.socket.recvfrom(self.buf)
            data_md, addr = self.socket.recvfrom(self.buf)
            file_name = data.decode() 
            file_size = int(data_size.decode())
            
            if data:
                print("file_name:", data.decode())
                print("file_size:", file_size)
                print("file_md:", data_md.decode('utf-8'))

            f = open(data.strip(), 'wb')

            md5 = hashlib.md5()
            i = 0

            j = 0
            while(i * self.buf <= file_size):
               data,addr = self.socket.recvfrom(self.buf)
               hash_recv, addr = self.socket.recvfrom(self.buf)

               f.write(data)

               hash_data = hashlib.md5(data).hexdigest()
               hash_md = md5.update(data)
               hash_recv = hash_recv.decode("utf-8")
               
               if(hash_recv == hash_data):
                   print(hash_data)
                   print(hash_recv)
                   print("same md5")
               else:
                   print("error")
                   j = j +1

               get_percent = (self.buf * i / file_size * 100)
               os.system('cls' if os.name == 'nt' else 'clear')
               print('\r[{0}] {1}%'.format('#'*(int(get_percent/2)), get_percent))
               print("current_size / total_size =", self.buf * i, "/", file_size)
               i = i + 1

            else:
                if(md5.hexdigest() == data_md.decode('utf-8')):
                    print("ok")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\r[{0}] {1}%'.format('#'*(int(get_percent/2)), 100))
                    print("current_size / total_size =", file_size , "/", file_size)
                    print("%s receive finished!" % file_name)
                else:
                    print("Receive failed..")
                print("Error rate : ", ((i - j ) / i) * 100, "%")


                print("(send)md5: ",data_md.decode('utf-8'))
                print("(recv)md5: ",md5.hexdigest())

                f.close()
                break;

    def main(self):
        self.socket_send()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', type=str, default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=1234)


    FLAGS, _ = parser.parse_known_args()

    client_socket = ClientSocket()
    client_socket.main()
