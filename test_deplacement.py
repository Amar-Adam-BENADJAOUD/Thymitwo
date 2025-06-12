import time
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor, servo


MOTOR_IN1 =  15      #Define the positive pole of M1
MOTOR_IN2 =  14      #Define the negative pole of M1

i2c = busio.I2C(SCL, SDA)
pwm_motor = PCA9685(i2c, address=0x5f)
pwm_motor.frequency = 50
pwm_servo = PCA9685(i2c, address=0x6f) # adresse peut creer bug
pwm_servo.frequency = 50

motor1 = motor.DCMotor(pwm_motor.channels[MOTOR_IN1],pwm_motor.channels[MOTOR_IN2] )
motor1.decay_mode = (motor.SLOW_DECAY)

def set_angle(ID, angle):
    servo_angle = servo.Servo(pca.channels[ID], min_pulse=500, max_pulse=2400,actuation_range=180)
    servo_angle.angle = angle

def map(x,in_min,in_max,out_min,out_max):
    return (x - in_min)/(in_max - in_min) *(out_max - out_min) +out_min

def motor(direction,motor_speed):
    if motor_speed > 100:
        motor_speed = 100
    elif motor_speed < 0:
        motor_speed = 0
    speed = map(motor_speed, 0, 100, 0, 1.0)
    if direction == -1:
        speed = -speed
    motor1.throttle = speed

def destroy():
    motor1.throttle = 0
    pwm_servo.deinit()
    pwm_motor.deinit()

def forward(speed):
    speed_set=0
    for i in range(speed):
        speed_set+=1
        motor(1, speed_set)
        time.sleep(0.01)

def backward(speed):
    speed_set=0
    for i in range(speed):
        speed_set+=1
        motor(-1, speed_set)
        time.sleep(0.01)

def stop():
    motor(1, 0)

def turn_left(angle):
    set_angle(0, 90+angle)

def turn_right(angle):
    set_angle(0, 90-angle)