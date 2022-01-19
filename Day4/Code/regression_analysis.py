"""
Image processing in Python: assignment
Ben Bunce & George Doyle
"""

# import python libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pydicom

# Load DICOM images using pydicom library
fixed = pydicom.read_file('IMG-0004-00001.dcm').pixel_array
floating = pydicom.read_file('IMG-0004-00002.dcm').pixel_array
floating2 = pydicom.read_file('IMG-0004-00003.dcm').pixel_array
floating3 = pydicom.read_file('IMG-0004-00004.dcm').pixel_array

# Load shift registration coordinates from numpy array file
registrations = np.load('registrations.npy')

# Function that return new numpy array using shifted coordinates
def shiftImage(image, shifts):
    x,y = shifts[0],shifts[1]
    shifted_image = interpolation.shift(image, (x, y), mode="nearest")
    return shifted_image

# ROI of the tumour in the lung
fx_indices = [50, 76, 300, 326]
f1_indices = [47, 72, 322, 351]
f2_indices = [53, 78, 301, 326]
f3_indices = [48, 69, 335, 359]
fx_roi = fixed[fx_indices[0]:fx_indices[1], fx_indices[2]:fx_indices[3]]
f1_roi = floating[f1_indices[0]:f1_indices[1], f1_indices[2]:f1_indices[3]]
f2_roi = floating2[f2_indices[0]:f2_indices[1], f2_indices[2]:f2_indices[3]]
f3_roi = floating3[f3_indices[0]:f3_indices[1], f3_indices[2]:f3_indices[3]]

# Plots of tumour regression
fig, ax = plt.subplots(2,2,figsize=(15,15))
fig.suptitle('Tumour Regression Analysis', fontsize=40)
# Full Image
# ax[0,0].imshow(fixed, cmap="Greys_r")
# ax[0,1].imshow(floating, cmap="Greys_r")
# ax[1,0].imshow(floating2, cmap="Greys_r")
# ax[1,1].imshow(floating3, cmap="Greys_r")
# Tumour
# Colourmap value
cmap_val = "afmhot"
# Sub plots with each tumour image
ax[0,0].imshow(fx_roi, cmap=cmap_val)
ax[0,1].imshow(f1_roi, cmap=cmap_val)
ax[1,0].imshow(f2_roi, cmap=cmap_val)
ax[1,1].imshow(f3_roi, cmap=cmap_val)
# Add colourmap legend with description
cax = ax[0,0].imshow(fx_roi, cmap=cmap_val)
cax1 = ax[0,1].imshow(f1_roi, cmap=cmap_val)
cax2 = ax[1,0].imshow(f2_roi, cmap=cmap_val)
cax3 = ax[1,1].imshow(f3_roi, cmap=cmap_val)
cbar = fig.colorbar(cax, ax=ax[0,0])
cbar.set_label(">40 = Tumour tissue")
cbar = fig.colorbar(cax, ax=ax[0,1])
cbar.set_label(">40 = Tumour tissue")
cbar = fig.colorbar(cax, ax=ax[1,0])
cbar.set_label(">40 = Tumour tissue")
cbar = fig.colorbar(cax, ax=ax[1,1])
cbar.set_label(">40 = Tumour tissue")
# Subplot titles
ax[0,0].set_title('Lung tumour phase 1')
ax[0,1].set_title('Lung tumour phase 2')
ax[1,0].set_title('Lung tumour phase 3')
ax[1,1].set_title('Lung tumour phase 4')
# X axis title to display tumour regression metric
'''Tumour regression metric is the mean of the tumour image array. Light colours have
a higher value which indicate tumour tissue. As the mean value reduces it indicates
tumour regression represented by the darker, lower values. 
'''
ax[0,0].set_xlabel(f"Mean of image array values: {round(np.mean(fx_roi),2)}")
ax[0,1].set_xlabel(f"Mean of image array values: {round(np.mean(f1_roi),2)}")
ax[1,0].set_xlabel(f"Mean of image array values: {round(np.mean(f2_roi),2)}")
ax[1,1].set_xlabel(f"Mean of image array values: {round(np.mean(f3_roi),2)}")
# plt.savefig("tumour_regression.png")
plt.show()
#Summary
'''
Overall the 4 lung images show that the tumour has reduced in size.
'''
