import serial
import time

# Define the serial port
port = '/dev/ttyACM0'  # Change this to the appropriate port for your system

# Establish serial communication with the Arduino Uno
arduino = serial.Serial(port, 9600)
time.sleep(2)  # Wait for the Arduino to initialize
