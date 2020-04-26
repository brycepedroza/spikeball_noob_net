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
    GPIO.setmode(motor['in_1', GPIO.OUT])
    GPIO.setmode(motor['in_2', GPIO.OUT])
    GPIO.setmode(motor['en', GPIO.OUT])

# GPIO.setup(in1,GPIO.OUT)
# GPIO.setup(in2,GPIO.OUT)
# GPIO.setup(en,GPIO.OUT)
# GPIO.output(in1,GPIO.LOW)
# GPIO.output(in2,GPIO.LOW)

# Pulse Width Modulation
p = GPIO.PWM(en, 1000)
p.start(66)

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

    if ctrl == 'w':
        print("forward")
        GPIO.output(motor1['in_1'], GPIO.LOW)
        GPIO.output(motor1['in_2'], GPIO.LOW)
        GPIO.output(motor2['in_1'], GPIO.HIGH)
        GPIO.output(motor2['in_2'], GPIO.LOW)
        GPIO.output(motor3['in_1'], GPIO.HIGH)
        GPIO.output(motor3['in_2'], GPIO.LOW)

    if ctrl == 's':
        print("backwards")
        GPIO.output(motor1['in_1'], GPIO.LOW)
        GPIO.output(motor1['in_2'], GPIO.LOW)
        GPIO.output(motor2['in_1'], GPIO.LOW)
        GPIO.output(motor2['in_2'], GPIO.HIGH)
        GPIO.output(motor3['in_1'], GPIO.LOW)
        GPIO.output(motor3['in_2'], GPIO.HIGH)

    elif ctrl == 'l':
        print("low")
        p.ChangeDutyCycle(25)
        ctrl = 'z'

    elif ctrl == 'm':
        print("medium")
        p.ChangeDutyCycle(50)
        ctrl = 'z'

    elif ctrl == 'h':
        print("high")
        p.ChangeDutyCycle(75)
        ctrl = 'z'

    elif ctrl == 'e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
