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

# Configure the GPIO Pins
motors = [motor1, motor2, motor3]
GPIO.setmode(GPIO.BCM)
for motor in motors:
    GPIO.setup(motor['in_1'], GPIO.OUT)
    GPIO.setup(motor['in_2'], GPIO.OUT)
    GPIO.setup(motor['en'], GPIO.OUT)

# Pulse Width Modulation
p1 = GPIO.PWM(motor1['en'], 1000)
p2 = GPIO.PWM(motor2['en'], 1000)
p3 = GPIO.PWM(motor3['en'], 1000)

p1.start(60)
p2.start(60)
p3.start(60)

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
        p1.ChangeDutyCycle(60)
        p2.ChangeDutyCycle(60)
        p3.ChangeDutyCycle(60)

    elif ctrl == 'a':
        print("left")
        GPIO.output(motor1['in_1'], GPIO.LOW)
        GPIO.output(motor1['in_2'], GPIO.HIGH)
        GPIO.output(motor2['in_1'], GPIO.LOW)
        GPIO.output(motor2['in_2'], GPIO.HIGH)
        GPIO.output(motor3['in_1'], GPIO.HIGH)
        GPIO.output(motor3['in_2'], GPIO.LOW)
        p1.ChangeDutyCycle(70)
        p2.ChangeDutyCycle(55)
        p3.ChangeDutyCycle(55)

    elif ctrl == 's':
        print("backwards")
        GPIO.output(motor1['in_1'], GPIO.LOW)
        GPIO.output(motor1['in_2'], GPIO.LOW)
        GPIO.output(motor2['in_1'], GPIO.HIGH)
        GPIO.output(motor2['in_2'], GPIO.LOW)
        GPIO.output(motor3['in_1'], GPIO.HIGH)
        GPIO.output(motor3['in_2'], GPIO.LOW)
        p1.ChangeDutyCycle(60)
        p2.ChangeDutyCycle(60)
        p3.ChangeDutyCycle(60)

    elif ctrl == 'd':
        print("right")
        GPIO.output(motor1['in_1'], GPIO.HIGH)
        GPIO.output(motor1['in_2'], GPIO.LOW)
        GPIO.output(motor2['in_1'], GPIO.HIGH)
        GPIO.output(motor2['in_2'], GPIO.LOW)
        GPIO.output(motor3['in_1'], GPIO.LOW)
        GPIO.output(motor3['in_2'], GPIO.HIGH)
        p1.ChangeDutyCycle(70)
        p2.ChangeDutyCycle(55)
        p3.ChangeDutyCycle(55)

    elif ctrl == 'e':
        GPIO.cleanup()
        break

    else:
        print("try again")
