import time
import src.modules as mod
import src.initialize as init
import src.manual as man
import pandas as pd
from datetime import datetime

TEMPERATURE = -100
HUMIDITY = -100
BRIGHTNESS = -100
TEMPERATURE_LOW = 20
TEMPERATURE_HIGH = 30
HUMIDITY_LOW = 20
HUMIDITY_HIGH = 30
LIGHT = False
BRIGHTNESS_MIN = 2

def to_time(time_str):
    """Convert time string to datetime object.

    Args:
        time_str (str): Time string

    Returns:
        datetime.Object: Datetime object of current time
    """
    return datetime.strptime(time_str, "%H:%M")

def get_optimal(df, value, current_time):
    """Get optimal value for the current time in the df.

    Args:
        df (pd.Dataframe): Dataframe to search
        value (str): Dataframe column to search
        current_time (str): Current local time

    Returns:
        int/float/bool: Optimal value
    """
    assert value in ['temperature', 'humidity', 'light']
    current_time = to_time(current_time)
    for _, row in df.iterrows():
        start_time = to_time(row['start_time'])
        end_time = to_time(row['end_time'])

        # Check if current_time is within the time interval
        if start_time <= end_time:  # interval is in the same day
            if start_time <= current_time <= end_time:
                return row[value]
        else:  # interval spans midnight
            if current_time >= start_time or current_time <= end_time:
                return row[value]

    raise NameError

def environment():
    """Periodically update the optimal and read temperature, humidity, and light (brightness).
    """
    global TEMPERATURE, HUMIDITY, BRIGHTNESS
    global TEMPERATURE_LOW, TEMPERATURE_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT
    
    while True:
        temperature = pd.read_csv('data/temperature.csv')
        humidity = pd.read_csv('data/humidity.csv')
        light = pd.read_csv('data/light.csv', dtype={'light': bool})
        
        temperature = temperature[temperature['crop_name'] == init.CROP]
        humidity = humidity[humidity['crop_name'] == init.CROP]
        light = light[light['crop_name'] == init.CROP]
        
        current_time = datetime.now().strftime('%H:%M')
        TEMPERATURE_LOW = get_optimal(temperature, 'temperature', current_time) - 5
        TEMPERATURE_HIGH = get_optimal(temperature, 'temperature', current_time) + 5
        HUMIDITY_LOW = get_optimal(humidity, 'humidity', current_time) - 5
        HUMIDITY_HIGH = get_optimal(humidity, 'humidity', current_time) + 5
        LIGHT = get_optimal(light, 'light', current_time)
        print(f"Current time: {current_time}\tOptimal temperature/humidity/lighting for {init.CROP}\t: {TEMPERATURE_LOW+5} / {HUMIDITY_LOW+5} / {LIGHT}")
        
        TEMPERATURE = mod.environment.temperature
        HUMIDITY = mod.environment.humidity
        BRIGHTNESS = mod.environment.brightness
        print(f"Current time: {current_time}\tProtection: {man.PROTECTION}\tTemperature/humidity/brightness\t: {TEMPERATURE} / {HUMIDITY} / {BRIGHTNESS}")
        time.sleep(2)