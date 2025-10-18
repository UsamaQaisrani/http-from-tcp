import socket
from request import RequestLine, Headers

class TcpListener:
    def __init__(self) -> None:
        self.host = "localhost"
        self.port = 6842

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.host, self.port))
            sock.listen()
            print(f"Listening on port: {self.port}")

            conn, addr = sock.accept()
            with conn:
                print(f"Connection accepted from: {addr}")

                while (data := conn.recv(1024)):
                    decodedData = data.decode("utf-8")
                    startLine = RequestLine(decodedData.splitlines()[0])
                    headers = Headers(decodedData.split("\r\n")[1:])
                    body = None

                    if "Content-Length" in headers.headerDict \
                        or "Transfer-Encoding" in headers.headerDict: 
                        #POST Request
                        pass
                    else:
                        #GET Request
                        pass
