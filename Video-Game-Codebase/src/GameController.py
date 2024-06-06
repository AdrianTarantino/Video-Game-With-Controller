import serial
import time


def writeDataToDevice(deviceSerialConnection: serial.Serial, data: str) -> None: 
  deviceSerialConnection.write(bytes(data, 'utf-8'))
  return


def readDeviceData(deviceSerialConnection: serial.Serial) -> str:
  deviceSerialConnectionResponseData: str = deviceSerialConnection.readline().decode()
  return deviceSerialConnectionResponseData


def createDeviceSerialConnection(serialPort: str) -> serial.Serial:
  for attempt in range(10):
    try:
      deviceSerialConnection: serial.Serial = serial.Serial(serialPort, 115200, timeout=1)
      return deviceSerialConnection
  
    except serial.serialutil.SerialException:
      print(f"No Serial Connection Found on {serialPort}")
    time.sleep(1)


def main() -> None:
  serialPort: str = input("Serial Port of Device: ")
  deviceSerialConnection = createDeviceSerialConnection(serialPort)
  
  while True:
    # data: str = input("Input Data: ")
    # writeDataToDevice(deviceSerialConnection, data)
    # deviceSerialConnectionResponseData: str = readDeviceData(deviceSerialConnection)
    # print(deviceSerialConnectionResponseData)
    deviceSerialConnectionResponseData = readDeviceData(deviceSerialConnection)
    print(deviceSerialConnection)


main()
