from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
import scipy.misc
from skimage import io
img=np.array(Image.open('C:/Users/Administrator/Desktop/lena.bmp'))  #打开图像并转化为数字矩阵

# 初始化参考矩阵
np.set_printoptions(threshold=np.inf)
M = np.zeros((255, 255))

b = 0
z = 0
for x in list(range(0, 255)):
    for y in list(range(0, 255, 8)):

        while z <= 7:
            M[x][y] = int((z+b) % 8)
            y = y+1
            z = z+1
            if y >= 254:
                break
        # print(y)
        # print(z)
        z = 0
    if x % 2 == 1:
        b = b+3
    else:
        b = b+2
# 嵌入秘密信息

# 获取密文长度

sec = input("请输入密文：")
print(sec)
sec1 = list(sec)
sec3 = []
a = 0
b = 0

# 将输入信息编码

for i in range(len(sec1)):
    sec2 = ord(sec1[i])
    sec3.append(sec2)

sec4 = []
i = 0

#将秘密信息转化为int型数组

sec4 = [int(a)for a in sec3]
sec5 = [oct(a)for a in sec3]#转换为八进制
sec6 = []

#去除进制标识

while i < len(sec5):
    a = str(sec5[i])
    print(a)

    b = str(len(a)-2)
    print(b)
    c = [b,a]
    print(c)
    d = ''.join(c)
    print(d)
    sec6.append(d)
    i = i+1


# 将所有数组整合

sec6 = ''.join(sec6)
print(sec6)
sec6 = list(sec6)
print(sec6)
i = len(sec6)-1
while i >= 0:
    if sec6[i] == 'o':
        del sec6[i]
        del sec6[i-1]
        i = i-2
    else:
        i = i-1

# print(sec6)
# sec5=[int(a)for a in sec4]
# sec5=[oct(a)for a in sec5]
# print(sec5)
# print(sec5)
print(sec6)
print("秘钥为：", len(sec6))

