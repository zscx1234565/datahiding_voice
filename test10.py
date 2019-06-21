
import secure_gen
import random
import numpy as np
import os
import os.path
import re
import sys
import test
import new_inhi
import matplotlib.pyplot as plt

##读取文件夹内所有文件并进行数据隐藏并绘制散点图
path=r'F:/UCIDimage1'
files = os.listdir(path)
y=[]
i=0
for file in files:
    i=i+1
    img_path = 'F:/UCIDimage/' + file
    new_inhi.ypyincang(img_path)
    try:
        y.append(str(round(test.show_psnr(img_path), 2)))
    except:
        1
    print(y)
# np.save('D:/123/TEST/y.npy',y)
y=np.load('D:/123/TEST/y.npy')
x_values=range(1,887)
y_values=y
plt.scatter(x_values, y_values)
# plt.xlabel('Image ID', fontsize=14)
# plt.ylabel('PSNR(dB)', fontsize=14)
plt.show()
