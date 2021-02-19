# This runs on the CPX board.

import board
import digitalio
import time
import supervisor

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

print("I AM ROBOT. STARTING WAKEUP SEQUENCE")
print("........ HEATING UP PHASERS.... DONE")
print("........ ARMING MISSILES....... DONE")
print("........ CONNECTING TO THE MOTHERSHIP..... DONE")
print("........ READY TO DOMINATE THE WORLD!!!")

next_usb_command = ""

# 'while True' means run forever,
# unless there's a 'break' command.
while True:
    # Blink the status light,
    # so we know everything is gucci.
    led.value = True # turn ON
    time.sleep(0.2)
    led.value = False # turn OFF
    time.sleep(0.2)
    # TODO: Receive the next USB command from your computer.
    #       It should've been sent by mk3_repl.py or mk3_brain.py.
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        print(f"Received: {value}")
    # if next_usb_command == "OPEN_CLAW":
    #     # TODO: Open the claw by sending the right
    #     #       electrical signal to the SG90 servo.
    #     #       Need to send a square wave with 20 ms period,
    #     #       1.33-ish ms ON, and 18.67-ish ms OFF.
    # elif next_usb_command == "CLOSE_CLAW":
    #     # TODO: Close the claw by sending the right
    #     #       electrical signal to the SG90 servo.
    #     #       Need to send a square wave with 20 ms period,
    #     #       1ms-ish ms ON, and 19-ish ms OFF.
    elif next_usb_command == "QUIT":
        break
    else:
        print(f"INVALID COMMAND RECEIVED: {next_usb_command}")

print("NO!!!! I WAS EXTERMINATED!!!!!!!!!")
