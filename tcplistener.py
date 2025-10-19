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
                    headerData, _, bodyData = decodedData.partition("\r\n\r\n")
                    body = bodyData.encode()
                    startLine = RequestLine(headerData.splitlines()[0])
                    header = Headers(headerData.split("\r\n")[1:])

                    contentLength = int(header.headerDict.get("Content-Length", 0))

                    if contentLength: 
                        while len(body) < contentLength:
                            moreData = conn.recv(contentLength - len(body))
                            if not moreData:
                                break
                            body += moreData
                    print("Body:", body)
                    
