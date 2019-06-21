from PIL import Image
from tkinter import *
import luyin
import decode_wave
import wave_inhi
import io
from tkinter import filedialog
from PIL import ImageTk

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
import test

np.set_printoptions(threshold=np.inf)
img = Image.open("C:/Users/Administrator/Desktop/标准图像/NEW/Baboon.tif")
img1 = np.array(img)
img =Image.open("D:/123/TEST/ypinfhided.tif")
img2 = np.array(img)
    # print(1)
img3=(img2-img1)
    # print(2)
o=img3.shape
p=int(o[0])
q=int(o[1])
a=0
b=0
print(img3)
    # print(3)
Image.fromarray(img3).save("C:/Users/Administrator/Desktop/标准图像/3.tif")
File="C:/Users/Administrator/Desktop/标准图像/3.tif"
