from djitellopy import Tello

tello = Tello()

tello.connect()

tello.send_command_without_return()

