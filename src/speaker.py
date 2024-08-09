from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
import time
import src.environment as env
import src.ir as ir
import src.manual as man
# depends on pydub (pip install pydub), ffmpeg (brew install ffmpeg) ,
# and simpleaudio (pip install simpleaudio) [[and pyaudio (pip install pyaudio) ERROR]]

WELCOME = AudioSegment.from_mp3('assets/welcome.mp3')
WILD = AudioSegment.from_mp3('assets/warning.mp3')
HOT = AudioSegment.from_mp3('assets/HOT.mp3')
COLD = AudioSegment.from_mp3('assets/COLD.mp3')
HUMID = AudioSegment.from_mp3('assets/HUMID.mp3')
DRY = AudioSegment.from_mp3('assets/DRY.mp3')

def play_audio(audio, duration=None):
    """
    Play an audio at a certain duration with the computer's default speaker.

    Args:
        audio (AudioSegment object): Parsed mp3 sound file
        duration (int): duration of warning sound playback, 
                        defaulted to None to play the whole audio
    """
    playback = _play_with_simpleaudio(audio)
    if not duration:
        duration = len(audio)/1000.0
    time.sleep(duration)
    playback.stop()
    
def environment_warning():
    """
    Play the appropriate warning message if 
    the temperature or humidity is outside the optimal range.
    """
    while True:
            
        if env.TEMPERATURE < env.TEMPERATURE_LOW:
            print("WARNING: The environment is too cold!")
            play_audio(COLD)
            
        elif env.TEMPERATURE > env.TEMPERATURE_HIGH:
            print("WARNING: The environment is too hot!")
            play_audio(HOT)
            
        if env.HUMIDITY < env.HUMIDITY_LOW:
            print("WARNING: The environment is too dry!")
            play_audio(DRY)
            
        elif env.HUMIDITY > env.HUMIDITY_HIGH:
            print("WARNING: The environment is too humid!")
            play_audio(HUMID)
            
def bad_warning():
    """
    Play the propaganda song if there is any wild animal or bad neighbors
    when the protection mode is on.
    """
    while True:
        
        if man.PROTECTION:
            
            if ir.IR_FRONT > ir.IR_THRESHOLD:
                print("WARNING: Wild animal or bad neighbor approaching the front!")
                play_audio(WILD)
                
            if ir.IR_LEFT > ir.IR_THRESHOLD:
                print("WARNING: Wild animal or bad neighbor approaching the left!")
                play_audio(WILD)
                
            if ir.IR_RIGHT > ir.IR_THRESHOLD:
                print("WARNING: Wild animal or bad neighbor approaching the right!")
                play_audio(WILD)