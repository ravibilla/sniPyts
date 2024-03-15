# Record voice
#!pip install sounddevice
#!pip install SciPy
import sounddevice
from scipy.io.wavfile import write

def record_voice(seconds, file):
    print("Recording started...")
    recording = sounddevice.rec((seconds * 44100), samplerate = 44100, channels = 1)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording completed!")

record_voice(5, "./files/voice_recording.wav")