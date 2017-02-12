# coding=utf-8
# https://segmentfault.com/a/1190000004467183
import datetime
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
import cv2
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']


def showPlt(data):
    x = np.arange(len(data))
    plt.plot(x, data, color='r')
    plt.bar(x, data, alpha=0.5, color='g')
    plt.show()


def getHistogram(img):
    size = (256, 256)
    img = img.resize(size).convert("RGB")
    return img.histogram()


def compareHist(data1, data2):
    length = max(data1 + data2)
    hist1 = pylab.histogram(data1, bins=length, normed=True)[0]
    hist2 = pylab.histogram(data2, bins=length, normed=True)[0]
    total = 0.0
    for i in range(0, length):
        if hist1[i] == 0 and hist2[i] == 0:
            total += 1
        else:
            total += (1 - abs(hist1[i] - hist2[i])/max(hist1[i], hist2[i]))
    return total/length


def quickCompare(a, b):
    img1 = Image.open("data/" + str(a) + ".jpg", mode="r")
    img2 = Image.open("data/" + str(b) + ".jpg", mode="r")
    print compareHist(getHistogram(img1), getHistogram(img2))


def CVsplit2RGB(imgPath):
    imgCV = cv2.resize(
        cv2.imread(imgPath),
        (256, 256),
        interpolation=cv2.INTER_CUBIC
        )
    return cv2.split(imgCV)


def quickCompareCV(a, b):
    b1, g1, r1 = CVsplit2RGB("data/" + str(a) + ".jpg")
    b2, g2, r2 = CVsplit2RGB("data/" + str(b) + ".jpg")
    print "(histogram)Compare " + str(a) + " to " + str(b)
    print ("R: %.2f, G: %.2f, B: %.2f" % (
        compareHist(r1.flatten(), r2.flatten()),
        compareHist(g1.flatten(), g2.flatten()),
        compareHist(b1.flatten(), b2.flatten())
    ))


if __name__ == "__main__":
    start = datetime.datetime.now()
    """
    quickCompare(6, 7)
    quickCompare(1, 2)
    quickCompare(1, 1)
    quickCompare(8, 8)
    """
    quickCompareCV(1, 2)
    quickCompareCV(6, 7)
    quickCompareCV(2, 5)
    quickCompareCV(8, "8-lighten")

    end = datetime.datetime.now()
    print "Process time = " + str(end-start)

    # raw_input()
