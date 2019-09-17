from gpiozero import Robot
import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)

print("Wake Up Plant Wartering Robot")
time.sleep(3)

servoPIN = 26
pumpPIN = 16
IO.setup(servoPIN, IO.OUT)
IO.setup(pumpPIN, IO.OUT)

IO.output(pumpPIN,IO.LOW)

p = IO.PWM(servoPIN, 50)
if servoPIN != 0:
    print("Servo Motor Setting Up")
    time.sleep(3)
    p.start(2.5)
    print("Stay Home")
    p.ChangeDutyCycle(7)
    time.sleep(2)
    print("Turn Right")
    p.ChangeDutyCycle(5)
    time.sleep(2)
    print("Stay Home")
    p.ChangeDutyCycle(7)
    time.sleep(2)
    print("Turn Left")
    p.ChangeDutyCycle(9)
    time.sleep(2)
    print("Stay Home")
    p.ChangeDutyCycle(7)
    time.sleep(2)
    p.start(0)

time.sleep(2)
p.start(0)

kps = Robot(left=(22,23), right=(17,18))

IO.setup(21,IO.IN)
IO.setup(20,IO.IN)
status = 1
stopTime = 0
print("Engin Start To Go")
time.sleep(2)
print("Moves Forward")
time.sleep(2)
while status:
    l_sensor = IO.input(21)
    r_sensor = IO.input(20)

    if l_sensor == 1 and r_sensor == 1 :
        kps.forward(0.7)
        IO.output(pumpPIN,IO.LOW)

    if l_sensor == 1 and r_sensor == 0 :
        kps.left(0.7)
    if l_sensor == 0 and r_sensor == 1 :
        kps.right(0.7)	

    if l_sensor == 0 and r_sensor == 0 :
        stopTime = stopTime + 1
        print("Stop Robot To Water Plant")
        kps.stop()
        time.sleep(3)
        print("Turn Right The Pipe")
        p.ChangeDutyCycle(2)
        time.sleep(1)
        p.start(0)
        time.sleep(2)
        IO.output(pumpPIN,IO.HIGH)
        print("Pump Switch On")
        time.sleep(1)
        IO.output(pumpPIN,IO.LOW)
        print("Pump Switch Off")
        time.sleep(2)
        print("Stay Home")
        p.ChangeDutyCycle(7)
        time.sleep(1)
        print("Turn Left The Pipe")
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        p.start(0)
        time.sleep(2)
        IO.output(pumpPIN,IO.HIGH)
        print("Pump Switch On")
        time.sleep(1)
        IO.output(pumpPIN,IO.LOW)
        print("Pump Switch Off")
        time.sleep(2)
        print("Stay Home")
        p.ChangeDutyCycle(7)
        time.sleep(2)
        if(stopTime == 1):
            IO.cleanup()
            print("Change Motors")
            time.sleep(2)
            kps = Robot(left=(23, 22), right=(18, 17))
        if(stopTime == 2):
            IO.cleanup()
            print("Change Motors")
            time.sleep(2)
            kps = Robot(left=(22, 23), right=(17, 18))
            stopTime = 0
        print("Moves Forward")
        kps.forward(0.5)
        time.sleep(1)




	