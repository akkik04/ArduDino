# ArduDino (Playing Dino Game with Infrared Remote)

- This project was made in relation to my [Spotuino](https://github.com/akkik04/Spotuino) project, as it also demonstrates the functionality of the Arduino Uno R3 with the Python language. The project plays the famous 'Dino Game' using an IR remote and receiver. The Arduino Uno communicates the keyword 'jump' through the COM3 port to the Python script, upon interaction with a button on the IR remote. The Python script receives this communication through the serial port and activates the appropriate PyAutoGUI function.

- The name of this project is 'ArduDino'. It is a combination of Arduino & Dino.

# Main Hardware Requirements:
Along with the main components listed below, a solderless breadboard and jumper wires were used.![ArduDino Hardware Requirements Picture](https://user-images.githubusercontent.com/81925146/147990139-cc2ee496-9e75-4997-a491-f196d482c271.png)

# Important Documentations:
## Python Module Documentations:
- **PyAutoGUI's Documentation:** I used this documentation to become familiar with the functions that the PyAutoGUI module has to offer. The PyAutoGUI module plays a crucial role in my Python script because after the signal is sent from the Arduino to the Python script, we use the functions from the PyAutoGUI module to automate interactions with the Dino character in the game. To view the PyAutoGUI module's documentation click [PyAutoGUI documentation](https://pyautogui.readthedocs.io/en/latest/#).

- **pySerial's Documentation:** I used this documentation to find out how I can receive access to the serial port. The pySerial module plays a very important role in my Python script because it plays the central role of receiving the signal from components connnected to the Arduino Uno. For this project, the communication is done through the COM3 port. To view the pySerial module's documentation click [pySerial documentation](https://pyserial.readthedocs.io/en/latest/index.html).

## Arduino Module Documentations:
- **IR Remote Documentation:** I used this documentation to familiarize myself with the uses of the IR receiver and transmitter. The IR functionality plays a crucial role in my project because the transmitter (remote) conveys a signal to the receiver, which gets passed on to the Python script to activate the appropriate function on the Dino Game. To view the IR Remote library's documentation click [IR Remote Documentation](https://github.com/Arduino-IRremote/Arduino-IRremote).
