import serial.serialutil
from Game_Controllers.GameController import GameController
import serial
import time

serial.Serial()

class JoystickController(GameController):
  def __init__(self, serialPort: str, baudrate: int = 115200, timeout: int = 1):
    # Initializes Joystick Controller class, as well as establish serial connection between computer and joystick controller.
    super().__init__()
    self.joystickControllerSerialConnection = self.createDeviceSerialConnection(serialPort, baudrate, timeout)

  def createDeviceSerialConnection(self, serialPort: str, baudrate: int = 115200, timeout: int = 1) -> serial.Serial:
    # Establishes serial connection between joystick controller and computer.
    for attempt in range(10):
      try:
        deviceSerialConnection: serial.Serial = serial.Serial(serialPort, baudrate, timeout=1)
        return deviceSerialConnection
      
      except serial.serialutil.SerialException:
        print(f"Attempt {attempt} Failed! No Serial Connection Found on {serialPort}")
        time.sleep(1)

  def readDeviceData(self) -> tuple:
    # Reads data sent from the controller and decodes it.
    # Returns data in tuple formatted (xValue, yValue).
    # Data from joystick controller is formatted 'xValue yValue'.
    deviceSerialConnectionResponseData: str = self.joystickControllerSerialConnection.readline()
    print(deviceSerialConnectionResponseData)
    return (0, 0)
  
# def writeDataToDevice(deviceSerialConnection: serial.Serial, data: str) -> None: 
#   deviceSerialConnection.write(bytes(data, 'utf-8'))
#   return


# def readDeviceData(deviceSerialConnection: serial.Serial) -> str:
#   deviceSerialConnectionResponseData: str = deviceSerialConnection.readline().decode()
#   return deviceSerialConnectionResponseData


# def createDeviceSerialConnection(serialPort: str) -> serial.Serial:
#   for attempt in range(10):
#     try:
#       deviceSerialConnection: serial.Serial = serial.Serial(serialPort, 115200, timeout=1)
#       return deviceSerialConnection
  
#     except serial.serialutil.SerialException:
#       print(f"No Serial Connection Found on {serialPort}")
#     time.sleep(1)


# def main() -> None:
#   serialPort: str = input("Serial Port of Device: ")
#   deviceSerialConnection = createDeviceSerialConnection(serialPort)
  
#   while True:
#     # data: str = input("Input Data: ")
#     # writeDataToDevice(deviceSerialConnection, data)
#     # deviceSerialConnectionResponseData: str = readDeviceData(deviceSerialConnection)
#     # print(deviceSerialConnectionResponseData)
#     deviceSerialConnectionResponseData = readDeviceData(deviceSerialConnection)
#     print(deviceSerialConnection)


# main()
