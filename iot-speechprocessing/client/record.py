import sounddevice
from scipy.io.wavfile import write
import warnings
import json 
import numpy as np

SECONDS = 10

CONFIG_FILE_NAME = "config.json"

try:
    SECONDS = int(json.load(open(CONFIG_FILE_NAME, "r"))["max_rec_time"])
except OSError:
    pass

def start_recording():
    fs=44100
    print("recording . . .")
    warnings.filterwarnings("ignore")
    try:
        rec_speech = sounddevice.rec(int(SECONDS * fs), samplerate=fs, channels = 2, dtype=np.int16)
        sounddevice.wait()
        print("done recording")
        write("outputFile.wav", fs, rec_speech)
        return rec_speech
    except OSError:
        print("Could not record!")
        print("Pls check your input device and restart!")
    except KeyboardInterrupt:
        print("Aufnahme abgebrochen")

