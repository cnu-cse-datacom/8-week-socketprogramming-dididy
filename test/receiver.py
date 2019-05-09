import socket
import sys
import select

FLAGS = None
class ClientSocket():
    
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((FLAGS.ip, FLAGS.port))
        self.addr = (FLAGS.ip, FLAGS.port)
        self.buf = 1024

    def socket_send(self):
        data,addr = self.socket.recvfrom(self.buf)
        f = open(data.strip(), 'wb')

        data,addr = s.recvfrom(self.buf)
        try:
            while(data):
                f.write(data)
                self.socket.settimeout(2)
                data,addr = s.recvfrom(self.buf)
        except timeout:
            f.close()
            self.socket.close()
            print ("File Downloaded")

    def main(self):
        self.socket_send()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', type=str, default='localhost')
    parser.add_argument('-p', '--port', type=int, default=8080)
    parser.add_argument('-f', '--filename', type=str)


    FLAGS, _ = parser.parse_known_args()

    client_socket = ClientSocket()
    client_socket.main()
