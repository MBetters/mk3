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
            # TODO AJ and Owen: Send the robot USB command to close the claw
        elif event.code == "ABS_Z" and event.state == 0:
            print("LT not pressed")
            # TODO: Send the robot USB command stop closing the claw
            print(event.ev_type, event.code, event.state)
        # Handle the right trigger
        if event.code == "ABS_RZ" and event.state > 0:
            print("RT pressed")
            # TODO AJ and Owen: Send the robot USB commands to close the claw
        elif event.code == "ABS_RZ" and event.state == 0:
            print("RT not pressed")
            # TODO: Send the robot USB command stop closing the claw
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