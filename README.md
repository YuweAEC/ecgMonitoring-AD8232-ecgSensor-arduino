# Sensor Data Monitoring Project with Arduino Uno

Welcome to our Sensor Data Monitoring Project! This project is designed to showcase the capabilities of Arduino Uno in collecting and processing data from various sensors. By utilizing an Arduino Uno board along with Python scripting, we can effectively monitor vital parameters such as temperature, heart rate, oxygen levels, and electrocardiogram (ECG) readings.

## Components Used

### Sensors and Modules:
- **AD8232 ECG Sensor:** Captures electrocardiogram (ECG) data, providing insights into heart activity.
- **LM35 Temperature Sensor:** Offers precise temperature readings in Celsius, ideal for environmental monitoring.
- **DS18B20 Waterproof Temperature Probe:** A rugged probe for measuring temperature in aquatic environments and industrial applications.
- **MAX30102 Heart Rate and Pulse Oximeter Sensor Module:** Measures heart rate and blood oxygen levels, crucial for health monitoring.
- **5V Active Buzzer Module:** Provides audible alerts or notifications based on sensor readings.

### Hardware:
- **Arduino Uno:** The central microcontroller board responsible for interfacing with sensors and executing firmware.
- **Breadboard 840 Pin:** Offers a convenient platform for prototyping and connecting electronic components.
- **USB A to Mini B Cable:** Facilitates communication and programming of the Arduino Uno.

### Wiring Accessories:
- **Male-to-Female, Male-to-Male, and Female-to-Female Jumper Wires:** Essential for establishing connections between components on the breadboard.

## Project Overview

### Usage:
1. **Hardware Setup:** Connect the sensors and modules to the Arduino Uno following the provided circuit diagram.
2. **Firmware Installation:** Utilize the Arduino IDE to upload the firmware code to the Arduino Uno, ensuring seamless interaction with the sensors.
3. **Python Script Execution:** Run the Python script on your computer to establish communication with the Arduino Uno via the serial port and fetch sensor data.
4. **Real-time Monitoring:** The Python script continuously retrieves sensor data from the Arduino Uno, displaying it on the console for monitoring and analysis.

### Key Features:
- **Multi-Sensor Integration:** Harnesses the capabilities of multiple sensors to gather comprehensive data for diverse applications.
- **User-friendly Interface:** Employs Python scripting to facilitate easy interaction with the Arduino Uno, enabling real-time monitoring of sensor data.
- **Customizable and Expandable:** Offers flexibility for customization and expansion, allowing users to tailor the project to their specific needs and incorporate additional sensors or functionalities as desired.

## Arduino Firmware

The provided Arduino firmware code orchestrates the data acquisition process, interfacing with sensors and responding to requests from the Python script over the serial port. It retrieves sensor readings and transmits them back to Python for visualization and analysis.

## Getting Started

To embark on your journey with our Sensor Data Monitoring Project, simply follow these steps:

1. **Installation:** Install the necessary Python packages (`pyserial`) to enable communication with the Arduino Uno.
2. **Connection:** Connect the Arduino Uno to your computer via USB and ensure the correct serial port is specified in the Python script.
3. **Configuration:** Customize the project as per your requirements, adjusting sensor placement, sampling intervals, and data visualization options.
4. **Exploration:** Dive into the world of sensor data monitoring, explore various applications, and unleash the full potential of Arduino Uno in data acquisition and analysis.
