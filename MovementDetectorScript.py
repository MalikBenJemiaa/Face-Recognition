from gpiozero import MotionSensor
p = MotionSensor(12)
while True:
    print("Movement scan!!")
    p.wait_for_motion()
    print("Movement detected!!")
    # run one the face recognition scripts
    p.wait_for_no_motion()
    print('The area is clear')
