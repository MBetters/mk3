# This REPL (Read Eval Print Loop) Terminal runs on your computer
# and sends commands to the CPX board in the MK3 robot.
# It's just for testing robot commands.
import time
import serial
import sys
# NOTE: Change your COM string to be what you see in Device Manager.
#       and make sure the baudrate matches double-clicked --> Port Settings.
com_connection = None
com_port = 'COM5'
baud_rate = 115200 # in bits / sec
read_timeout = 1 # in secs
try:
    # Try to open the COM port....
    com_connection = serial.Serial(port=com_port, baudrate=baud_rate, timeout=read_timeout)
except serial.serialutil.SerialException:
    # ... but if it fails to open, then give the user some hints....
    print("Cannot connect to your robot over USB!!! Possible causes....")
    print("1. You have Mu open and it locked the COM port. Close it!!")
    print("2. You have another Python shell open with the COM port locked.Quit it with quit()!!!")
    print(f"3. The COM port you provided is wrong. You gave me {com_port}, but maybe that's the wrong COM port. Check your Device Manager.")
    print(f"4. The baud rate you provided is wrong. You gave me {baud_rate}, but maybe it's set up with a different baud rate. Check Device Manager.")
    print(".... There's multiple other potential problems probably not listed here.")
    print("Goodbye!")
    sys.exit() # Exit this script. We can't run without a working COM connection.
from inputs import devices, get_gamepad
# NOTE: I'm assuming we're only using XBox / Logitech controllers.
#       i.e.- A, B, etc.
while True:
    events = get_gamepad() # gets the latest gamepad input events
    for event in events:
        print("-----------------------------------------")
        print(event.ev_type, event.code, event.state)
        # Handle the A button
        if event.code == "BTN_SOUTH" and event.state == 1:
            print("A button pressed")
            # TODO: Send USB commands to the robot
        elif event.code == "BTN_SOUTH" and event.state == 0:
            print("A button unpressed")
        # Handle the B button
        if event.code == "BTN_EAST" and event.state == 1:
            print("B button pressed")
        elif event.code == "BTN_EAST" and event.state == 0:
            print("B button unpressed")
        # Handle the Y button
        if event.code == "BTN_NORTH" and event.state == 1:
            print("Y button pressed")
        elif event.code == "BTN_NORTH" and event.state == 0:
            print("Y button unpressed")
        # Handle the X button
        if event.code == "BTN_WEST" and event.state == 1:
            print("X button pressed")
        elif event.code == "BTN_WEST" and event.state == 0:
            print("X button unpressed")
        # Handle the left trigger
        if event.code == "ABS_Z" and event.state > 0:
            print("LT pressed")
            num_bytes_written = com_connection.write(b"START_CLOSE_CLAW\n\r")
        if num_bytes_written != len("START_CLOSE_CLAW\n\r"):
            print("ERROR: Couldn't write the full command")
        elif event.code == "ABS_Z" and event.state == 0:
            print("LT not pressed")
            num_bytes_written = com_connection.write(b"STOP_CLOSE_CLAW\n\r")
        if num_bytes_written != len("STOP_CLOSE_CLAW\n\r"):
            print("ERROR: Couldn't write the full command")
            print(event.ev_type, event.code, event.state)
        # Handle the right trigger
        if event.code == "ABS_RZ" and event.state > 0:
            print("RT pressed")
            num_bytes_written = com_connection.write(b"START_OPEN_CLAW\n\r")
        if num_bytes_written != len("START_OPEN_CLAW\n\r"):
            print("ERROR: Couldn't write the full command")
        elif event.code == "ABS_RZ" and event.state == 0:
            print("RT not pressed")
            num_bytes_written = com_connection.write(b"STOP_OPEN_CLAW\n\r")
            #This code is never gonna give you up...
        if num_bytes_written != len("STOP_OPEN_CLAW\n\r"):
            print("ERROR: Couldn't write the full command")
            print(event.ev_type, event.code, event.state)
        # Likewise as the above section for the right trigger,
        # except it should send commands to open the claw / stop opening it.
        # TODO: Vibrate the gamepad when the robot knows that it has picked
        #       up the soda can. https://raw.githubusercontent.com/zeth/inputs/master/examples/vibrate_example.py
        # TODO: Use joystick events to move the robot arm.
        #       Maybe right joystick left/right rotates the forearm in/out.
        #       Maybe right joystick up/down does nothing.
        #       Maybe left joystick up/down rotates the upper arm up/down.
        #       Maybe left joystick left/right rotates the shoulder CW/CCW.
        # IM a convertable