import cv2
import numpy as np
import math


PIXEL_TO_CM_FACTOR = 0.0264583333
width, height = 389, 113
pts1=np.float32([[3,160],[1276,120],[10,520],[1276,490]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)


def getSize(img,imgContour):
    contour = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
    for cnt in contour:
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt, True)
        radiusFromArea = math.sqrt(area * PIXEL_TO_CM_FACTOR * PIXEL_TO_CM_FACTOR / math.pi)
        radiusFromPeri = peri * PIXEL_TO_CM_FACTOR / math.pi / 2
        radius = (radiusFromArea + radiusFromPeri) / 2
        if radius > 0.5:
#             print('radius from area: ', radiusFromArea)
#             print('radius from peri: ', radiusFromPeri)
            print('radius: ', radius)
#             cv2.drawContours(imgContour, cnt, -1, (255, 255, 0), 2)
            return radius
        else:
            return None 


def autoCanny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    # return the edged image
    return edged
    
    
def getSpecs(f):
    frame=f[0:800,0:f.shape[1]]    
    imgOut = cv2.warpPerspective(frame, matrix, (width, height))
    imgContour = imgOut.copy()
    for i in range(0, 4):
        cv2.circle(frame, (pts1[i][0], pts1[i][1]), 5, (0,255, 255), cv2.FILLED)
    imgBlur = cv2.GaussianBlur(imgOut, (11, 11), 0)
    thresh = cv2.threshold(imgBlur, 60, 200, cv2.THRESH_BINARY)[1]
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
#     closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    auto = autoCanny(thresh)
#     dilate = cv2.morphologyEx(auto, cv2.MORPH_DILATE, kernel, iterations=1)
#     cv2.imshow('dilate',dilate)
#     cv2.imshow('Blur',imgBlur)
#     cv2.imshow('result', imgResult)
#     cv2.imshow("Canny", auto)
#     cv2.imshow('closing', closing)
#     cv2.imshow('thresh', thresh)
#     cv2.imshow("Contour", imgContour)
#     cv2.imshow('frame', frame)
#     cv2.imshow('Warp', imgOut)
#     cv2.waitKey(0)
    return getSize(auto, imgContour)


def coin(radius):
    try:
#         print('radius= ',radius)
        twoFifty=1.175
        fiveHundred=1.225
        val1=abs(twoFifty-radius)
        val2=abs(fiveHundred-radius)
        if min(val1,val2)>0.5:
            return False
        else:
            return True
    except:
        return False


def main():
    video = cv2.VideoCapture(0)
    video.set(3, 1280)
    video.set(4, 1024)
    video.set(15, -8)
    back=video.read()[1]
    cv2.imshow('back',back)
    cv2.waitKey(0)
    back=cv2.cvtColor(back,cv2.COLOR_BGR2GRAY)
    back=cv2.bitwise_not(back)
    while 1:
        check, f = video.read()
        i=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
        i = cv2.bitwise_and(i, back, mask = back)
        radius=getSpecs(i)
        print(coin(radius))
    
if __name__ == "__main__":
    main()