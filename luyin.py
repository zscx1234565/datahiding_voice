
import tkinter.simpledialog
import pyaudio
import wave
from numpy import *
from tkinter import filedialog



def luyin1(Time):

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 2000

    if Time =='':
        RECORD_SECONDS=20
    else:
        RECORD_SECONDS=int(Time)+10
    # WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    tkinter.messagebox.showinfo('', '开始录音')

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open("D:/2323/output.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    print(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    tkinter.messagebox.showinfo('', '录音完成')

#听取录音
def Listenluyin(File):
    # 定义数据流块
    CHUNK = 1024

    # 只读方式打开wav文件
    # File=filedialog.askopenfilename(initialdir="C:/Users/Administrator/PycharmProjects/inhi", title='选择音频')
    wf = wave.open(File, 'rb')  # (sys.argv[1], 'rb')

    p = pyaudio.PyAudio()

    # 打开数据流
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # 读取数据
    data = wf.readframes(CHUNK)

    # 播放
    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    # 停止数据流
    stream.stop_stream()
    stream.close()

    # 关闭 PyAudio
    p.terminate()
