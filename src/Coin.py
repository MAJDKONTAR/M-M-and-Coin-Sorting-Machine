import cv2
import numpy as np

def checkCoin(i):
    img=i[0:500,0:i.shape[1]]
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     width, height = 389, 113
#     pts1 = np.float32([[30, 205], [1276, 300], [2, 480], [1265, 620]])
#     pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
#     matrix = cv2.getPerspectiveTransform(pts1, pts2)
#     imgOut = cv2.warpPerspective(imgHSV, matrix, (width, height))
    colors =np.array(['250','500'])
    masks=np.array([[10,127,54,58,255,172],[9,0,78,47,93,150]])
#     cv2.imshow('img',img)
#     cv2.waitKey(10)     
    for i,mask in enumerate (masks):
        out=cv2.inRange(imgHSV,mask[0:3],mask[3:6])
#         cv2.imshow('out',out)
#         cv2.waitKey(0)
        sum=np.sum(out)
#         print(sum)
        if sum>150000:
#             print('The coin is: '+str(colors[i]))
            return colors[i]
    return 'not identified!'
#     cv2.imshow('img',img)
#     cv2.waitKey(0)

def main ():
    video=cv2.VideoCapture(0)
    video.set(3, 1280)
    video.set(4, 1024)
    video.set(15, -8)
    while 1:
        check, f = video.read()
        img=f[0:500,0:f.shape[1]]
        cv2.imshow('i',img)
        cv2.waitKey(0)
        checkCoin(img)
        
if __name__ == "__main__":
    main()
