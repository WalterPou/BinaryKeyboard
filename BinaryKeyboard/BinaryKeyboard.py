import pyfirmata as pyf
import time
import pydirectinput as pyd
import winsound
import ctypes
from ctypes import windll

user32=ctypes.windll.user32

keyboard = input('Board: ')  # Asking user for board input
board = pyf.Arduino(keyboard)
it = pyf.util.Iterator(board)
it.start()

pin_7 = board.get_pin('d:7:i')  # Pin 7 for '0' input
pin_8 = board.get_pin('d:8:i')
pin_9 = board.get_pin('d:9:i')  # Pin 9 for '1' input
char = []
bits = 8  # Number of bits per character

VK_CODE = {
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    ' ': 0x20,
    '!': 0x31,
    '@': 0x40,
    '#': 0x23,
    '$': 0x24,
    '%': 0x25,
    '^': 0x5E,
    '&': 0x26,
    '*': 0x2A,
    '(': 0x28,
    ')': 0x29,
    '_': 0x5F,
    '+': 0xBB,
    '{': 0xDB,
    '}': 0xDD,
    '|': 0x7C,
    ':': 0xBA,
    '"': 0x22,
    '<': 0x3C,
    '>': 0x3E,
    '?': 0x3F,
    ',': 0xBC,
    '.': 0xBE,
    '/': 0xBF,
    ';': 0xBA,
    '\'': 0x27,
    '`': 0xC0,
    '\\': 0xDC,
    '[': 0xDB,
    ']': 0xDD,
    'Enter': 0x0D,
    'Backspace': 0x08,
    'Tab': 0x09,
    'Shift': 0x10,
    'Ctrl': 0x11,
    'Alt': 0x12,
    'Space': 0x20,
    'Delete': 0x2E,
    'Insert': 0x2D,
    'Home': 0x24,
    'End': 0x23,
    'PageUp': 0x21,
    'PageDown': 0x22,
    'Up': 0x26,
    'Down': 0x28,
    'Left': 0x25,
    'Right': 0x27,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
}


def binary_to_ascii(binary_str):
    """Converts a binary string to an ASCII string."""
    # Ensure the binary string is a multiple of 8 bits
    if len(binary_str) % 8 != 0:
        fast_press('Right')
        for i in range(bits+2):
            fast_press('Backspace')
        winsound.Beep(2000,150)
        raise ValueError("Binary string length must be a multiple of 8.")
    
    # Convert binary to integer, then to bytes, and decode to ASCII
    byte_data = int(binary_str, 2).to_bytes(len(binary_str) // 8, byteorder='big')
    ascii_string = byte_data.decode('ascii')
    
    return ascii_string
()
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
        fast_press(key)

def fast_press(key):
    vk_code=VK_CODE.get(key)
    user32.keybd_event(vk_code,0,0,0)
    user32.keybd_event(vk_code,0,2,0)

space=False
state=False

while True:
    while len(char)<bits:  # Collect 8 bits to form one character
        if pin_7.read() == 1:  # Pin 7 reads '0'
            print('0')
            if len(char)<1:
               fast_press('[')
               fast_press(']')
               fast_press('Left')
            #pyd.press('0')
            fast_press('0')
            #winsound.Beep(750,150)
            char.append('0')
            time.sleep(0.1)  # Small delay to avoid reading too fast
        if pin_8.read() == 1:
            print('Backspace')
            if len(char)!=0:
                state=False
                if state==False:
                    fast_press('Right')
                    state=True
            fast_press('Backspace')
            char=[]
            time.sleep(0.1)
        if pin_9.read() == 1:  # Pin 9 reads '1'
            print('1')
            if len(char)<1:
                fast_press('[')
                fast_press(']')
                fast_press('Left')
            #pyd.press('1')
            fast_press('1')
            #winsound.Beep(1000,150)
            char.append('1')
            time.sleep(0.1)  # Small delay to avoid reading too fast

    # Once 8 bits are collected, convert binary to ASCII
    binary_string = ''.join(char)  # Join the list to form a binary string
    try:
        ascii_string = binary_to_ascii(binary_string)  # Convert to ASCII
        print(f"ASCII: {ascii_string}")  # Optional: Print the ASCII output for debugging
        if binary_string!="00001010":
            fast_press('Right')
            for i in range(bits+2):
                fast_press('Backspace')
            #pyd.press('backspace',8)
            press_key(ascii_string)  # Use the new function to handle key presses
            state=False
            winsound.Beep(2000,150)
        else:
            fast_press('Right')
            for i in range(bits+2):
                fast_press('Backspace')
            #pyd.press('backspace',8)
            #time.sleep(.2)
            pyd.press('enter')
    except ValueError as e:
        fast_press('Right')
        for i in range(bits+2):
            fast_press('Backspace')
        winsound.Beep(2000,150)
        print(f"Error: {e}")
    
    # Clear the list for the next input
    char = []
