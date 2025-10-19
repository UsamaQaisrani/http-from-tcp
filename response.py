from enum import Enum
class Response:
    def __init__(self, statusCode, message) -> None:
        self.statusCode = statusCode
        self.message = message

    def createResponse(self):
        body = b"This is a response from the server\n"
        startline = f"HTTP/1.1 {self.statusCode[0]} {self.statusCode[1]}\r\n"
        contentLength = f"Content-Length: {len(body)}\r\n"
        contentType = f"Content-Type: text/plain\r\n\r\n"
        header = startline + contentLength + contentType
        response = header.encode("utf-8") + body
        return response

class ResponseType(Enum):
    OK = (200, "OK")
    NOT_FOUND = (404, "NOT FOUND")
    INTERNAL_ERROR = (500, "INTERNAL SERVER ERROR.")
    BAD_REQUEST = (400, "BAD REQUEST SENT.")


