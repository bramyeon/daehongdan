import time
import src.modules as mod

MANUAL_WATER = False
MANUAL_FERTILIZER = False
PROTECTION = True

def manual():
    """Checks if the user wants to manually water or fertilize the plant in real time. 
    Remarks: PyMODI network bluetooth implementation is buggy (cannot receive signal from
             MODI Play properly), so we use keyboard inputs instead.
             We implement the manual watering and fertilizing using MODI Play joystick 
             separately in MODI Studio.
    """
    global MANUAL_WATER
    global MANUAL_FERTILIZER
    
    while True:
        key = input()
        if key in ['w', 'a']:
            MANUAL_WATER = True
            print(f"MANUAL: {key} is pressed. Watering plant manually.")
        if key in ['f', 'a']:
            MANUAL_FERTILIZER = True
            print(f"MANUAL: {key} is pressed. Fertilizing plant manually.")
        #if mod.network.joystick() in ['left', 'up']:
            #MANUAL_WATER = True
        #if mod.network.joystick() in ['right', 'up']:
            #MANUAL_FERTILIZER = True

def protect():
    """Toggle to turn on/off protection against approaching wild animals and
    bad neighbors.
    """
    global PROTECTION
    
    while True:
        if mod.button.pressed:
            PROTECTION = not PROTECTION
            if PROTECTION:
                print("MANUAL: Protection against wild animals and bad neighbors is turned ON.")
            else:
                print("MANUAL: Protection against wild animals and bad neighbors is turned OFF.")
            time.sleep(1)
                
                
