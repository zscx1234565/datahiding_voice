from tkinter import *
import luyin
import wave_inhi
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
import secure_gen
import time
from skimage import io,transform,color
def ypyincang(File):
    start = time.clock()
    # img=io.imread(File)
    # img=color.rgb2gray(img)
    img = np.array(Image.open(File))  # 打开图像并转化为数字矩阵

    ini_valu = random.uniform(0, 1)
    rate = random.uniform(3.6, 4)
    # print("秘钥为：", ini_valu, rate)
    M = secure_gen.sec_gen(ini_valu, rate)
    # print(shape(M))
    # 嵌入秘密信息

    # 录音编码为十进制数
    wf = wave.open(r'D:/2323/output.wav', 'rb')
    FORMAT = pyaudio.paInt16
    p = pyaudio.PyAudio()
    params = wf.getparams()
    nchannels,sampwidth,framerate,nframes = params[:4]
    # print(nchannels, sampwidth, framerate, nframes)
    seq = list(params[:4])

    data = wf.readframes(nframes)
    # print(data)
    # print(data)

    a1 = list(data)

    # print(a1)
    # print("数据元素的个数为："+str(len(a1)))

    a2=seq+a1
    # print("a1的长度为："+str(len(a1)))
    # print("转为十进制的数为：")
    # print( len(a1))
    # print(a2)
    i = 0
    j = 0
    i = int(i)
    sec1=[]
    # print(a1)
    sec=[oct(a) for a in a2]
    # 去除进制标识
    a=0
    while i < len(sec):
        a = sec[i]
        # print(a)

        b = len(a) - 2
        # print(b)

        c = [b, str(a[2:])]
        # print(c)
        c=[str(d)for d in c]
        d = ''.join(c)
        # print(d)
        sec1.append(d)
        i = i + 1

    sec2 = ''.join(sec1)
    # print(sec2)
    # print(len(sec1))
    sec3 = list(sec2)

    # print("嵌入的秘密信息为：")
    # print(sec3)

    a = img.shape
    o = int(a[0])
    p = int(a[1])
    # print('sec3='+str(len(sec3)))
    # print(sec3)
    i = 0
    j = 0
    z = 0
    # print(o,p)
    # print(img[i][j])
    # print(sec3)
    # print(M[255][255])
    q=int(o*p/2)

    sec3=sec3[:q]

    for k in sec3:  # 读取秘密信息的数字形式
        z = z+1

        if i <= o-1:
            if j > p-1:
                j = 0
                i = i + 1
            if i > o-1:
                d = str(o * p * 1.5)
                # tkinter.messagebox.showinfo('', '已达到最大嵌入容量'+str(z)+'!')
                break
            # print(z,k)


            x1 = int(img[i][j])  # 获取像素对
            x2 = int(img[i][j + 1])

            if x1 == 0 and x2 == 0 :#写的有点复杂回头修改一下
                list1 = [M[x1][x2], M[x1][x2 + 1],M[x1][x2+2], M[x1 + 1][x2], M[x1 + 1][x2 + 1],
                          M[x1 + 1][x2 + 2], M[x1 + 2][x2], M[x1 + 2][x2 + 1],  M[x1 + 2][x2 + 2]]
                list1 = [int(a) for a in list1]
                m = 0
                while m <= len(list1) - 1:
                    if int(list1[m]) == int(k):
                        # print(m, list1[m], k)
                        if m == 1:
                            x2 = x2 + 1
                            break
                        if m == 2:
                            x2 = x2 + 2
                            break
                        if m == 3:
                            x1 = x1 + 1
                            break
                        if m == 4:
                            x1 = x1 + 1
                            x2 = x2 + 1
                            break
                        if m == 5:
                            x1 = x1 + 1
                            x2 = x2 + 2
                            break
                        if m == 6:
                            x1 = x1 + 2
                            x2 = x2
                            break
                        if m == 7:
                            x1 = x1 + 2
                            x2 = x2 + 1
                            break
                        if m == 8:
                            x1 = x1 + 2
                            x2 = x2 + 2
                            break

                    m = m + 1
                j=j+2
                continue
            if x1 == 0 and 0 < x2 < 255:
                list1 = [M[x1][x2], M[x1][x2 + 1],M[x1][x2 - 1],M[x1 +1][x2],  M[x1 + 1][x2 + 1],
                         M[x1 + 1][x2 - 1], M[x1 + 2][x2], M[x1 + 2][x2 + 1], M[x1 + 2][x2 - 1]]

                list1 = [int(a) for a in list1]
                m = 0
                while m <= len(list1) - 1:

                    if int(list1[m]) == int(k):
                        # print(m, list1[m], k)
                        if m == 1:
                            x2 = x2 + 1
                            break
                        if m == 2:
                            x2 = x2 - 1
                            break
                        if m == 3:
                            x1 = x1 + 1
                            break
                        if m == 4:
                            x1 = x1 + 1
                            x2 = x2 + 1
                            break
                        if m == 5:
                            x1 = x1 + 1
                            x2 = x2 - 1
                            break
                        if m == 6:
                            x1 = x1 + 2

                            break
                        if m == 7:
                            x1 = x1 + 2
                            x2 = x2 + 1
                            break
                        if m == 8:
                            x1 = x1 + 2
                            x2 = x2 - 1
                            break
                    m = m + 1
                j=j+2
                continue
            if x1 == 0 and x2 == 255:
                list1 = [M[x1][x2], M[x1][x2 - 1],M[x1][x2 - 2], M[x1 + 1][x2], M[x1 + 1][x2 - 1],
                         M[x1 + 1][x2 - 2], M[x1 + 2][x2], M[x1 + 2][x2 - 1], M[x1 + 2][x2 - 2]]

                list1 = [int(a) for a in list1]
                m = 0
                while m <= len(list1) - 1:

                    if int(list1[m]) == int(k):
                        # print(m, list1[m], k)
                        if m == 1:
                            x2 = x2 - 1
                            break
                        if m == 2:
                            x2 = x2 - 2
                            break
                        if m == 3:
                            x1 = x1 + 1
                            break
                        if m == 4:
                            x1 = x1 + 1
                            x2 = x2 - 1
                            break
                        if m == 5:
                            x1 = x1 + 1
                            x2 = x2 - 2
                            break
                        if m == 6:
                            x1 = x1 + 2
                            x2 = x2
                            break
                        if m == 7:
                            x1 = x1 + 2
                            x2 = x2 - 1
                            break
                        if m == 8:
                            x1 = x1 + 2
                            x2 = x2 - 2
                            break
                    m = m + 1
                j=j+2
            if x1 == 255 and 0 < x2 < 255:
                list1 = [M[x1][x2], M[x1][x2 - 1],M[x1][x2 + 1], M[x1 - 1][x2], M[x1 - 1][x2 + 1],
                         M[x1 - 1][x2 - 1],M[x1 - 2][x2], M[x1 - 2][x2 - 1], M[x1 - 2][x2 + 1]]

                list1 = [int(a) for a in list1]
                m = 0
                while m <= len(list1) - 1:

                    if int(list1[m]) == int(k):
                        # print(m, list1[m], k)
                        if m == 1:
                            x2 = x2 - 1
                            break
                        if m == 2:
                            x2 = x2 + 1
                            break
                        if m == 3:
                            x1 = x1 - 1
                            break
                        if m == 4:
                            x1 = x1 - 1
                            x2 = x2 + 1
                            break
                        if m == 5:
                            x1 = x1 - 1
                            x2 = x2 - 1
                            break
                        if m == 6:
                            x1 = x1 - 2
                            break
                        if m == 7:
                            x1 = x1 - 2
                            x2 = x2 - 1
                            break
                        if m == 8:
                            x1 = x1 - 2
                            x2 = x2 + 1
                            break
                    m = m + 1
                j=j+2
                continue
            if x1 == 255 and x2 == 255:
                list1 = [M[x1][x2], M[x1][x2 - 1],M[x1][x2 - 2], M[x1 - 1][x2], M[x1 - 1][x2 - 1],
                         M[x1 - 1][x2 - 2], M[x1 - 2][x2], M[x1 - 2][x2 - 1], M[x1 - 2][x2 - 2]]

                list1 = [int(a) for a in list1]
                m = 0
                while m <= len(list1) - 1:

                    if int(list1[m]) == int(k):
                        # print(m, list1[m], k)
                        if m == 1:
                            x2 = x2 - 1
                            break
                        if m == 2:
                            x2 = x2 - 2
                            break
                        if m == 3:
                            x1 = x1 - 1
                            break
                        if m == 4:
                            x1 = x1 - 1
                            x2 = x2 - 1
                            break
                        if m == 5:
                            x1 = x1 - 1
                            x2 = x2 - 2
                            break
                        if m == 6:
                            x1 = x1 - 2
                            x2 = x2
                            break
                        if m == 7:
                            x1 = x1 - 2
                            x2 = x2 - 1
                            break
                        if m == 8:
                            x1 = x1 - 2
                            x2 = x2 - 2
                            break
                    m = m + 1
                j=j+2
                continue
            if 0 < x1 < 255 and x2 == 255:
                list1 = [M[x1][x2], M[x1][x2 - 1], M[x1][x2 - 2], M[x1 - 1][x2], M[x1 - 1][x2 - 1],
                         M[x1 - 1][x2 - 2], M[x1 + 1][x2], M[x1 + 1][x2 - 1],M[x1 + 1][x2 - 2]]

                list1 = [int(a) for a in list1]
                m = 0
                while m <= len(list1) - 1:

                    if int(list1[m]) == int(k):
                        # print(m, list1[m], k)
                        if m == 1:
                            x2 = x2 - 1
                            break
                        if m == 2:
                            x2 = x2 - 2
                            break
                        if m == 3:
                            x1 = x1 - 1
                            break
                        if m == 4:
                            x1 = x1 - 1
                            x2 = x2 - 1
                            break
                        if m == 5:
                            x1 = x1 - 1
                            x2 = x2 - 2
                            break
                        if m == 6:
                            x1 = x1 + 1

                            break
                        if m == 7:
                            x1 = x1 + 1
                            x2 = x2 - 1
                            break
                        if m == 8:
                            x1 = x1 + 1
                            x2 = x2 - 2
                            break
                    m = m + 1
                j=j+2
                continue
            if x1 == 255 and x2 == 0:
                list1 = [M[x1][x2], M[x1][x2 + 1],M[x1][x2 + 2], M[x1 - 1][x2], M[x1 - 1][x2 + 1],
                         M[x1 - 1][x2 + 2], M[x1 - 2][x2], M[x1 - 2][x2 + 1], M[x1 - 2][x2 + 2]]

                list1 = [int(a) for a in list1]
                m = 0
                while m <= len(list1) - 1:

                    if int(list1[m]) == int(k):
                        # print(m, list1[m], k)
                        if m == 1:
                            x2 = x2 + 1
                            break
                        if m == 2:
                            x2 = x2 + 2
                            break
                        if m == 3:
                            x1 = x1 - 1
                            break
                        if m == 4:
                            x1 = x1 - 1
                            x2 = x2 + 1
                            break
                        if m == 5:
                            x1 = x1 - 1
                            x2 = x2 + 2
                            break
                        if m == 6:
                            x1 = x1 - 2
                            x2 = x2
                            break
                        if m == 7:
                            x1 = x1 - 2
                            x2 = x2 + 1
                            break
                        if m == 8:
                            x1 = x1 - 2
                            x2 = x2 + 2
                            break
                    m = m + 1
                j=j+2
                continue
            if 0 < x1 < 255 and x2 == 0:
                list1 = [M[x1][x2], M[x1][x2 + 1],M[x1][x2 + 2],  M[x1 - 1][x2], M[x1 - 1][x2 + 1],
                         M[x1 - 1][x2 + 2], M[x1 + 1][x2], M[x1 + 1][x2 + 1], M[x1 + 1][x2 + 2]]

                list1 = [int(a) for a in list1]
                m = 0
                while m <= len(list1) - 1:

                    if int(list1[m]) == int(k):
                        # print(m, list1[m], k)
                        if m == 1:
                            x2 = x2 + 1
                            break
                        if m == 2:
                            x2 = x2 + 2
                            break
                        if m == 3:
                            x1 = x1 - 1
                            break
                        if m == 4:
                            x1 = x1 - 1
                            x2 = x2 + 1
                            break
                        if m == 5:
                            x1 = x1 - 1
                            x2 = x2 + 2
                            break
                        if m == 6:
                            x1 = x1 + 1
                            break
                        if m == 7:
                            x1 = x1 + 1
                            x2 = x2 + 1
                            break
                        if m == 8:
                            x1 = x1 + 1
                            x2 = x2 + 2
                            break
                    m = m + 1
                j = j + 2
                continue
            if 0 < x1 < 255 and 0 < x2 < 255:
                list1 = [M[x1][x2], M[x1][x2 + 1], M[x1][x2 - 1], M[x1 + 1][x2],
                         M[x1 + 1][x2 + 1], M[x1 + 1][x2 - 1], M[x1 - 1][x2], M[x1 - 1][x2 + 1], M[x1 - 1][x2 - 1]]
                list1 = [int(a) for a in list1]
                m = 0
                while m <= (len(list1) - 1):

                    if int(list1[m]) == int(k):
                        # print(m, list1[m], k)
                        if m == 1:
                            x2 = x2 + 1
                            break
                        if m == 2:
                            x2 = x2 - 1
                            break
                        if m == 3:
                            x1 = x1 + 1
                            break
                        if m == 4:
                            x1 = x1 + 1
                            x2 = x2 + 1
                            break
                        if m == 5:
                            x1 = x1 + 1
                            x2 = x2 - 1
                            break
                        if m == 6:
                            x1 = x1 - 1
                            break
                        if m == 7:
                            x1 = x1 - 1
                            x2 = x2 + 1
                            break
                        if m == 8:
                            x1 = x1 - 1
                            x2 = x2 - 1
                            break
                    m = m + 1
                # if z<=30:
                # print(x1, x2)
            img[i][j] = int(x1)
            img[i][j + 1] = int(x2)
                # print(img[i][j],img[i][j+1])
            f = int(img[i][j])
            g = int(img[i][j + 1])
                # if z <= 30:
                # print(int(M[f][g]))
            j = j + 2
            if int(k) != int(M[x1][x2]):
                print("Error:"+str(z),k,M[f][g],f,g)

        else:
            d = str(o * p * 1.5)
            # tkinter.messagebox.showinfo('', '已达到最大嵌入容量' + str(z) + '个八进制数' + '!')
            break
    # a = []
    # j = 0
    # for j in range(0,124,2):
    #     print(j)
    #     u=img[0][j]
    #     v=img[0][j+1]
    #     print(u,v)
    #     a.append(M[u][v])
    # print(a)

    # print('', '总秘密长度为：'+ str(len(sec3)))
    # print('', '实际嵌入长度为：' + str(z-1)+'个八进制数')
    # os.remove("D:/123/TEST/ypinfhided.tif")
    Image.fromarray(img).save("D:/123/TEST/ypinfhided.tif")
    # # img.show()
    File2 ="D:/123/TEST/ypinfhided.tif"
    # io.imsave("D:/123/TEST/ypinfhided.tif", img)
    # # scipy.misc.imsave("D:/123/infhided.bmp", img)
    end = time.clock()
    # print('Running time: %s Seconds' % (end - start))
    return File2
