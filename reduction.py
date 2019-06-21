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
# from skimage import io
import test

def reduct(file):
    img = Image.open(file)
    img1 = np.array(img)
    img =Image.open("D:/123/TEST/ypinfhided.tif")
    img2 = np.array(img)
    # print(1)
    img3=img2-img1
    # print(2)

    # print(img1)
    # print(img2)
    # print(img3)
    # print('count(0)=', np.sum(img3 == 0))
    # print('count(1)=', np.sum(img3 == 1))
    # print('count(255)=', np.sum(img3 == 255))
    Image.fromarray(img3).save("C:/Users/Administrator/Desktop/论文/标准图像/10.tif")
    File="C:/Users/Administrator/Desktop/论文/标准图像/10.tif"
    return File