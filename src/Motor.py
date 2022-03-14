import RPi.GPIO as IO
import time


def motor1(dutyCycle1, front, back, duration=0):
    IN1 = IO.output(18, back)
    IN2 = IO.output(16, front)
    pwm1 = IO.PWM(33, 100)
    pwm1.start(dutyCycle1)
    # pwm1.ChangeDutyCycle(dutyCycle1)
#     print('Motor 1 running')
    time.sleep(duration)
    IN1 = IO.output(18, 1)
    IN2 = IO.output(16, 1)

def motor2(dutyCycle2, right, left, duration=0):
    IN3 = IO.output(29, left)
    IN4 = IO.output(31, right)
    pwm2 = IO.PWM(12, 100)
    pwm2.start(dutyCycle2)
    # pwm2.ChangeDutyCycle(dutyCycle2)
#     print('Motor 2 running')
    time.sleep(duration)
    IN3 = IO.output(29, 1)
    IN4 = IO.output(31, 1)