import board
import digitalio
import time
import pwmio
import supervisor
from adafruit_motor import servo

# All our variables....
red_led = digitalio.DigitalInOut(board.D13)
red_led.direction = digitalio.Direction.OUTPUT
blink_red_led = True

# 4 servos - 2 share a pin because there's only 3 PWM pins.
# Claw and Shoulder
pin_claw_and_shoulder = board.A1
pwm_claw_and_shoulder = pwmio.PWMOut(
    pin_claw_and_shoulder,
    duty_cycle=2**15, 
    frequency=50, 
    variable_frequency=False
)
claw_and_shoulder = servo.Servo(pwm_claw_and_shoulder)
# Elbow
pin_elbow = board.A2
pwm_elbow = pwmio.PWMOut(
    pin_elbow,
    duty_cycle=2**15, 
    frequency=50, 
    variable_frequency=False
)
elbow = servo.Servo(pwm_elbow)
# Retractor
pin_retractor = board.A3
pwm_retractor = pwmio.PWMOut(
    pin_retractor,
    duty_cycle=2**15, 
    frequency=50, 
    variable_frequency=False
)
retractor = servo.Servo(pwm_retractor)
# Servo to move
servo_to_move = None

# The next action to perform
next_action = None

# Servo angles, we only use increments of 5 degrees
servo_angles = list(range(0, 180, 5))
servo_angles_index = 0

print("I AM ROBOT. STARTING WAKEUP SEQUENCE")
print("........ HEATING UP PHASERS.... DONE")
print("........ ARMING MISSILES....... DONE")
print("........ CONNECTING TO THE MOTHERSHIP..... DONE")
print("........ READY TO DOMINATE THE WORLD!!!")

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
    if next_action == "START_OPEN_CLAW":
        # TODO: Open the claw by sending the right
        #       electrical signal to the SG90 servo.
        #       Need to send a square wave with 20 ms period,
        #       1.33-ish ms ON, and 18.67-ish ms OFF.
        servo_to_move = "claw_and_shoulder"
        next_action = None
    elif next_action == "STOP_CLOSE_CLAW":
        # TODO: Close the claw by sending the right
        #       electrical signal to the SG90 servo.
        #       Need to send a square wave with 20 ms period,
        #       1ms-ish ms ON, and 19-ish ms OFF.
        servo_to_move = None
        next_action = None
    elif next_action == "RED_OFF":
        blink_red_led = False
    elif next_action == "RED_ON":
        blink_red_led = True
    elif next_action == "TERMINATE":
        break
    elif next_action != "":
        print("INVALID COMMAND RECEIVED: " + next_action)
    
    # Move the servo
    if servo_to_move == "claw_and_shoulder":
        servo_angle = servo_angles[servo_angles_index]
        servo_angles_index = servo_angles_index + 1
        servo_angles_index = servo_angles_index % len(servo_angles)
        claw_and_shoulder.angle = servo_angle
        time.sleep(0.2) # give it enough time to get there

print("NO!!!! I WAS EXTERMINATED!!!!!!!!!")

# import time
# import board
# import pwmio
# from adafruit_motor import servo
# pwm_pins = [
#     board.A2, # index 0
#     board.A3, # index 1
#     board.A1, # index 2
#     # board.A7 # TODO: This pin unfortunately doesn't work due to a timer conflict, so only 3 PWM pins are available :,-(
#                #       See https://github.com/adafruit/circuitpython/issues/1838
# ]
# pwm_pin_index = 0
# while True:
#     # Get the PWM pin for the servo we want to control
#     servo_to_move_pwm_pin = pwm_pins[pwm_pin_index]
#     # Create a PWM signal for the servo
#     servo_to_move_pwm = pwmio.PWMOut(servo_to_move_pwm_pin, duty_cycle=2**15, frequency=50, variable_frequency=False)
#     # Create a servo object to control its angle
#     servo_to_move = servo.Servo(servo_to_move_pwm)
#     # Move the servo the full range
#     for angle in range(0, 180, 5):  # 0 - 180 degrees, 15 degrees at a time.
#         servo_to_move.angle = angle
#         time.sleep(0.05)
#     for angle in range(180, 0, -5): # 180 - 0 degrees, 15 degrees at a time.
#         servo_to_move.angle = angle
#         time.sleep(0.05)
#     pwm_pin_index = pwm_pin_index + 1
#     pwm_pin_index = pwm_pin_index % len(pwm_pins)
#     servo_to_move_pwm.deinit()
