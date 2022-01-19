"""
Image processing in Python: assignment
Ben Bunce & George Doyle
"""

# import python libraries
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import pydicom

# Load DICOM images using pydicom library
fixed = pydicom.read_file('IMG-0004-00001.dcm').pixel_array
floating = pydicom.read_file('IMG-0004-00002.dcm').pixel_array
floating2 = pydicom.read_file('IMG-0004-00003.dcm').pixel_array
floating3 = pydicom.read_file('IMG-0004-00004.dcm').pixel_array
# Add DICOM images to list to enable iteration
floating_list = [floating, floating2, floating3]

# Generate and save fixed and floating image as .png
'''
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1 = plt.imshow(fixed, cmap="Greys_r")
# ax1 = plt.imshow(floating, alpha=0.25, cmap="Purples_r")
# plt.savefig("image_1_2_overlay.png")
# plt.show()
'''

# Function to shift x, y coordinates and return image array
def shiftImage(image, shifts):
    x,y = shifts[0],shifts[1]
    shifted_image = interpolation.shift(image, (x, y), mode="nearest")
    return shifted_image


# Function to calculate cost between fixed and floating
# Cost value used to determine similarity between images
def costFunction(fixed, floating):
    return np.mean((fixed - floating)**2)

# Function to return cost function after adjusting floating image using shift coordinates
# Used in scipy.optimiser function to allow algorithm to repeating test different shift coordinates
def registerImages(shift, fixed, floating):
    # Call shift function to get new image
    shifted_image = shiftImage(floating, shift)
    # Testing purposes to display lowest cost value after optimisation
    '''cost = costFunction(fixed, shifted_image) 
    global low_cost
    low_cost = 100
    if cost < low_cost:
        low_cost = cost'''
    # return cost value
    return costFunction(fixed, shifted_image)

# print("Final cost", low_cost)

# Testing affect of changing ranges, Ns and optimisation methods
'''
# registering_shift1 = brute(registerImages, ((-5, 5), (-5, 5)), args=(fixed, floating))
# registering_shift2 = brute(registerImages, ((-50, 50), (-50, 50)), args=(fixed, floating))
# registering_shift3 = brute(registerImages, ((-100, 100), (-100, 100)), Ns=20, args=(fixed, floating))
# registering_shift4 = brute(registerImages, ((-200, 200), (-200, 200)), args=(fixed, floating))
# registering_shift_evo = differential_evolution(registerImages, ((-100, 100), (-100,100)), args=(fixed, floating))
'''

# Record of optimal shift coordinates
'''
# print(registering_shift1) #[  3.00046965 -24.99650448]
# print(registering_shift2) #[  3.00393757 -25.00177484]
# print(registering_shift3) #[  2.99566717 -25.00354501]
# print(registering_shift4) #[  2.99495951 -24.99885047]
# print(registering_shift_evo) #[  3.00064562, -25.00657224]
'''

# Question X
'''
1. Change in the low, high ranges produces the same final cost metric of 0.27736663818359375
but the shift coodinate differ.
2. Changing evaluation point increased the time taken to complete the calculation but has
no impact on the final cost score.
3. Using differential_evolution produced a similar shift, cost score and time taken remained
similar to brute.''' 

# Generate and save registration array from brute optimiser as registration.npy file
registrations = []
for floating in floating_list:
    registering_shift = brute(registerImages, ((-100, 100), (-100, 100)), Ns=20, args=(fixed, floating))
    registrations.append(registering_shift)

registrations_arr = np.array(registrations)
np.save("registrations.npy", registrations_arr)

# Load registration.npy file
registrations = np.load("registrations.npy")
# Create list of shifted images that match based on brute optimiser registrations
shifted_list = [shiftImage(image, shift) for image, shift in zip(floating_list, registrations)]
