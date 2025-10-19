from enum import Enum

class RequestLine:
    def __init__(self, line):
       self.line = line 

    def getParts(self):
        parts = self.line.split(" ")
        if len(parts) == 3:
            return (parts, None)
        else:
            err = "Invalid startline for the request header."
            return (parts, err)

class Headers:
    def __init__(self, lines):
        self.lines = lines

    def getPairs(self):
        headerDict = {}
        for line in self.lines:
            if line == "":
                break
            if ":" not in line:
                err = "Invalid header, expected key:value pairs."
                return (headerDict, err)
            key, value = line.split(":", 1)
            headerDict[key.strip()] = value.strip()
        return (headerDict, None)

class RequesType(Enum):
    GET = "GET"
    POST = "POST"
