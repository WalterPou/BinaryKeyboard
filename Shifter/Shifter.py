import pyfirmata as pyf
import pydirectinput as pyd
import time
import ctypes
from ctypes import windll
from pygame import mixer
import threading

user32=ctypes.windll.user32
chip=input('Board: ')
board=pyf.Arduino(chip)
pin7=board.get_pin("d:7:i")
pin8=board.get_pin("d:8:i")
pin9=board.get_pin("d:9:i")
it=pyf.util.Iterator(board)
it.start()

codes={"E": 0x45, "Q": 0x51, "P": 0x50}

def ShiftingSound():
    mixer.init()
    mixer.music.load('Explode.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.5)

def fast_press(key):
    code=codes.get(key)
    user32.keybd_event(key,0,0,0)
    user32.keybd_event(key,0,2,0)
    print(key)

def ParkingBrake():
    while True:
        press=False
        if pin9.read()==1:
            press=True
        if press==False:
            pyd.keyUp("p")
        if press==True:
            pyd.keyDown("p")
        time.sleep(.05)

thread=threading.Thread(target=ParkingBrake)
thread.start()

def Main():
    while True:
        if pin7.read()==1:
            current=time.time()
            print(current)
            #fast_press("Q")
            print("Clutch Down")
            pyd.keyDown("shift")
            print("Shifting Down")
            pyd.press("q")
            pyd.keyUp("shift")
            print("Clutch Up")
            #pyd.press("f")
            time.sleep(.05)
        if pin8.read()==1:
            current=time.time()
            print(current)
            #fast_press("E")
            print("Clutch Down")
            pyd.keyDown("shift")
            print("Shifting Up")
            pyd.press("e")
            pyd.keyUp("shift")
            print("Clutch Up")
            #pyd.press("r")
            time.sleep(.05)
        #if pin9.read()==1:
        #    pyd.press("f")
        #    time.sleep(.05)
        time.sleep(0.05)
        
if __name__ == '__main__':
    Main()
