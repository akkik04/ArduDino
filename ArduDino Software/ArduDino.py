'''
PYTHON SCRIPT FOR THE 'ArduDino' PROJECT.
AKSHITH KANDIVANAM.

The main idea for this script is to recognize the 'keyword' sent by the Arduino/C++ script and perform the appropriate function on the famous DinoGame.
The IR remote sends a hexadecimal signal to the IR receiver, which becomes interpreted as either'jump' or 'duck' to the Python script, activating the appropriate PyAutoGUI functions to perform the 'jump' or 'duck' action on the dino in the game.
'''

'''
1. The PyAutoGUI module is mandatory because we will use its functions to perform the 'jump' movement on the dino in the game.
2. The Serial module is extremely important, as it forms the foundation for this project. The communication between both scripts is performed with the serial port ('COM3'), which is why this modules functions are important.
'''
# importing the required modules.
import pyautogui, serial

# creating a variable to allow for communication on the 'com3' port. 
# the 'serial.Serial' function takes the base parameters of: __init__(port, baudrate).
arduino_uno = serial.Serial('com3', 9600)

# creating a function to perform the task of analyzing the signal that is sent from the Arduino/C++ script.
def eval_keyword():

    # creating a variable to store the signal returned by the arduino as a string.
    signal = str(arduino_uno.readline())

    '''
    The program will print the signal returned from the Arduino/C++ script. 
    This signal will contain the keyword 'jump', indicating that the dino in the game must jump using PyAutoGUI's functions.
    '''
    print(signal)

    # creating an if-statement to check if the keyword 'jump' is present within the signal. 
    if 'jump' in signal:

        # activating the PyAutoGUI module's 'typewrite()' function to activate the space bar, default time interval (0 sec) is used.
        pyautogui.typewrite(['space'])

# creating a while-loop.
while True:

    # code to call the function to analyze the IR remote signal sent from the Arduino.
    eval_keyword()
