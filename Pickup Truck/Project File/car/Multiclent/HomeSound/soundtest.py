import numpy as np
import sounddevice as sd

duration = 10 #in seconds
volume = None
def audio_callback(indata, frames, time, status):
   global  volume
   volume_norm = np.linalg.norm(indata) * 10
   volume = volume_norm


def sound():
  global  volume
  stream = sd.InputStream(callback=audio_callback)
  with stream:
    sd.sleep(duration * 5)
  return volume

