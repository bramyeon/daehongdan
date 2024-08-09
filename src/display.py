import src.modules as mod
import src.environment as env
import src.ir as ir

TEXT = ''

def real_time():
    """Display a summary of plant environment condition in real time.
    """
    global TEXT
    
    while True:
        text = []
        
        if env.TEMPERATURE < env.TEMPERATURE_LOW:
            text.append('COLD')
        elif env.TEMPERATURE > env.TEMPERATURE_HIGH:
            text.append('HOT')
            
        if env.HUMIDITY < env.HUMIDITY_LOW:
            text.append('DRY')
        elif env.HUMIDITY > env.HUMIDITY_HIGH:
            text.append('HUMID')
        
        if env.LIGHT and env.BRIGHTNESS < env.BRIGHTNESS_MIN:
            text.append('DARK')
            
        if ir.IR_FRONT > ir.IR_THRESHOLD or ir.IR_LEFT > ir.IR_THRESHOLD \
            or ir.IR_RIGHT > ir.IR_THRESHOLD:
            text.append('WARNING')
            
        text = ', '.join(text)
        if text == '':
            text = 'ALL GOOD :)'
        if text != TEXT:
            mod.display.text = text
            TEXT = text
        
        
