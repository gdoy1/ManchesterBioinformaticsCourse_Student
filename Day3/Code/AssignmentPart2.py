"""
Image processing in Python: assignment
Ben Bunce & George Doyle
"""

from curses import reset_shell_mode
import sys
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from scipy.ndimage import interpolation, rotate

lungs = imread('lungs.jpg', as_gray=True)  # load image into skimage
lungs2 = imread('lungs2.jpg', as_gray=True)  # load image into skimage
lungs3 = imread('lungs3.jpg', as_gray=True)  # load image into skimage


def shiftImage(shifts):

    x,y = shifts[0],shifts[1]

    global lungs2

    shifted_image = interpolation.shift(lungs2, (x, y), mode="nearest")

    plt.imshow(lungs, cmap="Greys_r")
    plt.imshow(shifted_image, alpha=0.25, cmap="Greys_r")
    plt.show()


def rotateImage(shifts, rotation):

    x,y = shifts[0],shifts[1]

    global lungs3

    image = interpolation.shift(lungs3, (x, y), mode="nearest")
    image = rotate(image, rotation, reshape=False, mode='wrap')


    return(
        plt.imshow(lungs, cmap="Greys_r"),
        plt.imshow(image, alpha=0.25, cmap="Purples_r"))



def on_press(event):
    print('moved', event.key)
    sys.stdout.flush()
    global x, y, rotation
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

    print(f"X={x}, Y={y}, Rotation={rotation}")
    fig.canvas.draw()

# shiftImage([-10,-20])
# shiftImage([-15,-40])  # Coordinates required to align

# Coordinates required for both rotation and alignment through trial and error
# rotateImage([-20,-50], -3)
# Coordinates required for both rotation and alignment through shift/rotation function
# rotateImage([-35,-5], -3)


fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', on_press)
x, y, rotation = 0, 0, 0
ax = rotateImage([0,0], 0)
plt.show()