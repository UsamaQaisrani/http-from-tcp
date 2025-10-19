import socket
from request import *
from response import *

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

            def stopServer():
                if conn:
                    conn.shutdown(socket.SHUT_RDWR)
                    conn.close()

            with conn:
                print(f"Connection accepted from: {addr}")

                while (data := conn.recv(1024)):
                    decodedData = data.decode("utf-8")
                    headerData, _, bodyData = decodedData.partition("\r\n\r\n")
                    body = bodyData.encode()

                    startLine, err = RequestLine(headerData.splitlines()[0]).getParts()
                    if err is not None:
                        response = Response(ResponseType.BAD_REQUEST, err).createResponse()
                        stopServer()
                        break
                    method, path, version = startLine

                    headers, err = Headers(headerData.split("\r\n")[1:]).getPairs()
                    if err is not None:
                        response = Response(ResponseType.BAD_REQUEST, err).createResponse()
                        stopServer()
                        break
                
                    if method == "POST":
                        contentLength = int(headers.get("Content-Length", 0))
                        if contentLength: 
                            while len(body) < contentLength:
                                moreData = conn.recv(contentLength - len(body))
                                if not moreData or moreData == "":
                                    break
                                body += moreData
                        if contentLength < len(body):
                            message = "Incomplete data sent to the server."
                            response = Response(ResponseType.BAD_REQUEST, message).createResponse()
                            stopServer()
                            break

                    message = "All data received!"
                    response = Response(ResponseType.OK.value, message).createResponse()
                    conn.sendall(response)
                    stopServer()
                    break
                    
