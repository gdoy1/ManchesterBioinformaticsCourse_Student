"""
Image processing in Python: assignment
Ben Bunce & George Doyle
"""

# import python libraries
from curses import reset_shell_mode
import sys
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from scipy.ndimage import interpolation, rotate

# load image using skimage library
lungs = imread('lungs.jpg', as_gray=True)  
lungs2 = imread('lungs2.jpg', as_gray=True) 
lungs3 = imread('lungs3.jpg', as_gray=True) 


# Function to shift x, y coordinates of image
def shiftImage(shifts):

    # unpacks shifts input argument into x and y
    x,y = shifts[0],shifts[1]

    # set global so that function modifies image outside of scope
    global lungs2

    # set new variable that shift lungs2 image using x, y parameters
    shifted_image = interpolation.shift(lungs2, (x, y), mode="nearest")

    # show both original image and floating with transparency
    plt.imshow(lungs, cmap="Greys_r")
    plt.imshow(shifted_image, alpha=0.25, cmap="Greys_r")
    plt.show()


# Function to shift and rotate lungs3
def rotateImage(shifts, rotation):

    # unpacks shifts input argument into x and y
    x,y = shifts[0],shifts[1]

    # set global so that function modifies image outside of scope
    global lungs3

    # set new variable that shift lungs3 image using x, y parameters
    image = interpolation.shift(lungs3, (x, y), mode="nearest")
    # rotate shifted image
    image = rotate(image, rotation, reshape=False, mode='wrap')

    # function returns plot objects
    return(
        plt.imshow(lungs, cmap="Greys_r"),
        plt.imshow(image, alpha=0.25, cmap="Purples_r"))


# Function to allow user to interactively move floating image using x, y and rotation
def on_press(event):
    # Prints the key the user pressed
    print('moved', event.key)
    # “flush” the buffer - write everything in the buffer to the terminal
    sys.stdout.flush()
    # set global so that function modifies image outside of scope
    global x, y, rotation
    # if statements to identify user inputs and adjust the x, y or rotation variable accordingly
    if event.key == 'up':
        y-=5
        rotateImage([y,x],rotation)
    if event.key == 'down':
        y+=5
        rotateImage([y,x],rotation)
    if event.key == 'left':
        x-=5
        rotateImage([y,x],rotation)
    if event.key == 'right':
        x+=5
        rotateImage([y,x],rotation)
    if event.key == 'pageup':
        rotation+=1
        rotateImage([y,x],rotation)
    if event.key == 'pagedown':
        rotation-=1
        rotateImage([y,x],rotation)

    # print the current x, y and rotation coordinates
    print(f"X={x}, Y={y}, Rotation={rotation}")
    # update figure
    fig.canvas.draw()


# Coordinates required to align through trial and error
# shiftImage([-15,-40])  

# Coordinates required for both rotation and alignment through trial and error
# rotateImage([-20,-50], -3)

# Coordinates required for both rotation and alignment through shift/rotation function
# rotateImage([-35,-5], -3)

# set figure
fig, ax = plt.subplots()
# connecting event handler function to figure
fig.canvas.mpl_connect('key_press_event', on_press)
# set default x, y and rotation values
x, y, rotation = 0, 0, 0
# call rotation function which return image object to display
ax = rotateImage([0,0], 0)
plt.show()