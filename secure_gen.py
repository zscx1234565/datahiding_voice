import pynamical
import random
from pynamical import simulate, bifurcation_plot, save_fig
import pandas as pd, numpy as np, IPython.display as display, matplotlib.pyplot as plt, matplotlib.cm as cm
from scipy.special import comb, perm
import math
# np.set_printoptions(threshold = 1e6)

def lm_inhi(ini_value,rate,num):
    pops = np.zeros((num))
    pops[0]=ini_value
    for i in range(0,num-1):
        pops[i+1] =pynamical.pynamical.logistic_map(pops[i], rate)

    return pops
def sec_gen(ini_valu,rate):


    pops0=lm_inhi(0.6321712366185492,3.921497865843587,20000)
    pops=pops0[999:19999]
    key_seq=[int((a*10000)%9) for a in pops]
    ini_seq=[20, 20, 20, 20, 20, 20, 20, 20, 20]
    count=8
    for ini_num in range(0,10000):
        if key_seq[ini_num] not in ini_seq:
            ini_seq[count]=key_seq[ini_num]
            count = count-1
        if count < 0:
            break
    ini_seq = list(np.array(ini_seq).reshape(3, 3))
    # print(ini_seq)
#
    m = np.zeros((3, 253))
    ini_seq=np.hstack((ini_seq, m))

    num = 0

    for i in range(0,1500):
        if num >= 253:
            break

        a = int(num % 3)
        b = num + 3


        if int(key_seq[num+10000] % 6) == 0:
            ini_seq[0, b] = int(ini_seq[0, a])
            ini_seq[1, b] = int(ini_seq[1, a])
            ini_seq[2, b] = int(ini_seq[2, a])
            num = num + 1
            continue
        if int(key_seq[num+10000] % 6) == 1:
            ini_seq[0, b] = int(ini_seq[0, a])
            ini_seq[2, b] = int(ini_seq[1, a])
            ini_seq[1, b] = int(ini_seq[2, a])
            num = num + 1
            continue
        if int(key_seq[num+10000] % 6) == 2:
            ini_seq[1, b] = int(ini_seq[0, a])
            ini_seq[0, b] = int(ini_seq[1, a])
            ini_seq[2, b] = int(ini_seq[2, a])
            num = num + 1
            continue
        if int(key_seq[num+10000] % 6) == 3:
            ini_seq[1, b] = int(ini_seq[0, a])
            ini_seq[2, b] = int(ini_seq[1, a])
            ini_seq[0, b] = int(ini_seq[2, a])
            num = num + 1
            continue
        if int(key_seq[num+10000] % 6) == 4:
            ini_seq[2, b] = int(ini_seq[0, a])
            ini_seq[0, b] = int(ini_seq[1, a])
            ini_seq[1, b] = int(ini_seq[2, a])
            num = num + 1
            continue
        if int(key_seq[num+10000] % 6) == 5:
            ini_seq[2, b] = int(ini_seq[0, a])
            ini_seq[1, b] = int(ini_seq[1, a])
            ini_seq[0, b] = int(ini_seq[2, a])
            num = num+1
            continue
    M=np.zeros((258,256))
    for i in range(0,86):
       M [i*3:i*3+3,:]=ini_seq
    # print(M)
    return M


def sec_genb(ini_valu):

    pops0 = lm_inhi(0.6321712366185492, 3.921497865843587, 20000)
    pops = pops0[999:19999]
    key_seq = [int((a*10000) % 16) for a in pops]
    w = np.ones((1, 16))
    ini_seq = 20 * w
    count = 15
    for ini_num in range(0,10000):
        if key_seq[ini_num] not in ini_seq:
            ini_seq[0, count] = key_seq[ini_num]
            count = count-1
        if count < 0:
            break
    ini_seq = list(ini_seq.reshape(4, 4))
    # print(ini_seq)
#
    m = np.zeros((4, 252))
    ini_seq = np.hstack((ini_seq, m))
    # print(ini_seq)
    num = 0
    j = [int((c * 10000) % 24) for c in pops]
    num = 0
    peu = np.zeros((24, 4))
    for x in range(0, 4):
        for y in range(0, 4):
            if y == x:
                continue
            for z in range(0, 4):
                if z == x or z == y:
                    continue
                for u in range(0, 4):
                    if u == x or u == y or u == z:
                        continue
                    peu[num, :] = [x, y, z, u]
                    num = num+1
    for num in range(0, 252):
            i = j[num]
            a = int(num % 4)
            b = num + 4
            ini_seq[int(peu[i, 0]), b] = ini_seq[0, a]
            ini_seq[int(peu[i, 1]), b] = ini_seq[1, a]
            ini_seq[int(peu[i, 2]), b] = ini_seq[2, a]
            ini_seq[int(peu[i, 3]), b] = ini_seq[3, a]

    M = np.zeros((256, 256))
    for i in range(0, 64):
        if i*4+4 > 256:
            break
        M[i*4:i*4+4, :] = ini_seq
    return M