i = 0
j = 0
i = int(i)
j = int(j)
sec6 = [int(a)for a in sec6]
a = M.shape
o = int(a[0])
p = int(a[1])
for k in list(sec6):                #读取秘密信息的数字形式
        if i <= o:
            if j > p:
                j = 0
                i = i+1
            x1 = int(img[i][j])                # 获取像素对
            x2 = int(img[i][j+1])
            if x1 >= 2 and x2 >= 2:
                print(i, j)
                print(x1, x2)
                print(k)
                print(M[x1][x2])
                # print(M[x1][x2-1])
                a = int(((x1-1)/2) % 2)
                b = x2 % 2
                c = (x1 - 1) % 2
                print(a, b, c)

                if a < 1 and b == 0 :#在龟壳边的嵌入算法
                    # print(x1,x2)
                    list1 = [M[x1][x2], M[x1][x2+1], M[x1][x2-1], M[x1+1][x2+1],
                           M[x1+1][x2], M[x1+1][x2-1], M[x1-1][x2+1], M[x1-1][x2], M[x1-1][x2-1]]
                    list1 = [int(a)for a in list1]
                    print(list1)
                    m = 0
                    while m <= len(list1)-1:

                        if list1[m] == k:
                            print(m,list1[m],k)
                            if m == 1:
                                x2 = x2+1
                                break
                            if m == 2:
                                x2=x2-1
                                break
                            if m == 3:
                                x1 = x1+1
                                x2 = x2+1
                                break
                            if m == 4:
                                x1 = x1 + 1
                                break
                            if m == 5:
                                x1 = x1+1
                                x2 = x2-1
                                break
                            if m == 6:
                                x1 = x1 - 1
                                x2 = x2 + 1
                                break
                            if m == 7:
                                x1 = x1 - 1
                                break
                            if m == 8:
                                x1 = x1 - 1
                                x2 = x2 - 1
                                break
                        m = m + 1

                if 1 <= a <= 2 and b==1 :#龟边嵌入算法2
                    list1 = [M[x1][x2], M[x1][x2 + 1], M[x1][x2 - 1], M[x1 + 1][x2 + 1],
                         M[x1 + 1][x2], M[x1 + 1][x2 - 1], M[x1 - 1][x2 + 1], M[x1 - 1][x2], M[x1 - 1][x2 - 1]]
                    list1 = [int(a) for a in list1]
                    print(list1)
                    m = 0
                    while m <= len(list1) - 1:

                        if list1[m] == k:
                            print(m,list1[m],k)
                            if m == 1:
                                x2 = x2 + 1
                                break
                            if m == 2:
                                x2 = x2 - 1
                                break
                            if m == 3:
                                x1 = x1 + 1
                                x2 = x2 + 1
                                break
                            if m == 4:
                                x1 = x1 + 1
                                break
                            if m == 5:
                                x1 = x1 + 1
                                x2 = x2 - 1
                                break
                            if m == 6:
                                x1 = x1 - 1
                                x2 = x2 + 1
                                break
                            if m == 7:
                                x1 = x1 - 1
                                break

                            if m == 8:
                                x1 = x1 - 1
                                x2 = x2 - 1
                                break
                        m = m + 1

                if 1 <= a <= 2 and b == 0 and c == 1:#在龟壳背部上一元素嵌入算法
                        # print(a)
                        list1 = [M[x1][x2], M[x1][x2+1], M[x1][x2-1],M[x1+1][x2],
                                 M[x1 - 1][x2 + 1], M[x1 - 1][x2],M[x1 - 1][x2 - 1],M[x1-2][x2]]
                        m = 0
                        while m <= len(list1) - 1:
                            if list1[m] == k:
                                if m == 1:
                                    x2 = x2 + 1
                                if m == 2:
                                    x2 = x2 - 1
                                if m == 3:
                                    x1 = x1 + 1
                                if m == 4:
                                    x1 = x1 - 1
                                    x2 = x2 + 1
                                if m == 5:
                                    x1 = x1 - 1
                                if m == 6:
                                    x1 = x1 - 1
                                    x2 = x2 - 1
                                if m == 7:
                                    x1 = x1-2
                            m = m+1

                if 1 <= a <= 2 and b == 0 and c == 0:   #在龟壳背部下一元素嵌入算法
                    list1 = [M[x1][x2], M[x1][x2+1], M[x1][x2-1], M[x1+1][x2+1],
                           M[x1+1][x2], M[x1+1][x2-1], M[x1+2][x2], M[x1-1][x2]]
                    print(list1)
                    m=0
                    while m <= len(list1) - 1:
                        if list1[m] == k:
                            if m == 1:
                                x2 = x2+1
                            if m == 2:
                                x2 = x2-1
                            if m == 3:
                                x1 = x1+1
                                x2 = x2+1
                            if m == 4:
                                x1 = x1 + 1
                            if m == 5:
                                x1 = x1+1
                                x2 = x2-1
                            if m == 6:
                                x1 = x1+2
                            if m==7:
                                x1 = x1-1
                        m = m+1

                if a < 1 and b == 1 and c == 1:#在龟壳背部上一元素嵌入算法
                    list1 = [M[x1][x2], M[x1][x2 + 1], M[x1][x2 - 1], M[x1 + 1][x2],
                             M[x1 - 1][x2 + 1], M[x1 - 1][x2], M[x1 - 1][x2 - 1], M[x1 - 2][x2]]
                    print(list1)
                    m = 0
                    while m <= len(list1) - 1:
                        if list1[m] == k:
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
                                x1 = x1 - 1
                                x2 = x2 + 1
                                break
                            if m == 5:
                                x1 = x1 - 1
                                break
                            if m == 6:
                                x1 = x1 - 1
                                x2 = x2 - 1
                                break
                            if m == 7:
                                x1 = x1 - 2
                                break
                        m = m+1
                if a < 1 and b == 1 and c == 0:#在龟壳背部下一元素嵌入算法
                    list1 = [M[x1][x2], M[x1][x2+1], M[x1][x2-1], M[x1+1][x2+1],
                           M[x1+1][x2], M[x1+1][x2-1], M[x1+2][x2], M[x1-1][x2],]
                    m=0
                    while m <= len(list1) - 1:
                        if list1[m] == k:
                            if m == 1:
                                x2 = x2+1
                            if m == 2:
                                x2 = x2-1
                            if m == 3:
                                x1 = x1+1
                                x2 = x2+1
                            if m == 4:
                                x1 = x1 + 1
                            if m == 5:
                                x1 = x1+1
                                x2 = x2-1
                            if m == 6:
                                x1 = x1+2
                            if m == 7:
                                x1 = x1-1
                        m = m+1
                print(x1, x2)
                img[i][j] = int(x1)
                img[i][j+1] = int(x2)
             #  print(img[i][j],img[i][j+1])
                f = int(img[i][j])
                g = int(img[i][j+1])
                print(int(M[f][g]))
                j = j + 2
        else:

            b = str(o*p/2*3)
            print("已达到嵌入容量，共计嵌入"+b+"bit字符")
# a = []
# j = 0
# for j in range(0,124,2):
#     print(j)
#     u=img[0][j]
#     v=img[0][j+1]
#     print(u,v)
#     a.append(M[u][v])
print(a)
print("秘钥为：", len(sec6))
img = Image.fromarray(img)
# # img.show()
io.imsave("D:/123/infhided.bmp", img)
# # scipy.misc.imsave("D:/123/infhided.bmp", img)








# plt.imshow(img)
#
# plt.show()



