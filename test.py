
import numpy
from PIL import Image
import fractions
from skimage import io
from skimage import io,transform,color

def psnr(im1,im2):
    diff = numpy.abs(im1 - im2)
    m = im1.shape
    m=[int(a)for a in m]
    rmse = numpy.sqrt(numpy.square(diff).sum()/(m[0]*m[1]))
    # print(fractions.Fraction(rmse))
    if rmse != 0:
        psnr = 20*numpy.log10((255/rmse))
        return psnr
    else:
        return 0
def show_psnr(File):
    x = numpy.array(Image.open('D:/123/TEST/ypinfhided.tif'))
    # img = io.imread(File)
    # img = color.rgb2gray(img)
    z = numpy.array(Image.open(File))

    psnr1 = psnr(x,z)

    img1 = Image.fromarray(x)

# img1.show()
# img2.show()
    return psnr1

def show_d_psnr(File1, File2):
    x = numpy.array(Image.open(File1))
    # img = io.imread(File)
    # img = color.rgb2gray(img)
    z = numpy.array(Image.open(File2))

    psnr1 = psnr(x,z)

    img1 = Image.fromarray(x)

    return psnr1