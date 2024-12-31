import time
from pyfirmata import Arduino, util
import pynput.keyboard

# Initialize the Arduino board
chip=input('Board: ')
board = Arduino(chip)  # Replace with the correct port for your Arduino

# Set up the pins for input
pin7 = board.get_pin('d:7:i')  # Pin 7 for '0'
pin8 = board.get_pin('d:8:i')  # Pin 8 for '1'
pin9 = board.get_pin('d:9:i')  # Pin 9 for 'esc'
it=util.Iterator(board)
it.start()

# Function to convert binary to ASCII
def binary_to_ascii(binary_str):
    if len(binary_str) != 8:
        return None
    try:
        ascii_value = int(binary_str, 2)
        return chr(ascii_value)
    except ValueError:
        return None

# Global variable to store typed binary
typed_binary = ""

# Set up the keyboard controller
controller = pynput.keyboard.Controller()

# Function to handle the input from Arduino pins
def check_pins():
    global typed_binary

    # Read the states of the pins
    pin7_state = pin7.read()  # Reads Pin 7 (0)
    pin8_state = pin8.read()  # Reads Pin 8 (1)
    pin9_state = pin9.read()  # Reads Pin 9 (esc)

    if pin7_state is not None and pin7_state == 1:
        typed_binary += '0'  # Pin 7 is pressed, add '0' to binary string
        controller.type('0')
        print("Pin 7: 0")
        time.sleep(0.1)
    
    if pin8_state is not None and pin8_state == 1:
        typed_binary += '1'  # Pin 8 is pressed, add '1' to binary string
        controller.type('1')
        print("Pin 8: 1")
        time.sleep(0.1)
    
    if pin9_state is not None and pin9_state == 1:
        if typed_binary:
            # Remove the last digit of binary input
            typed_binary = typed_binary[:-1]

            # Simulate backspace to remove the last typed binary digit
            controller.press(pynput.keyboard.Key.backspace)
            controller.release(pynput.keyboard.Key.backspace)

            print(f"\nResetting. Current binary: {typed_binary}")
            time.sleep(0.1)


    # Once we have 8 bits, process it
    if len(typed_binary) == 8:
        # Convert the 8-bit binary string to an ASCII character
        ascii_char = binary_to_ascii(typed_binary)

        if ascii_char:
            # Clear the last 8 typed characters (if necessary)
            for _ in range(8):
                controller.press(pynput.keyboard.Key.backspace)
                controller.release(pynput.keyboard.Key.backspace)

            # Simulate typing the ASCII character
            controller.type(ascii_char)
            typed_binary = ""  # Reset the binary sequence

# Keep checking the pin states
print("Monitoring Arduino pins (Pin 7 = 0, Pin 8 = 1, Pin 9 = ESC).")
try:
    while True:
        check_pins()
        time.sleep(0.05)  # Add a small delay to avoid overloading the CPU
except KeyboardInterrupt:
    print("\nProgram terminated.")
finally:
    board.exit()  # Exit the Arduino board
