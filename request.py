class RequestLine:
    def __init__(self, line) -> None:
       self.line = line 
       self.method = None
       self.path = None
       self.version = None
       self.getParts()

    def getParts(self):
        parts = self.line.split(" ")
        if len(parts) == 3:
            self.method, self.path, self.version = parts
            print(f"Method={self.method}, Path={self.path}, Version={self.version}")
        else:
            print("Invalid startline for the request header.")

class Headers:
    def __init__(self, lines) -> None:
        self.headerDict = {}
        self.lines = lines
        self.getPairs()

    def getPairs(self):
        for line in self.lines:
            if self.lines == "" or ":" not in line:
                break
            key, value = line.split(":", 1)
            self.headerDict[key.strip()] = value.strip()
        print(f"Headers: {self.headerDict}")


class Body:
    def __init__(self, data) -> None:
        self.data = data
