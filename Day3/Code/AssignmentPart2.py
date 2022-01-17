"""
Image processing in Python: assignment
Ben Bunce & George Doyle
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy
from skimage.io import imread
from scipy.ndimage import interpolation, rotate

lungs = imread('lungs.jpg', as_gray=True)  # load image into skimage
lungs2 = imread('lungs2.jpg', as_gray=True)  # load image into skimage
lungs3 = imread('lungs3.jpg', as_gray=True)  # load image into skimage

'''plt.imshow(lungs)
plt.imshow(lungs2)
plt.show()'''

'''plt.imshow(lungs, cmap="Greys_r")
plt.imshow(lungs2, alpha=0.25, cmap="Greys_r")
plt.show()'''

def shiftImage(shifts):

    x,y = shifts[0],shifts[1]

    global lungs
    global lungs2

    shifted_image = interpolation.shift(lungs2, (x, y), mode="nearest")


    plt.imshow(lungs, cmap="Greys_r")
    plt.imshow(shifted_image, alpha=0.25, cmap="Greys_r")
    plt.show()

    # floating.set_data(lungs2)
    # fig.canvas.draw()

# shiftImage([-10,-20])
# shiftImage([-15,-40])  #Coordinates required to align

def rotateImage(shifts, rotation):

    x,y = shifts[0],shifts[1]

    global lungs
    global lungs3

    shifted_image = interpolation.shift(lungs3, (x, y), mode="nearest")
    rotated_image = scipy.ndimage.interpolation.rotate(
            input=shifted_image,
            angle=rotation)


    plt.imshow(lungs, cmap="Greys_r")
    plt.imshow(rotated_image, alpha=0.25, cmap="Greys_r")
    plt.show()

    # floating.set_data(lungs2)
    # fig.canvas.draw()

rotateImage([0,0], 0)
rotateImage([-20,-50], -3)  # Coordinates required for both rotation and alignment



