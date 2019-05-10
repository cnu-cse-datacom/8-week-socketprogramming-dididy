import socket
import sys
import time
import os

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
            file_size = int(data_size.decode())
            if data:
                print("file_name:", data.decode())
                print("file_size:", file_size)

            f = open(data.strip(), 'wb')

            i = 0

            while(i * self.buf <= file_size):
               data,addr = self.socket.recvfrom(self.buf)
               f.write(data)
                    
               get_percent = (self.buf * i / file_size * 100)
               os.system('cls' if os.name == 'nt' else 'clear')
               print('\r[{0}] {1}%'.format('#'*(int(get_percent/2)), round(get_percent, 4)))
               print("current_size / total_size =", self.buf * i, "/", file_size)
               i = i + 1

            else:
                print("%s Finish!" % data.strip())
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
