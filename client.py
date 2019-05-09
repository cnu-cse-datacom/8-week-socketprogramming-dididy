import socket
FLAGS = None
class ClientSocket():
    
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def socket_send(self):
        ID = input("Please input StudentID : ")
        self.socket.sendto(ID.encode(), (FLAGS.ip, FLAGS.port))
        print("send complete")
        data,addr = self.socket.recvfrom(2000)
        print(data.decode())
        while True:
            if data.decode() == "게임을 시작합니다.":
                try:
                    input_game = input("[0]Scissor [1]Rock [2]Paper : ")
                    input_game = int(input_game)
                    a = [0,1,2]
                    if input_game not in a:
                        break
                    
                except:
                    print("Please input correctly ")
                    continue

                send_str = "game " +ID+" "+str(input_game)
                self.socket.sendto(send_str.encode(), (FLAGS.ip, FLAGS.port ))
                print("send complete")
                data,addr = self.socket.recvfrom(2000)
                print(data.decode())
            else:
                break;
        data,addr = self.socket.recvfrom(2000)
        print(data.decode())

    def main(self):
        self.socket_send()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', type=str, default='localhost')
    parser.add_argument('-p', '--port', type=int, default=8080)


    FLAGS, _ = parser.parse_known_args()

    client_socket = ClientSocket()
    client_socket.main()
