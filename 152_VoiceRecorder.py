import sounddevice 
from scipy.io.wavfile import write

def voice_recorder(seconds,file):
    print("Recording Started...")
    recording = sounddevice.rec((seconds * 44100),samplerate = 44100,channels=1)
    sounddevice.wait()
    write(file,44100,recording)
    print("Recording is finished!")

voice_recorder(10,"recordsave.wav")

