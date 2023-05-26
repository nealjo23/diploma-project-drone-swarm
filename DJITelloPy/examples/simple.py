from djitellopy import Tello

tello = Tello("10.25.35.127")

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.rotate_clockwise(90)
tello.move_forward(100)

tello.land()
