import RPi.GPIO as GPIO
from time import sleep

# Initialize the motors
motor1 = {
    "in_1": 24,
    "in_2": 23,
    "en": 25
}
motor2 = {
    "in_1": 7,
    "in_2": 8,
    "en": 12
}
motor3 = {
    "in_1": 16,
    "in_2": 20,
    "en": 21
}

motors = [motor1, motor2, motor3]

GPIO.setmode(GPIO.BCM)
for motor in motors:
    # Configure the GPIO Pins
    GPIO.setup(motor['in_1'], GPIO.OUT)
    GPIO.setup(motor['in_2'], GPIO.OUT)
    GPIO.setup(motor['en'], GPIO.OUT)

# GPIO.setup(in1,GPIO.OUT)
# GPIO.setup(in2,GPIO.OUT)
# GPIO.setup(en,GPIO.OUT)
# GPIO.output(in1,GPIO.LOW)
# GPIO.output(in2,GPIO.LOW)

# Pulse Width Modulation
p1 = GPIO.PWM(motor1['en'], 1000)
p2 = GPIO.PWM(motor2['en'], 1000)
p3 = GPIO.PWM(motor3['en'], 1000)

p1.start(55/2)
p2.start(55)
p3.start(55)

# make sure all motors aren't moving at start
GPIO.output(motor1['in_1'], GPIO.LOW)
GPIO.output(motor1['in_2'], GPIO.LOW)
GPIO.output(motor2['in_1'], GPIO.LOW)
GPIO.output(motor2['in_2'], GPIO.LOW)
GPIO.output(motor3['in_1'], GPIO.LOW)
GPIO.output(motor3['in_2'], GPIO.LOW)

print("\n")
print("wasd movement with q to stop and e to exit .....")
print("\n")

while(1):

    ctrl = raw_input()

    # wasd movement, q to stop.
    if ctrl == 'q':
        print("stop")
        GPIO.output(motor1['in_1'], GPIO.LOW)
        GPIO.output(motor1['in_2'], GPIO.LOW)
        GPIO.output(motor2['in_1'], GPIO.LOW)
        GPIO.output(motor2['in_2'], GPIO.LOW)
        GPIO.output(motor3['in_1'], GPIO.LOW)
        GPIO.output(motor3['in_2'], GPIO.LOW)

    elif ctrl == 'w':
        print("forwards")
        GPIO.output(motor1['in_1'], GPIO.LOW)
        GPIO.output(motor1['in_2'], GPIO.LOW)
        GPIO.output(motor2['in_1'], GPIO.LOW)
        GPIO.output(motor2['in_2'], GPIO.HIGH)
        GPIO.output(motor3['in_1'], GPIO.LOW)
        GPIO.output(motor3['in_2'], GPIO.HIGH)
        p1.ChangeDutyCycle(55/2)
        p2.ChangeDutyCycle(55)
        p3.ChangeDutyCycle(55)

    elif ctrl == 'a':
        print("left")
        GPIO.output(motor1['in_1'], GPIO.LOW)
        GPIO.output(motor1['in_2'], GPIO.HIGH)
        GPIO.output(motor2['in_1'], GPIO.LOW)
        GPIO.output(motor2['in_2'], GPIO.HIGH)
        GPIO.output(motor3['in_1'], GPIO.HIGH)
        GPIO.output(motor3['in_2'], GPIO.LOW)
        p1.ChangeDutyCycle(55/2)
        p2.ChangeDutyCycle(40)
        p3.ChangeDutyCycle(40)

    elif ctrl == 's':
        print("backwards")
        GPIO.output(motor1['in_1'], GPIO.LOW)
        GPIO.output(motor1['in_2'], GPIO.LOW)
        GPIO.output(motor2['in_1'], GPIO.HIGH)
        GPIO.output(motor2['in_2'], GPIO.LOW)
        GPIO.output(motor3['in_1'], GPIO.HIGH)
        GPIO.output(motor3['in_2'], GPIO.LOW)
        p1.ChangeDutyCycle(55/2)
        p2.ChangeDutyCycle(55)
        p3.ChangeDutyCycle(55)

    elif ctrl == 'd':
        print("right")
        GPIO.output(motor1['in_1'], GPIO.HIGH)
        GPIO.output(motor1['in_2'], GPIO.LOW)
        GPIO.output(motor2['in_1'], GPIO.HIGH)
        GPIO.output(motor2['in_2'], GPIO.LOW)
        GPIO.output(motor3['in_1'], GPIO.LOW)
        GPIO.output(motor3['in_2'], GPIO.HIGH)
        p1.ChangeDutyCycle(55/2)
        p2.ChangeDutyCycle(40)
        p3.ChangeDutyCycle(40)

    elif ctrl == 'l':
        print("low")
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        p3.ChangeDutyCycle(25)

    elif ctrl == 'm':
        print("medium")
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        p3.ChangeDutyCycle(50)

    elif ctrl == 'h':
        print("high")
        p1.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        p3.ChangeDutyCycle(75)

    elif ctrl == 'e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
