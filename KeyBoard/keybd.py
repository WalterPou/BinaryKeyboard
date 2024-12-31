import pynput.keyboard
import time

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

# Function to handle keyboard input
def on_press(key):
    global typed_binary, controller

    try:
        # Capture the character typed by the user
        if hasattr(key, 'char') and key.char is not None:
            # If the user types '0' or '1', add it to typed_binary
            if key.char == '0' or key.char == '1':
                typed_binary += key.char

            # Once we have 8 bits, process it
            if len(typed_binary) == 8:
                # Convert the 8-bit binary string to an ASCII character
                ascii_char = binary_to_ascii(typed_binary)

                if ascii_char:
                    # Clear the last 8 typed characters and type the ASCII character
                    for _ in range(8):
                        controller.press(pynput.keyboard.Key.backspace)
                        controller.release(pynput.keyboard.Key.backspace)

                    # Simulate typing the ASCII character
                    controller.type(ascii_char)
                    typed_binary = ""  # Reset the binary sequence

    except AttributeError:
        # In case of special keys (like space, enter, etc.)
        pass

# Function to stop the listener after some time (e.g., 10 seconds) or on some condition
def on_release(key):
    global typed_binary

    # If the ESC key is pressed, reset the binary input
    if key == pynput.keyboard.Key.esc:
        print("\nResetting binary input.")
        typed_binary = ""  # Clear the binary string
        # Optionally, clear the screen or the last typed text
        for _ in range(8):
            controller.press(pynput.keyboard.Key.backspace)
            controller.release(pynput.keyboard.Key.backspace)

        return False  # Stop listener on ESC key press
import pynput.keyboard
import time

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

# Function to handle keyboard input
def on_press(key):
    global typed_binary, controller

    try:
        # Capture the character typed by the user
        if hasattr(key, 'char') and key.char is not None:
            # If the user types '0' or '1', add it to typed_binary
            if key.char == '0' or key.char == '1':
                typed_binary += key.char

            # Once we have 8 bits, process it
            if len(typed_binary) == 8:
                # Convert the 8-bit binary string to an ASCII character
                ascii_char = binary_to_ascii(typed_binary)

                if ascii_char:
                    # Clear the last 8 typed characters and type the ASCII character
                    for _ in range(8):
                        controller.press(pynput.keyboard.Key.backspace)
                        controller.release(pynput.keyboard.Key.backspace)

                    # Simulate typing the ASCII character
                    controller.type(ascii_char)
                    typed_binary = ""  # Reset the binary sequence

    except AttributeError:
        # In case of special keys (like space, enter, etc.)
        pass

# Function to stop the listener after some time (e.g., 10 seconds) or on some condition
def on_release(key):
    global typed_binary

    # If the ESC key is pressed, remove the last digit of binary input
    if key == pynput.keyboard.Key.esc:
        if typed_binary:
            # Remove the last digit of binary input
            typed_binary = typed_binary[:-1]

            # Simulate backspace to remove the last typed binary digit
            controller.press(pynput.keyboard.Key.backspace)
            controller.release(pynput.keyboard.Key.backspace)

            print(f"\nResetting. Current binary: {typed_binary}")

        return True  # Stop listener on ESC key press

# Set up the keyboard controller
controller = pynput.keyboard.Controller()

# Start listening to the keyboard
listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Keep the script running
print("Start typing '0' and '1'. Press ESC to reset the last typed bit. Press ESC again to stop.")
while True:
    time.sleep(1)

# Set up the keyboard controller
controller = pynput.keyboard.Controller()

# Start listening to the keyboard
listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Keep the script running
print("Start typing '0' and '1'. Press ESC to reset. Press ESC again to stop.")
while True:
    time.sleep(1)
