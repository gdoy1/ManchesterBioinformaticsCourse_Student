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

# Function to modify window and level of lung image
def yourfunction(window, level):
    # create figure and subplots
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    # add lung image
    ax.imshow(cropped, interpolation="none", cmap="Greys_r", vmin=(level-window)/2, vmax=(level+window)/2)
    # add histogram
    ax2.hist(cropped.flatten())
    # set figure text
    plt.figtext(0.5, 0.01, "vmin: " + str(window) + ". vmax: " + str(level), fontsize=10,
                ha="center", bbox={"facecolor": "grey", "alpha": 0.5, "pad": 5})
    plt.show()

# Tested function with different window/level parameters
yourfunction(0.01, 1)
yourfunction(0.4, 1)
yourfunction(0.6, 0.8)
yourfunction(0.3, 0.7)
yourfunction(1, 1)
yourfunction(1, 0.2)