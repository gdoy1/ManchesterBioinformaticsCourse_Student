"""
Image processing in Python: assignment
Ben Bunce & George Doyle
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread

image = imread('lungs.jpg', as_gray=True)  # load image into skimage
cropped = image[90:480,140:480]
plt.imshow(cropped)
plt.show()


'''fig = plt.figure()
ax = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax.imshow(image, interpolation="none", cmap="Greys_r", vmin=0.0, vmax=0.2)
ax2.hist(image.flatten(), bins=255, facecolor="Red", edgecolor="Black")
plt.show()'''

# Step 4 - Show histogram
flat = cropped.flatten()
plt.hist(flat)
plt.show()

# Step 5 - Various plots with histogram and labelling
def yourfunction(window, level):
    '''plt.imshow(cropped, interpolation="none", cmap="Greys_r", vmin=window, vmax=level)
    plt.show()'''
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax.imshow(cropped, interpolation="none", cmap="Greys_r", vmin=(level-window)/2, vmax=(level+window)/2)
    ax2.hist(cropped.flatten())
    plt.figtext(0.5, 0.01, "vmin: " + str(window) + ". vmax: " + str(level), fontsize=10,
                ha="center", bbox={"facecolor": "grey", "alpha": 0.5, "pad": 5})
    plt.show()

yourfunction(0.01, 1)
yourfunction(0.4, 1)
yourfunction(0.6, 0.8)
yourfunction(0.3, 0.7)
yourfunction(1, 1)
yourfunction(1, 0.2)