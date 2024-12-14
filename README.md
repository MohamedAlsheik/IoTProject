# IoT Project: Virtual Sensor with MQTT and mTLS

This project demonstrates a virtual sensor implementation that publishes battery levels to an MQTT broker over a secure mTLS (mutual TLS) connection. The project is ideal for learning secure IoT communication using Python and MQTT.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [License](#license)

## Overview
The virtual sensor reads the current battery level of the host machine and sends it to a specified MQTT topic. Secure communication is achieved through mTLS, ensuring both the client and the broker authenticate each other.

## Features
- Secure MQTT communication using mTLS.
- Real-time battery level monitoring and publishing.
- Configurable MQTT broker settings.
- Lightweight and easy to set up.

## Requirements
### Software
- Python 3.8 or later
- Required Python libraries:
  - `paho-mqtt`
  - `psutil`

### Hardware
- A device capable of running Python and connecting to an MQTT broker.
- A configured MQTT broker supporting SSL/TLS (e.g., Mosquitto).

### Certificates
- Root CA certificate (`ca.crt`)
- Client certificate (`client.crt`)
- Client private key (`client.key`)

Ensure these files are placed in a secure directory and update the paths in the script as needed.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MohamedAlsheik/IoTProject.git
   cd IoTProject
   ```

2. Install the required Python libraries:
   ```bash
   pip install paho-mqtt psutil
   ```

3. Update the certificate paths in the script to point to your local certificate files:
   ```python
   CA_CERT = "path_to/ca.crt"
   CLIENT_CERT = "path_to/client.crt"
   CLIENT_KEY = "path_to/client.key"
   ```

## Usage
1. Start the MQTT broker (if not already running).

2. Run the virtual sensor script:
   ```bash
   python mqtt_virtual_sensor.py
   ```

3. View the logs to confirm the sensor is publishing messages:
   ```
   Skickade batterinivå: 87%
   ```

## Project Structure
```
IoTProject
├── mqtt_virtual_sensor.py      # Main script for the virtual sensor
├── README.md                   # Project documentation (this file)
└── certs/                      # Directory for storing certificates (not included)
```

## Future Improvements
- Add support for additional sensor data (e.g., CPU usage, memory usage).
- Implement a configuration file for easier customization.
- Improve logging for better debugging.
- Add retry logic for MQTT connection failures.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute or report issues via GitHub!
