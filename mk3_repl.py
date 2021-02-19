# This REPL (Read Eval Print Loop) Terminal runs on your computer
# and sends commands to the CPX board in the MK3 robot.
# It's just for testing robot commands.

import serial
import sys

com_connection = None

# NOTE: Change your COM string to be what you see in Device Manager.
#       and make sure the baudrate matches double-clicked --> Port Settings.
com_port = 'COM5'
baud_rate = 9600 # in bits / sec

try:
    # Try to open the COM port....
    com_connection = serial.Serial(com_port, baud_rate)
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

prompt = ">>> "

while True:
    action = input(prompt)
    if action == "help":
        print("open claw: Opens the claw")
        print("close claw: Closes the claw")
        print("quit: Quit this REPL Terminal")
        print("red off: Turn off red LED blinking")
        print("red on: Turn on red LED blinking")
        print("terminate: Terminate the code running on the robot")
        print("quit: Exit out of this REPL")
    elif action == "open claw":
        com_connection.write(b"OPEN_CLAW")
    elif action == "close claw":
        com_connection.write(b"CLOSE_CLAW")
    elif action == "red off":
        com_connection.write(b"RED_OFF")
    elif action == "red on":
        # TODO: There's a bug where if you do 'red off' then 'red on', it won't work. Can you solve it?
        com_connection.write(b"RED_ON")
    elif action == "terminate":
        com_connection.write(b"TERMINATE")
    elif action == "quit":
        break
    # TODO: Read any new messages from the robot,
    #       using function(s) from the com_connection object.
    #       Print those messages out here.

print("Goodbye!")

# Close the COM port. Although, I'm pretty sure this already gets called automatically when the script is done...
com_connection.close()
