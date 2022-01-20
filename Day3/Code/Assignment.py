"""
Image processing in Python: assignment
Ben Bunce & George Doyle
"""

# import python libraries
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread

# load image using skimage library and set image to grayscale
image = imread('lungs.jpg', as_gray=True)
# cropped the image to remove black border
cropped = image[90:480,140:480]
# display lung image
plt.imshow(cropped)
plt.show()

# Flatten cropped image array so that it can be plotted as a histogram
flat = cropped.flatten()
# display histogram
plt.hist(flat)
plt.show()

'''
Q5 - Histogram displays level of black/white in the grayscale image. A value of 0 correlates with black, whilst 1
correlates to white. The intervening values between 0 and 1 represent grayscale colouring.
'''

# Function to modify window and level of lung image
def adjustwindowlevel(window, level):
    # create figure and subplots
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    # add lung image
    ax.imshow(cropped, interpolation="none", cmap="Greys_r", vmin=(level-window)/2, vmax=(level+window)/2)
    # save modified lung image into a temporary jpg
    plt.imsave('lung_temp.jpg', cropped, cmap="Greys_r", vmin=(level-window)/2, vmax=(level+window)/2)
    # load the modified window/level lung into histo variable
    histo = imread('lung_temp.jpg', as_gray=True)
    # add histogram using adjusted image
    ax2.hist(histo.flatten())
    # set figure text
    plt.figtext(0.5, 0.01, "vmin: " + str(window) + ". vmax: " + str(level), fontsize=10,
                ha="center", bbox={"facecolor": "grey", "alpha": 0.5, "pad": 5})
    plt.show()

# Tested function with different window/level parameters
adjustwindowlevel(0.01, 1)
adjustwindowlevel(0.4, 1)
adjustwindowlevel(0.6, 0.8)
adjustwindowlevel(0.3, 0.7)
adjustwindowlevel(1, 1)
adjustwindowlevel(1, 0.2)