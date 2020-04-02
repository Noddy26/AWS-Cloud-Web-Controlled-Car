import socket
import RPi.GPIO as GPIO
from time import sleep


class ClientCar:

    def __init__(self):
        self.left_motor1 = 13
        self.left_motor2 = 6
        self.right_motor1 = 11
        self.right_motor2 = 5
        self.bottom_motor = 19
        self.side_motor = 26
        self.left_light = 27
        self.right_light_R = 22
        self.right_light_B = 10
        self.right_light_G = 9
        self.setup()

    def move_motors(self, data):
        data_types = {"forward": self.forward, "backward": self.backward, "left": self.left,
                      "right": self.right, "up": self.up, "down": self.down, "LEFT": self.LEFT, "RIGHT": self.RIGHT,
                      "left_light_on": self.left_light_on, "right_light_on": self.right_light_on,
                      "right_light_off": self.right_light_off, "left_light_off": self.left_light_off}
        if data in data_types:
            function = data_types[data]
            function()

    def setup(self):
        # car left 13,6
        # car right 5,11
        pins = [13, 6, 11, 5, 27, 22, 10, 9]
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.bottom_motor, GPIO.OUT)
        GPIO.setup(self.side_motor, GPIO.OUT)
        GPIO.output(self.bottom_motor, GPIO.HIGH)
        GPIO.output(self.side_motor, GPIO.LOW)
        for each in pins:
            print("setting pin %s" % each)
            GPIO.setup(each, GPIO.OUT)

    def forward(self):
        print("forward")
        GPIO.output(self.left_motor2, GPIO.HIGH)
        GPIO.output(self.left_motor1, GPIO.LOW)
        GPIO.output(self.right_motor1, GPIO.HIGH)
        GPIO.output(self.right_motor2, GPIO.LOW)
        sleep(1)
        self.car_destruct()

    def backward(self):
        print("backward")
        GPIO.output(self.left_motor1, GPIO.HIGH)
        GPIO.output(self.left_motor2, GPIO.LOW)
        GPIO.output(self.right_motor2, GPIO.HIGH)
        GPIO.output(self.right_motor1, GPIO.LOW)
        sleep(1)
        self.car_destruct()

    def left(self):
        print("Left")
        GPIO.output(self.left_motor1, GPIO.HIGH)
        GPIO.output(self.left_motor2, GPIO.LOW)
        sleep(0.5)
        self.car_destruct()

    def right(self):
        print("right")
        GPIO.output(self.right_motor2, GPIO.HIGH)
        GPIO.output(self.right_motor1, GPIO.LOW)
        sleep(0.5)
        self.car_destruct()

    def car_destruct(self):
        print("destruct")
        GPIO.output(self.left_motor1, GPIO.LOW)
        GPIO.output(self.left_motor2, GPIO.LOW)
        GPIO.output(self.right_motor1, GPIO.LOW)
        GPIO.output(self.right_motor2, GPIO.LOW)
        GPIO.cleanup()
        return

    def up(self):
        print("up")

    def down(self):
        print("down")

    def LEFT(self):
        print("LEFT")

    def RIGHT(self):
        print("RIGHT")

    def left_light_on(self):
        print("left light on")
        GPIO.output(self.left_light, GPIO.HIGH)

    def right_light_on(self):
        print("right light on")
        GPIO.output(self.right_light_R, GPIO.HIGH)
        GPIO.output(self.right_light_B, GPIO.HIGH)
        GPIO.output(self.right_light_G, GPIO.HIGH)

    def left_light_off(self):
        print("left light off")
        GPIO.output(self.left_light, GPIO.LOW)

    def right_light_off(self):
        print("right light off")
        GPIO.output(self.right_light_R, GPIO.LOW)
        GPIO.output(self.right_light_B, GPIO.LOW)
        GPIO.output(self.right_light_G, GPIO.LOW)

