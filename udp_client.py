import time
from socket import *
import asyncio
import time
import json

class Sender:

    def __init__(self, serverIP = "192.168.123.12", port=13, delay=0.016):
        self.serverIP = serverIP
        self.port = port
        self.delay = delay
        self.mode = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.pitch = 0
        self.roll = 0
        self.yaw = 0
        self.btn1 = 0
        self.btn2 = 0

    def send_date(self):
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.settimeout(1)
        addr = (self.serverIP, self.port)
        while True:
            srr = {"mode": self.mode, "x": self.x, "y": self.y, 'z': self.z, 'pitch': self.pitch, 'roll': self.roll, 'yaw': self.yaw}
            srr = json.dumps(srr)
            clientSocket.sendto(srr.encode(), addr)
            print(srr)
            time.sleep(self.delay)

    def send_button(self, btn_name):
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.settimeout(1)
        srr = {'btn_pushed': btn_name}
        addr = (self.serverIP, self.port)
        clientSocket.sendto(srr.encode(), addr)
        print(srr)


    def change_value(self, mode, x, y, z, pitch, roll, yaw, btn1, btn2):
        self.mode = mode
        self.x = x
        self.y = y
        self.z = z
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw
        self.btn1 = btn1
        self.btn2 = btn2