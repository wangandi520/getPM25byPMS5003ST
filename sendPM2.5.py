# encoding=utf-8
import os
import serial
import time
import requests
from struct import *

# pip install requests

ser = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=2.0)


def read_pm_line(_port):
    rv = b''
    while True:
        ch1 = _port.read()
        if ch1 == b'\x42':
            ch2 = _port.read()
            if ch2 == b'\x4d':
                rv += ch1 + ch2
                rv += _port.read(38)
                return rv


def main():
    recv = read_pm_line(ser)

    tmp = recv[4:36]
    datas = unpack('>hhhhhhhhhhhhhhhh', tmp)
    sendData = datas[0], datas[1], datas[2], datas[3], datas[4], datas[5], datas[6], datas[
        7], datas[8], datas[9], datas[10], datas[11], datas[12]/1000.0, datas[13]/10.0, datas[14]/10.0
    sendData = str(tuple(sendData))
    tmp = sendData.split(' ')
    sendData = ''.join(tmp)
    url = 'http://127.0.0.1/pm25/receivePM2.5.php?pm=' + sendData[1:-1]
    print(url)
    se = requests.Session()
    response = requests.get(url)
    if response.status_code == 200:
        resp = se.get(url)
    print(sendData)
    ser.flushInput()
    time.sleep(0.1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != N