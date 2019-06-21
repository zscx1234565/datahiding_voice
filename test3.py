import wave
import pyaudio
import numpy as np
import scipy.signal as signal

framerate = 44100
time = 10

# 产生10秒44.1kHz的100Hz - 1kHz的频率扫描波
wf = wave.open(r'C:/Users/Administrator/PycharmProjects/inhi/output.wav', 'rb')
FORMAT = pyaudio.paInt16
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
# print(wf.getparams())
CHUNK = 1024

data = wf.readframes(CHUNK)

# 打开WAV文档
f = wave.open(r"C:\Users\Administrator\PycharmProjects\inhi\解密音频.wav", "wb")

# 配置声道数、量化位数和取样频率
f.setnchannels(2)
f.setsampwidth(2)
f.setframerate(framerate)
# 将wav_data转换为二进制数据写入文件

f.writeframes(data)
f.close()