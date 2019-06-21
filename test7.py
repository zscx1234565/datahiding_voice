import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# def pha(File,File1):
# File="D:/123/TEST/new_pinfhided.tif"
File="D:/123/TEST/ypinfhided.tif"
File1="C:/Users/Administrator/Desktop/论文/标准图像/NEW/lena.tif"
a = [0]*256
b = [0]*256
x = np.arange(0,256)
xt = [25,50,75,100,125,150,175,200,225,255]
print(xt)
img = np.array(Image.open(File))
img1 = np.array(Image.open(File1))
# im = [True, False, True, True, True, False]
# print(img == 156,np.sum(img == 156))
for i in range(0,256):
        a[i] = int(np.sum(img == i))
        b[i] = int(np.sum(img1 == i))

plt.plot(x, a, c='red', marker='^')
plt.plot(x, b, c='blue')
plt.xticks(xt)
plt.xticks()
plt.xlabel('pixel value')
plt.ylabel('count')
plt.title('lena')
plt.show()
