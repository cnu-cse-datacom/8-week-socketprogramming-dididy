import socket
import sys
import select

FLAGS = None
class ClientSocket():
    
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((FLAGS.ip, FLAGS.port))
        self.buf = 1024
        self.addr = (FLAGS.ip, FLAGS.port)

    def socket_send(self):
        file_name = sys.argv[1]

        self.socket.sendto(file_name.encode('utf-8'),self.addr)

        f=open(file_name,"rb")
        data = f.read(self.buf)
        while (data):
            if(self.socket.sendto(data,self.addr)):
                print ("sending...")
                data = f.read(self.buf)
        self.socket.close()
        f.close()

    def main(self):
        self.socket_send()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', type=str, default='localhost')
    parser.add_argument('-p', '--port', type=int, default=8080)
    #parser.add_argument('-f', '--filename', type=str, default='test.txt')


    FLAGS, _ = parser.parse_known_args()

    client_socket = ClientSocket()
    client_socket.main()
