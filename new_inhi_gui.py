from PIL import Image
from tkinter import *
import luyin
import decode_wave
import wave_inhi
import decode_new
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
import reduction
import new_inhi
root = Tk()

paras = 300

frame = Frame(root, bd=2, relief=SUNKEN)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
canvasname1 = Label(frame, text='原始图像', bd=2, width=25, height=2)
canvasname1.grid(row=0, column=0, sticky=N+S+E+W)

canvasname2 = Label(frame, text='输出图像', width=25, height=2 ,bd=2)
canvasname2.grid(row=0, column=1, sticky=N+S+E+W)

canvasname3 = Label(frame, text='差分图像', width=25, height=2 ,bd=2)
canvasname3.grid(row=0, column=2, sticky=N+S+E+W)

canvas = Canvas(frame, bd=0, width=300, height=300)
canvas.grid(row=1, column=0, sticky=N + S + E + W)

canvas2 = Canvas(frame, bd=0, width=300, height=300)
canvas2.grid(row=1, column=1, sticky=N+S+E+W)

canvas3 = Canvas(frame, bd=0, width=300, height=300)
canvas3.grid(row=1, column=2, sticky=N+S+E+W)
frame.pack(fill=BOTH,expand=1)

# canvasly = Canvas(root,bd=3, width=600, height=200)
# canvasly.pack()
PSNR=''
text = StringVar()
Label(root, textvariable=text).pack()
# text="音频隐藏后图像的PSNR值为："+str(PSNR)
def printcoords1():
    File = filedialog.askopenfilename(parent=root, initialdir="C:/Users/Administrator/Desktop/标准图像/NEW", title='选择图像')
    img1 = Image.open(File)
    Img1 = img1.resize((paras, paras))
    filename = ImageTk.PhotoImage(Img1)
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0, 0, anchor='nw', image=filename)

    File2=new_inhi.ypyincang(File)

    img2=Image.open(File2)
    Img2=img2.resize((paras, paras))
    filename2 = ImageTk.PhotoImage(Img2)
    canvas2.image = filename2
    canvas2.create_image(0, 0, anchor='nw', image=filename2)

    File3=reduction.reduct(File)
    img3 = Image.open(File3)

    Img3 = img3.resize((paras, paras))

    filename3 = ImageTk.PhotoImage(Img3)
    canvas3.image = filename3
    canvas3.create_image(0, 0, anchor='nw', image=filename3)

    # canvasly.fig.add_subplot(221)
    # t = np.arange(0.0, 3.0, 0.01)
    # s = np.sin(2 * np.pi * t)
    # canvasly.axes.plot(t, s)

    o1 = os.path.getsize(File)
    origin_img=str(int(o1 / 1024)) + 'KB'

    o2 = os.path.getsize(File2)
    inhi_img = str(int(o2 / 1024)) + 'KB'

    ly_size1 = os.path.getsize("D:/2323/output.wav")
    ly_size2 = str(int(ly_size1 / 1024)) + 'KB'

    PSNR = "录制音频的大小为："+ly_size2+'\n'+"音频隐藏后图像的PSNR值为：" + \
           str(round(test.show_psnr(File), 2))+'\n'+"原始图像大小为："\
           +origin_img+'\n'+"输出图像大小为："+inhi_img
    text.set(PSNR)

    # test7.pha(File, File2)#绘制像素柱状分析折线图
    # os.remove("D:/2323/output.wav")

def printcoords2():
    File = filedialog.askopenfilename(parent=root, initialdir="D:/123/TEST", title='选择图像')
    # filename = ImageTk.PhotoImage(Image.open(File))
    # canvas.image = filename  # <--- keep reference of your image
    # canvas.create_image(0, 0, anchor='nw', image=filename)

    decode_new.dec_new(File)
    luyin.Listenluyin("D:/123/TEST/decode1.wav")
#创建录音文本框
# labellyTime = Label(root, text='录音时间:',width=10).pack()

# varlyTime = tkinter.StringVar(root, value='')

#创建参数信息文本框

def luyin2():
    luyin.luyin1(10)
    ly_size1 = os.path.getsize("D:/2323/output.wav")
    ly_size2 = str(int(ly_size1 / 1024)) + 'KB'

    text.set("录制音频的大小为："+ly_size2)
def luyin1():
    luyin.Listenluyin("D:/2323/output.wav")

# Entry(root,width=40,textvariable=varlyTime).pack()

# 创建按钮组件，同时设置按钮事件处理函数
Button(root, text='录制音频', width=25,command=luyin2).pack()
Button(root, text='音频播放', width=25,command=luyin1).pack()
Button(root, text='选择图像进行隐藏',width=25, command=printcoords1).pack()
# Button(root, text='输出图片云服务器存储',width=25).pack()
# Button(root, text='从云服务器下载图片',width=25).pack()
Button(root, text='提取音频信息并播放', width=25,command=printcoords2).pack()


#启动消息循环
root.mainloop()
