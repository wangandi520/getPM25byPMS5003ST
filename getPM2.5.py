#encoding=utf-8
import os
import serial
import time
from struct import *

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
    # conn = sqlite3.connect('pm25.db')
    # c = conn.cursor() 
    recv = read_pm_line(ser)

    tmp = recv[4:36]
    datas = unpack('>hhhhhhhhhhhhhhhh', tmp)
    print('Plantower PMS5003ST,Updated:',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('PM1.0(CF=1): {}ug/m3\n'
              'PM2.5(CF=1): {}ug/m3\n'
              'PM10 (CF=1): {}ug/m3\n'
              'PM1.0 (STD): {}ug/m3\n'
              'PM2.5 (STD): {}ug/m3\n'
              'PM10  (STD): {}ug/m3\n'
              '>0.3um     : {}/0.1L\n'
              '>0.5um     : {}/0.1L\n'
              '>1.0um     : {}/0.1L\n'
              '>2.5um     : {}/0.1L\n'
              '>5.0um     : {}/0.1L\n'
              '>10um      : {}/0.1L\n'
              'HCHO       : {}mg/m3\n'
              'Temperature: {}C\n'
              'Humidity   : {}%'.format(datas[0], datas[1], datas[2],
                                       datas[3], datas[4], datas[5],
                                       datas[6], datas[7], datas[8],
                                       datas[9], datas[10], datas[11],
                                       datas[12]/1000.0, datas[13]/10.0, datas[14]/10.0))
    ser.flushInput()
    time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()