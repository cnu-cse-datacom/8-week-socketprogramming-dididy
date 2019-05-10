import socket
import sys
import time
import select

FLAGS = None
class ClientSocket():

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', FLAGS.port))
        self.buf = 1024
        self.timeout = 3

    def socket_send(self):
        while True:
            data, addr = self.socket.recvfrom(self.buf)
            data_size, addr = self.socket.recvfrom(self.buf)
            if data:
                print("file_name:", data.decode())
                print("file_size:", data_size.decode())

            f = open(data.strip(), 'wb')

            while True:
                ready = select.select([self.socket], [], [], self.timeout)
                if ready[0]:
                    data,addr = self.socket.recvfrom(self.buf)
                    f.write(data)
            else:
                print("%s Finish!" % data.strip())
                f.close()
                break;

    def main(self):
        self.socket_send()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    #parser.add_argument('-i', '--ip', type=str, default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=1234)


    FLAGS, _ = parser.parse_known_args()

    client_socket = ClientSocket()
    client_socket.main()
