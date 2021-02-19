# This REPL (Read Eval Print Loop) Terminal runs on your computer
# and sends commands to the CPX board in the robot.
# It's just for testing robot commands.

import serial
import sys

com_connection = None
com_port = 'COM5'
baud_rate = 9600 # in bits / sec

# NOTE: Change your COM string to be what you see in Device Manager.
#       and make sure the baudrate matches double-clicked --> Port Settings.
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
    elif action == "open claw":
        # TODO: Send USB command "OPEN_CLAW" to the CPX board.
        com_connection.write("OPEN_CLAW") # might need to make this a binary string like b'OPEN_CLAW\n\r'
    elif action == "close claw":
        # TODO: Send USB command "CLOSE_CLAW" to the CPX board.
        com_connection.write("CLOSE_CLAW") # b"OPEN_CLAW"
    elif action == "quit":
        break
    # TODO: Read any new messages from the robot,
    #       using the com_connection.
    #       Print those messages out here.

print("Goodbye!")

# Close the COM port. Although, I'm pretty sure this already gets called automatically when the script is done...
com_connection.close()
