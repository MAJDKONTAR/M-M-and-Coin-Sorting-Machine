import cv2
import numpy as np

def checkColor(i):
    img=i[60:650,50:i.shape[1]]
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     cv2.imshow('i',img)
#     cv2.waitKey(0)
    
    colors =np.array(['yellow','green','pink','orange'])
    masks=np.array([[20,100,100,30,255,255],[44,127,54,58,255,172],[155,110,109,181,234,233],[0,130,115,12,255,218]])
#     cv2.imshow('img',img)
#     cv2.waitKey(0)     
    for i, mask in enumerate(masks):
        out=cv2.inRange(imgHSV,mask[0:3],mask[3:6])
        sum=np.sum(out)
        if sum>10000:
            print('The color is: '+str(colors[i]))
            return colors[i]
    print('Color not identified!')
    return None
#     cv2.imshow('img',img)
#     cv2.waitKey(0)

def main ():
    video=cv2.VideoCapture(0)
    video.set(3, 1280)
    video.set(4, 1024)
    video.set(15, -8)
    while 1:
        check, f = video.read()
#         img=f[0:800,0:f.shape[1]]
#         cv2.imshow('i',f)
#         cv2.waitKey(0)
        checkColor(f)
        
if __name__ == "__main__":
    main()