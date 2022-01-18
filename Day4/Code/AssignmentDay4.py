import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import pydicom

image1 = pydicom.read_file('IMG-0004-00001.dcm').pixel_array
image2 = pydicom.read_file('IMG-0004-00002.dcm').pixel_array

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1 = plt.imshow(image1, cmap="Greys_r")
ax1 = plt.imshow(image2, alpha=0.25, cmap="Purples_r")
# plt.savefig("image_1_2_overlay.png")
plt.show()

def shiftImage(image, shifts):
    x,y = shifts[0],shifts[1]
    shifted_image = interpolation.shift(image, (x, y), mode="nearest")
    return shifted_image


shifted_image = shiftImage(image2, [0,-25])

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1 = plt.imshow(image1, cmap="Greys_r")
ax1 = plt.imshow(shifted_image, alpha=0.25, cmap="Purples_r")
# plt.savefig("image_1_2_overlay.png")
plt.show()