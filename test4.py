from tkinter import *
import luyin
import wave_inhi
import struct
import io
from tkinter import filedialog
from PIL import Image, ImageTk
import os.path
import tkinter.simpledialog
import pyaudio
import wave
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
import scipy.misc
from skimage import io



wf = wave.open(r'C:/Users/Administrator/PycharmProjects/inhi/Speech Sleep.wav', 'rb')
params = wf.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
data = wf.readframes(nframes)

# print(type(data))
p1=list(data)
print(p1)
p2=[struct.pack('B',a)for a in p1]
# print(p2)
p3=b''.join(p2)
print(p3)
if p3 == data:
    print("GREAT!")
else:
    print("NO!")
f = wave.open("dd.wav", "wb")
f.setnchannels(nchannels)
f.setsampwidth(sampwidth)
f.setframerate(framerate)
f.writeframes(p3)
f.close()