import wave,sys

try:
    import pyaudio
    USE_PYAUDIO = True
except ImportError:
    USE_PYAUDIO = False

def playSound(filename):
    if USE_PYAUDIO:
        CHUNK = 1024

        wf = wave.open(filename, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(CHUNK)

        while data != '':
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()

        p.terminate()