import cv2
import Motor
import time
import Color
import Size
import RPi.GPIO as IO


def main():
    video=cv2.VideoCapture(0)
    video.set(3, 1280)
    video.set(4, 1024)
    video.set(15, -8)
    IO.setwarnings(False)
    IO.setmode(IO.BOARD)
    IO.setup(12, IO.OUT)
    IO.setup(16, IO.OUT)
    IO.setup(18, IO.OUT)
    IO.setup(29, IO.OUT)
    IO.setup(31, IO.OUT)
    IO.setup(33, IO.OUT)
    IO.setup(38, IO.OUT)
    IO.setup(40, IO.OUT)
    IO.setup(36, IO.OUT)

    while True:
        back = video.read()[1]
        Motor.motor1(50, 1, 0, 0.5)
        for x in range (10):
            fore = video.read()[1]
        color=Color.checkColor(fore)
        back=cv2.cvtColor(back,cv2.COLOR_BGR2GRAY)
        fore=cv2.cvtColor(fore,cv2.COLOR_BGR2GRAY)
        back=cv2.bitwise_not(back)
        i = cv2.bitwise_and(fore, back, mask = back)
        radius=Size.getSpecs(i)
        print('*'*50)
        if color=='green':
            green = IO.output(38, 1)
            Motor.motor1(50, 1, 0, 1.2)
            Motor.motor2(75, 1,0, 1)
            green = IO.output(38, 0)
        elif color=='yellow':
            yellow = IO.output(40, 1)
            Motor.motor1(50, 1, 0, 1.2)
            Motor.motor2(75,0,1,1)
            yellow = IO.output(40, 0)
        else:
            red = IO.output(36, 1)
            Motor.motor1(100,0,1,1)
            red= IO.output(36,0)
        time.sleep(2)
    


if __name__ == "__main__":
    main()
