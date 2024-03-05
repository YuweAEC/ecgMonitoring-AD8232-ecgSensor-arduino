import serial
import time

# Define the serial port
port = '/dev/ttyACM0'  # Change this to the appropriate port for your system

# Establish serial communication with the Arduino Uno
arduino = serial.Serial(port, 9600)
time.sleep(2)  # Wait for the Arduino to initialize

# Function to read data from Arduino
def read_from_arduino():
    arduino.write(b'r')  # Send 'r' to request sensor data from Arduino
    data = arduino.readline().decode().strip()  # Read the response
    return data

# Main program loop
try:
    while True:
        # Read temperature from LM35 sensor
        temperature_lm35 = read_from_arduino()
        print("Temperature (LM35):", temperature_lm35)

        # Read temperature from DS18B20 sensor
        temperature_ds18b20 = read_from_arduino()
        print("Temperature (DS18B20):", temperature_ds18b20)

        # Read heart rate from MAX30102 sensor
        heart_rate = read_from_arduino()
        print("Heart Rate (MAX30102):", heart_rate)

        # Read oxygen level from MAX30102 sensor
        oxygen_level = read_from_arduino()
        print("Oxygen Level (MAX30102):", oxygen_level)

        # Read ECG data from AD8232 sensor
        ecg_data = read_from_arduino()
        print("ECG Data (AD8232):", ecg_data)

        # Read buzzer status
        buzzer_status = read_from_arduino()
        print("Buzzer Status:", buzzer_status)

        time.sleep(1)  # Wait for 1 second between readings
