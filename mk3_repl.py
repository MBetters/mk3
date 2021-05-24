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

# If we get to this point, then com_connection should not be equal to None!

print("Do 'help' to ask for help!")
prompt = ">>> "

while True:
    action = input(prompt)
    if action == "help":
        print("open claw: Opens the claw")
        print("close claw: Closes the claw")
        print("red off: Turn off red LED blinking")
        print("red on: Turn on red LED blinking")
        print("terminate: Terminate the code running on the robot")
        print("quit: Exit out of this REPL")
    elif action == "open claw":
        num_bytes_written = com_connection.write(b"OPEN_CLAW\n\r")
        if num_bytes_written != len("OPEN_CLAW\n\r"):
            print("ERROR: Couldn't write the full command")
    elif action == "close claw":
        num_bytes_written = com_connection.write(b"CLOSE_CLAW\n\r")
        if num_bytes_written != len("CLOSE_CLAW\n\r"):
            print("ERROR: Couldn't write the full command")
    elif action == "red off":
        num_bytes_written = com_connection.write(b"RED_OFF\n\r")
        if num_bytes_written != len("RED_OFF\n\r"):
            print("ERROR: Couldn't write the full command")
    elif action == "red on":
        # TODO: There's a bug where if you do 'red off' then 'red on', it won't work. Can you solve it?
        num_bytes_written = com_connection.write(b"RED_ON\n\r")
        if num_bytes_written != len("RED_ON\n\r"):
            print("ERROR: Couldn't write the full command")
    elif action == "terminate":
        num_bytes_written = com_connection.write(b"TERMINATE\n\r")
        if num_bytes_written != len("TERMINATE\n\r"):
            print("ERROR: Couldn't write the full command")
    elif action == "quit":
        break
    # If you sent a command to the robot, then wait for it to flush.
    if action not in ["help", "quit"]:
        time.sleep(3)
        all_bytes_from_robot = com_connection.read_all()
        print("All bytes from MK3:")
        print(all_bytes_from_robot)

# Close the COM port. Although, I'm pretty sure this already gets called automatically when the script is done...
com_connection.close()

print("Goodbye!")
