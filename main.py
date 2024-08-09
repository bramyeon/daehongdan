"""
Fall CoE202-B Basics of AI <Physical AI> Team 5
Bryan Nathanael Wijaya, Tivan Varghese George, Sachit Varshney
20200735, 20200829, 20220859 

Final Project Implementation for OhMyCrop
Environment: pymodi 
        * create environment (for first time)   : conda create -n pymodi
        * activate environment                  : conda activate pymodi
Notes: This environment contains PyModi and other requirements, 
       installed via pip as follows:
        $ pip install -r requirements.txt

Usage: python main.py --crop [CROP] --water [WATER]
Args: 
    --crop (str): Crop type (e.g., potato, strawberry, etc.)
    --water [WATER]: Watering time interval in hours (e.g., 2, 4.5, etc.)
Example: 
    python main.py --crop potato --water 4
    
"""

import threading
import time
import argparse
import src.initialize as init
import src.environment as env
import src.manual as man
import src.speaker as spk
import src.motor as mtr
import src.ir as ir
import src.led as led
import src.display as dis
    
if __name__ == '__main__':
    '''
    We assume to have 3 different CSV files in the data folder, 
    each for temperature (in PyMODI units), humidity (in PyMODI units), 
    and light, such as the following:
    
    1. temperature.csv
    +-------------+--------------+------------+---------------+
    |  crop_name  |  start_time  |  end_time  |  temperature  |
    +-------------+--------------+------------+---------------+
    |   potato    |   08:00      |   18:00    |      25       |
    |   potato    |   18:00      |   08:00    |      20       |
    | strawberry  |   10:00      |   17:00    |      18       |
    | strawberry  |   17:00      |   10:00    |      15       |
    +-------------+--------------+------------+---------------+
    
    2. humidity.csv
    +-------------+--------------+------------+---------------+
    |  crop_name  |  start_time  |  end_time  |   humidity    |
    +-------------+--------------+------------+---------------+
    |   potato    |   07:00      |   20:00    |      30       |
    |   potato    |   20:00      |   07:00    |      25       |
    | strawberry  |   11:00      |   17:00    |      25       |
    | strawberry  |   17:00      |   11:00    |      20       |
    +-------------+--------------+------------+---------------+
    
    3. light.csv
    +-------------+--------------+------------+---------------+
    |  crop_name  |  start_time  |  end_time  |     light     |
    +-------------+--------------+------------+---------------+
    |   potato    |   08:00      |   18:00    |     True      |
    |   potato    |   18:00      |   08:00    |     False     |
    | strawberry  |   10:00      |   17:00    |     True      |
    | strawberry  |   17:00      |   10:00    |     False     |
    +-------------+--------------+------------+---------------+
    
    The system automatically updates the optimal temperature, humidity, and light conditions 
    in real time by comparing the current time and the time range in the CSVs.
    
    '''
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--crop", default=None, type=str, help='crop type')
    parser.add_argument("--water", default=2, type=float, help='watering time interval in hours')
    args = parser.parse_args()

    print("""훌륭하신 장군님께서 조국 로동자의 편함을 위하여 백두산에서 개발하신 
          대 홍 단 감 자 자 동 돌 봄 장 치
          """)
    print("김*은 장군님께 충성하는 마음으로 조국과 로동당을 위하여 열심히 일하자!")
    spk.play_audio(spk.WELCOME)
    init.START = time.time()
    init.CROP = args.crop.lower()
    init.WATERING_INTERVAL = 3600 * args.water
        
    # Create thread objects for each task
    thread1 = threading.Thread(target=env.environment)
    thread2 = threading.Thread(target=man.manual)
    thread3 = threading.Thread(target=man.protect)
    thread4 = threading.Thread(target=spk.environment_warning)
    thread5 = threading.Thread(target=spk.bad_warning)
    thread6 = threading.Thread(target=mtr.water_motor)
    thread7 = threading.Thread(target=mtr.fertilizer_motor)
    thread8 = threading.Thread(target=ir.ir_proxy)
    thread9 = threading.Thread(target=led.lighting)
    thread10 = threading.Thread(target=dis.real_time)
        
    # Start the threads
    print("Ready, go!")
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    
    # Wait for all threads to finish
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()

    print("All tasks are done.")
