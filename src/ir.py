import time
import src.modules as mod
import src.manual as man

IR_FRONT = -100
IR_LEFT = -100
IR_RIGHT = -100
IR_THRESHOLD = 10

def ir_proxy():
    """Monitors the IR proximity in real time to look out for
    wild animals or bad neighbors.
    """
    global IR_FRONT
    global IR_LEFT
    global IR_RIGHT
    
    while True:
        if man.PROTECTION:
            IR_FRONT = mod.ir_front.proximity
            IR_LEFT = mod.ir_left.proximity
            IR_RIGHT = mod.ir_right.proximity
            print(f"IR proximity at the FRONT/LEFT/RIGHT: {IR_FRONT} / {IR_LEFT} / {IR_RIGHT}")
            time.sleep(1)
            
            