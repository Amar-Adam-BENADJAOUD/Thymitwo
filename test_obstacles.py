import test_ultra, test_deplacement, time

DISTANCE = 200
SPEED = 100
ANGLE = 5
INTER = 0.01

def evitement():
    # Move forward until an obstacle is detected
    while(test_ultra.ultrasonic_distance() > DISTANCE):
        test_deplacement.forward(SPEED)

    # Avoid the obstacle and go back into your initial sens
    for i in range(10):
        test_deplacement.turnleft(ANGLE * i)
        time.sleep(INTER)
    test_deplacement.forward(SPEED)
    time.sleep(1)
    for i in range(10):
        test_deplacement.turnright(ANGLE * i)
        time.sleep(INTER)

    # Move forward until overtake the obstacle
    test_deplacement.forward(SPEED)
    time.sleep(5)


    # Go back into your initial path
    for i in range(10):
        test_deplacement.turnright(ANGLE * i)
        time.sleep(INTER)
    test_deplacement.forward(SPEED)
    time.sleep(1)
    for i in range(10):
        test_deplacement.turnleft(ANGLE * i)
        time.sleep(INTER)


while(True) :
    while(1):
        evitement()
