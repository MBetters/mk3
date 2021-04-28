# Purposes:
# - Detect if the claw is ABOVE the soda can
# - If it's not, say whether the claw needs to go LEFT or RIGHT
#   in order to be above the soda can.

# Tests:
# - mk3_camera_test1.png : It's ABOVE
# - mk3_camera_test2.png : NOT ABOVE. Go RIGHT.
# - mk3_camera_test3.png : NOT ABOVE. Go LEFT.

from PIL import Image
import numpy

claw_color = [0, 255, 0] # green claw
soda_can_color = [255, 165, 0] # Fanta soda can

def get_image_data(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values, width, height

image, width, height = get_image_data("mk3_camera_test1.png")
print(f"This should be white: {image[0][0]}")

# Search for green pixel
stop_searching = False
for i in range(0, width):
    for j in range(0, height):
        if image[i][j][0] == 0 and image[i][j][2]: # red 0 and blue 0 == greenish
            print(f"This should be green: {image[i][j]} at ({i}, {j})")
            stop_searching = True
            break # break out of the inner for-loop
    if stop_searching:
        break # break out of the outer for-loop
