import time
import src.initialize as init
import src.environment as env
import src.manual as man
import src.modules as mod

def water_motor():
    """Activates the motor for watering plant when humidity is too low, 
    or during the correct watering interval, or when manual watering button is triggered.
    """
    while True:
        current = time.time()
        if env.HUMIDITY < env.HUMIDITY_LOW or \
            (current - init.START) % init.WATERING_INTERVAL <= 5 or man.MANUAL_WATER:
            print("MODI: Watering plant...")
            man.MANUAL_WATER = False
            mod.motor_water.speed = -100, 100 # press pump (or diffuser)
            time.sleep(1)
            mod.motor_water.speed = 0,0
            time.sleep(4)
            
def fertilizer_motor():
    """Activates the motor for fertilizing the plant when manual fertilizing button is triggered.
    """
    while True:
        if man.MANUAL_FERTILIZER:
            print("MODI: Fertilizing plant...")
            man.MANUAL_FERTILIZER = False
            mod.motor_fertilizer.speed = 100, -100 # press diffuser
            time.sleep(1)
            mod.motor_fertilizer.speed = 0,0
            time.sleep(4)