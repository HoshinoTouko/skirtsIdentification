# coding=utf-8
# Avarage hash
# https://segmentfault.com/a/1190000004467183
import datetime
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
import cv2


def CVsplit2RGB(imgPath):
    imgCV = cv2.resize(
        cv2.imread(imgPath),
        (16, 16),
        interpolation=cv2.INTER_CUBIC
        )
    return cv2.split(imgCV)


def getMatrixOffset(matrix):
    length = len(matrix)
    width = len(matrix[0])
    average = 1.0 * sum(matrix.flatten()) / (length*width)
    output = []
    for x in matrix:
        tempY = []
        for y in x:
            if y > average:
                tempY.append(1)
            else:
                tempY.append(0)
        output.append(tempY)
    return np.array(output)


def compareMatrixOffset(matrix1, matrix2):
    itemsNumber = len(matrix1.flatten())
    sameNumber = 0
    for x in range(len(matrix1)):
        for y in range(len(matrix2)):
            if matrix1[x][y] == matrix2[x][y]:
                sameNumber += 1
    return 1.0 * sameNumber/itemsNumber


def aHashCompare(a, b):
    b1, g1, r1 = CVsplit2RGB("data/" + str(a) + ".jpg")
    b2, g2, r2 = CVsplit2RGB("data/" + str(b) + ".jpg")
    # merged = cv2.merge([b1, g1, r1])
    # cv2.imshow("test", merged)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print "(aHash)Compare " + str(a) + " to " + str(b)
    print "R: %.2f G: %.2f B: %.2f" % (
        compareMatrixOffset(
            getMatrixOffset(r1),
            getMatrixOffset(r2)
        ),
        compareMatrixOffset(
            getMatrixOffset(g1),
            getMatrixOffset(g2)
        ),
        compareMatrixOffset(
            getMatrixOffset(b1),
            getMatrixOffset(b2)
        )
    )


if __name__ == "__main__":
    start = datetime.datetime.now()

    aHashCompare(1, 1)
    aHashCompare(6, 7)
    aHashCompare(8, "8-lighten")

    end = datetime.datetime.now()
    print "Process time = " + str(end-start)
