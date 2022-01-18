"""
Image processing in Python: assignment
Ben Bunce & George Doyle
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy
from skimage.io import imread
from scipy.ndimage import interpolation, rotate

lungs = imread('lungs.jpg', as_gray=True)  # load image into skimage
lungs2 = imread('lungs2.jpg', as_gray=True)  # load image into skimage
lungs3 = imread('lungs3.jpg', as_gray=True)  # load image into skimage


def shiftImage(shifts):

    x,y = shifts[0],shifts[1]

    global lungs
    global lungs2

    shifted_image = interpolation.shift(lungs2, (x, y), mode="nearest")

    plt.imshow(lungs, cmap="Greys_r")
    plt.imshow(shifted_image, alpha=0.25, cmap="Greys_r")
    plt.show()


def rotateImage(shifts, rotation):

    x,y = shifts[0],shifts[1]

    global lungs
    global lungs3

    shifted_image = interpolation.shift(lungs3, (x, y), mode="nearest")
    rotated_image = scipy.ndimage.interpolation.rotate(
            input=shifted_image,
            angle=rotation)


    return(plt.imshow(lungs, cmap="Greys_r"),
    plt.imshow(rotated_image, alpha=0.25, cmap="Greys_r"))

    plt.show()


def on_press(event):
    print('moved', event.key)
    sys.stdout.flush()
    global x, y, turn
    if event.key == 'up':
        y+=5
        rotateImage([y,0],0)
    if event.key == 'down':
        y-=5
        rotateImage([y,0],0)
    if event.key == 'left':
        x+=5
        rotateImage([0,x],0)
    if event.key == 'right':
        x-=5
        rotateImage([0,x],0)
    if event.key == 'pageup':
        turn+=3
        rotateImage([x,y],turn)
    if event.key == 'pagedown':
        turn-+3
        rotateImage([x,y],turn)

    fig.canvas.draw()

# shiftImage([-10,-20])
# shiftImage([-15,-40])  # Coordinates required to align

# rotateImage([0,0], 0)
# rotateImage([-20,-50], -3)  # Coordinates required for both rotation and alignment

fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', on_press)

x, y, turn = 0, 0, 0
ax = rotateImage([0,0], 0)
# xl = ax.set_xlabel('easy come, easy go')
# ax.set_title('Press a key')
plt.show()