import reduction
import new_inhi
import os
import sys
import fnmatch
from PIL import Image
import numpy as np
import test
import pandas as pd

org_path = "E:\BOSSBASE"
target_path = "E:\Paper_test"
psnr= np.zeros((1,10000))

def main():
        count = 0

        for root, dirs, files in os.walk(org_path):

            for _file in files:

                file1 = os.path.join(target_path, str(count) + ".pgm")
                file2 = os.path.join(org_path, _file)

                # img1 = Image.open(file1)
                # img1 = np.array(img1)
                # img2 = Image.open(file2)
                # img2 = np.array(img2)
                #
                # img3 = img2 - img1
                psnr[0, count] = round(test.show_d_psnr(file1, file2), 2)
                # file3 = os.path.join(target_path,'1', str(count)+'.pgm')
                count = count + 1

                # Image.fromarray(img3).save(file3)
                if count == 10000:
                    break
        file4 = os.path.join(target_path,"PSNR",'data.csv')
        data = pd.DataFrame(psnr)
        data.to_csv(file4)
if __name__ == '__main__':
    main()