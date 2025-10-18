import socket

class TcpListener:
    def __init__(self) -> None:
        self.host = "localhost"
        self.port = 6842

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.host, self.port))
            sock.listen()

            conn, addr = sock.accept()
            while conn:
                print(f"Connection accepted from: {addr}")

                while (data := conn.recv(1024)):
                    print(data.decode(), end="")
