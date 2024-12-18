import pyfirmata as pyf
import time
import pydirectinput as pyd
import winsound

keyboard = input('Board: ')  # Asking user for board input
board = pyf.Arduino(keyboard)
it = pyf.util.Iterator(board)
it.start()

pin_7 = board.get_pin('d:7:i')  # Pin 7 for '0' input
pin_8 = board.get_pin('d:8:i')
pin_9 = board.get_pin('d:9:i')  # Pin 9 for '1' input
char = []
bits = 8  # Number of bits per character

def binary_to_ascii(binary_str):
    """Converts a binary string to an ASCII string."""
    # Ensure the binary string is a multiple of 8 bits
    if len(binary_str) % 8 != 0:
        winsound.Beep(2000,150)
        raise ValueError("Binary string length must be a multiple of 8.")
    
    # Convert binary to integer, then to bytes, and decode to ASCII
    byte_data = int(binary_str, 2).to_bytes(len(binary_str) // 8, byteorder='big')
    ascii_string = byte_data.decode('ascii')
    
    return ascii_string

def press_key(key):
    """Handle key presses, including special characters like !."""
    if key == '!':
        pyd.keyDown('shift')
        pyd.press('1')
        pyd.keyUp('shift')
    elif key == '@':
        pyd.keyDown('shift')
        pyd.press('2')
        pyd.keyUp('shift')
    elif key == '#':
        pyd.keyDown('shift')
        pyd.press('3')
        pyd.keyUp('shift')
    elif key == '$':
        pyd.keyDown('shift')
        pyd.press('4')
        pyd.keyUp('shift')
    elif key == '%':
        pyd.keyDown('shift')
        pyd.press('5')
        pyd.keyUp('shift')
    elif key == '^':
        pyd.keyDown('shift')
        pyd.press('6')
        pyd.keyUp('shift')
    elif key == '&':
        pyd.keyDown('shift')
        pyd.press('7')
        pyd.keyUp('shift')
    elif key == '*':
        pyd.keyDown('shift')
        pyd.press('8')
        pyd.keyUp('shift')
    elif key == '(':
        pyd.keyDown('shift')
        pyd.press('9')
        pyd.keyUp('shift')
    elif key == ')':
        pyd.keyDown('shift')
        pyd.press('0')
        pyd.keyUp('shift')
    elif key == '{':
        pyd.keyDown('shift')
        pyd.press('[')
        pyd.keyUp('shift')
    elif key == '}':
        pyd.keyDown('shift')
        pyd.press(']')
        pyd.keyUp('shift')
    elif key == '|':
        pyd.keyDown('shift')
        pyd.press('\\')
        pyd.keyUp('shift')
    elif key == '~':
        pyd.keyDown('shift')
        pyd.press('`')
        pyd.keyUp('shift')
    elif key == '>':
        pyd.keyDown('shift')
        pyd.press('.')
        pyd.keyUp('shift')
    elif key == '<':
        pyd.keyDown('shift')
        pyd.press(',')
        pyd.keyUp('shift')
    elif key == '?':
        pyd.keyDown('shift')
        pyd.press('/')
        pyd.keyUp('shift')
    elif key == '"':
        pyd.keyDown('shift')
        pyd.press("'")
        pyd.keyUp('shift')
    elif key == ':':
        pyd.keyDown('shift')
        pyd.press(';')
        pyd.keyUp('shift')
    elif key == '+':
        pyd.keyDown('shift')
        pyd.press('=')
        pyd.keyUp('shift')
    elif key == '_':
        pyd.keyDown('shift')
        pyd.press('-')
        pyd.keyUp('shift')
    else:
        pyd.press(key)

while True:
    while len(char) < bits:  # Collect 8 bits to form one character
        if pin_7.read() == 1:  # Pin 7 reads '0'
            print('0')
            #pyd.press('0')
            winsound.Beep(750,150)
            char.append('0')
            time.sleep(0.05)  # Small delay to avoid reading too fast
        if pin_8.read() == 1:
            print('Backspace')
            pyd.press('backspace')
            time.sleep(0.05)
        if pin_9.read() == 1:  # Pin 9 reads '1'
            print('1')
            #pyd.press('1')
            winsound.Beep(1000,150)
            char.append('1')
            time.sleep(0.05)  # Small delay to avoid reading too fast

    # Once 8 bits are collected, convert binary to ASCII
    binary_string = ''.join(char)  # Join the list to form a binary string
    try:
        ascii_string = binary_to_ascii(binary_string)  # Convert to ASCII
        print(f"ASCII: {ascii_string}")  # Optional: Print the ASCII output for debugging
        if binary_string!="00001010":
            #pyd.press('backspace',8)
            press_key(ascii_string)  # Use the new function to handle key presses
            winsound.Beep(2000,150)
        else:
            #pyd.press('backspace',8)
            #time.sleep(.2)
            pyd.press('enter')
    except ValueError as e:
        winsound.Beep(2000,150)
        print(f"Error: {e}")
    
    # Clear the list for the next input
    char = []
