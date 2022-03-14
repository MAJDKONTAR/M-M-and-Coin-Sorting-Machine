import cv2
import Motor
import time
import Coin
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
    money=0
    back = video.read()[1]
    back=cv2.cvtColor(back,cv2.COLOR_BGR2GRAY)
    back=cv2.bitwise_not(back)

    while True:
        
        Motor.motor1(50, 1, 0, 0.4)
        for x in range (20):
            fore = video.read()[1]
        coin=Coin.checkCoin(fore)
        fore=cv2.cvtColor(fore,cv2.COLOR_BGR2GRAY)
        i = cv2.bitwise_and(fore, back, mask = back)
        radius=Size.getSpecs(i)
        correct=Size.coin(radius)
        if correct:
            print('The coin is ',coin)
        else:
            print('Rejected')
        print('*'*50)
        if correct:
            
            if coin=='250':
                green = IO.output(38, 1)
                Motor.motor1(50, 1, 0, 1.2)
                time.sleep(1)
                Motor.motor2(80, 1,0, 1)
                money+=250
                green = IO.output(38, 0)
                
            elif coin=='500':
                yellow = IO.output(40, 1)
                Motor.motor1(50, 1, 0, 1.2)
                time.sleep(1)
                Motor.motor2(80,0,1,1)
                money+=500
                yellow = IO.output(40, 0)
            else:
                red = IO.output(36, 1)
                Motor.motor1(100,0,1,1)
                red= IO.output(36,0)
        else:
            red = IO.output(36, 1)
            Motor.motor1(100,0,1,1)
            red= IO.output(36,0)
        print('Your balance is: '+str(money)+'L.L.')
        time.sleep(2)
    


if __name__ == "__main__":
    main()
