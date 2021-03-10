import board
import digitalio
import time
import supervisor

red_led = digitalio.DigitalInOut(board.D13)
red_led.direction = digitalio.Direction.OUTPUT
blink_red_led = True

print("I AM ROBOT. STARTING WAKEUP SEQUENCE")
print("........ HEATING UP PHASERS.... DONE")
print("........ ARMING MISSILES....... DONE")
print("........ CONNECTING TO THE MOTHERSHIP..... DONE")
print("........ READY TO DOMINATE THE WORLD!!!")

next_action = ""

# 'while True' means run forever,
# unless there's a 'break' command
while True:
    # Blink the status light,
    # so we know everything is gucci.
    if blink_red_led:
        red_led.value = True # turn on the red LED
        time.sleep(0.02)
        red_led.value = False # turn off the red LED
        time.sleep(0.02)
    if supervisor.runtime.serial_bytes_available:
        usb_message = input().strip()
        print("Received USB Message: " + usb_message)
        next_action = usb_message
    # if next_action == "OPEN_CLAW":
    #     # TODO: Open the claw by sending the right
    #     #       electrical signal to the SG90 servo.
    #     #       Need to send a square wave with 20 ms period,
    #     #       1.33-ish ms ON, and 18.67-ish ms OFF.
    # elif next_action == "CLOSE_CLAW":
    #     # TODO: Close the claw by sending the right
    #     #       electrical signal to the SG90 servo.
    #     #       Need to send a square wave with 20 ms period,
    #     #       1ms-ish ms ON, and 19-ish ms OFF.
    elif next_action == "RED_OFF":
        blink_red_led = False
    elif next_action == "RED_ON":
        blink_red_led = True
    elif next_action == "TERMINATE":
        break
    elif next_action != "":
        print("INVALID COMMAND RECEIVED: " + next_action)

print("NO!!!! I WAS EXTERMINATED!!!!!!!!!")
