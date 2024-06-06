import serial
import time

arduino: serial.Serial = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)

def writeReadTest(writeData: str) -> any:
  arduino.write(bytes(writeData, 'utf-8'))
  time.sleep(0.005)
  data: any = arduino.readline()
  return data

while True:
  number: str = input("Number to send to Arduino: ")
  value: str = str(writeReadTest(number))
  print(value)
