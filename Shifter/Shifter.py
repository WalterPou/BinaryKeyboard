import pyfirmata as pyf
import pydirectinput as pyd
import time
import ctypes
from ctypes import windll

user32=ctypes.windll.user32
chip=input('Board: ')
board=pyf.Arduino(chip)
pin7=board.get_pin("d:7:i")
pin8=board.get_pin("d:8:i")
pin9=board.get_pin("d:9:i")
it=pyf.util.Iterator(board)
it.start()

codes={"E": 0x45, "Q": 0x51}

def fast_press(key):
    code=codes.get(key)
    user32.keybd_event(key,0,0,0)
    user32.keybd_event(key,0,2,0)
    print(key)

def Main():
    while True:
        if pin7.read()==1:
            #fast_press("Q")
            pyd.keyDown("shift")
            pyd.press("q")
            pyd.keyUp("shift")
            #pyd.press("f")
            time.sleep(.05)
        if pin8.read()==1:
            #fast_press("E")
            pyd.keyDown("shift")
            pyd.press("e")
            pyd.keyUp("shift")
            #pyd.press("r")
            time.sleep(.05)
        if pin9.read()==1:
            pyd.press("f")
            time.sleep(.05)

if __name__ == '__main__':
    Main()
