import src.modules as mod
import src.environment as env

def lighting():
    """Turns on LED when brightness is too low and the plant requires light at that time.
    """
    message = True
    while True:
        if env.LIGHT and env.BRIGHTNESS < env.BRIGHTNESS_MIN: # neglecting intervals for now
            mod.led.turn_on()
            if message == True:
                print("WARNING: The environment brightness is too low. Turning on light...")
                message = False
        else:
            mod.led.turn_off()
            message = True