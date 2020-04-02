import socket


class Socket:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "95.44.225.20"
        port = 2005
        self.s.connect((host, port))

    def forward(self):
        self.s.send("forward".encode())

    def backward(self):
        self.s.send("backward".encode())

    def left(self):
        self.s.send("left".encode())

    def right(self):
        self.s.send("right".encode())

    def up(self):
        print("up")

    def down(self):
        print("down")

    def LEFT(self):
        print("LEFT")

    def RIGHT(self):
        print("RIGHT")

    def left_light(self):
        print("left light on")

    def right_light(self):
        print("right light on")
