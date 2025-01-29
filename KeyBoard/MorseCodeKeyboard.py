import pyfirmata
import time
import pynput.keyboard as pyk

# Set up Arduino
PORT = input("Board: ")
PIN = 8  # Digital pin connected to the button

board = pyfirmata.Arduino(PORT)
it = pyfirmata.util.Iterator(board)
it.start()

button = board.get_pin(f'd:{PIN}:i')  # Digital input

# Morse Code Dictionary
MORSE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '/': ' '  # Space separator
}

controller=pyk.Controller()

# Timing Variables
DOT_TIME = 0.25
DASH_TIME = 1.5
LETTER_GAP = 0.9
WORD_GAP = 1.5

current_symbol = ""
translated_text = ""
last_press_time = None

def translate_morse(morse_sequence):
    """Translate Morse code sequence to text."""
    MORSE_DICT = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '/': ' ', '.-.-': " "
    }
    return MORSE_DICT.get(morse_sequence, '?')

print("Waiting for input.")
while True:
    try:
        state = button.read()

        if state:  # Button Pressed
            print("Entering Code..")
            start_time = time.time()

            while button.read():  # Wait until button is released
                pass  # Holding...
            press_duration = time.time() - start_time
            #print(f"{press_duration:.2f}")

            if press_duration < DOT_TIME:
                current_symbol += "."
                controller.type('.')
                #print("Detected: DOT (.)")
                time.sleep(0.1)
            elif press_duration < DASH_TIME:
                current_symbol += "-"
                controller.type('-')
                #print("Detected: DASH (-)")
                time.sleep(0.1)
            else:
                print("Ignored: Press too long!")

            last_press_time = time.time()

        elif last_press_time:  # Detect letter/word spacing
            wait_time = time.time() - last_press_time

            if wait_time > LETTER_GAP:
                if current_symbol:
                    translated_text = translate_morse(current_symbol)
                    for _ in range(len(current_symbol)):
                        controller.press(pyk.Key.backspace)
                        controller.release(pyk.Key.backspace)
                    current_symbol = ""
                #print("Current Translation:", translated_text)
                controller.type(translated_text)
                last_press_time = None

    except KeyboardInterrupt:
        print("\nExiting...")
        board.exit()
        break