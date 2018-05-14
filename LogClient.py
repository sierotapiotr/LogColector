import socket

class LogClient:

    def connect(self):
        host = '127.0.0.1'
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = (host, 10001)
        msg = b"test"
        sock.sendall(msg)
        try:
            sock.connect(addr)
            print("s")
        except:
            print("Nie udało się połączyć")



    def sendLog(self):
        try:

        except socket.errno as e:
            print("Socket error", e)
        finally:
            sock.close()
