import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import pydicom

fixed = pydicom.read_file('IMG-0004-00001.dcm').pixel_array
floating = pydicom.read_file('IMG-0004-00002.dcm').pixel_array
floating2 = pydicom.read_file('IMG-0004-00003.dcm').pixel_array
floating3 = pydicom.read_file('IMG-0004-00004.dcm').pixel_array
floating_list = [floating, floating2, floating3]

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1 = plt.imshow(fixed, cmap="Greys_r")
# ax1 = plt.imshow(floating, alpha=0.25, cmap="Purples_r")
# plt.savefig("image_1_2_overlay.png")
# plt.show()

def shiftImage(image, shifts):
    x,y = shifts[0],shifts[1]
    shifted_image = interpolation.shift(image, (x, y), mode="nearest")
    return shifted_image


# shifted_image = shiftImage(floating, [0,-25])

def costFunction(fixed, floating):
    return np.mean((fixed - floating)**2)

# print(costFunction(fixed, floating))
# print(costFunction(fixed, shifted_image))


def registerImages(shift, fixed, floating):
    shifted_image = shiftImage(floating, shift)
    cost = costFunction(fixed, shifted_image) 
    global low_cost
    low_cost = 100
    if cost < low_cost:
        low_cost = cost
    return costFunction(fixed, shifted_image)

# registering_shift1 = brute(registerImages, ((-5, 5), (-5, 5)), args=(fixed, floating))
# registering_shift2 = brute(registerImages, ((-50, 50), (-50, 50)), args=(fixed, floating))
# registering_shift3 = brute(registerImages, ((-100, 100), (-100, 100)), Ns=20, args=(fixed, floating))
# registering_shift4 = brute(registerImages, ((-200, 200), (-200, 200)), args=(fixed, floating))
# registering_shift_evo = differential_evolution(registerImages, ((-100, 100), (-100,100)), args=(fixed, floating))

# print("Final cost", low_cost)

# print(registering_shift1) #[  3.00046965 -24.99650448]
# print(registering_shift2) #[  3.00393757 -25.00177484]
# print(registering_shift3) #[  2.99566717 -25.00354501]
# print(registering_shift4) #[  2.99495951 -24.99885047]
# print(registering_shift_evo) #[  3.00064562, -25.00657224]

'''Question X
1. Change in the low, high ranges produces the same final cost metric of 0.27736663818359375
but the shift coodinate differ.
2. Changing evaluation point increased the time taken to complete the calculation but has
no impact on the final cost score.
3. Using differential_evolution produced a similar shift, cost score and time taken remained
similar to brute.''' 

# shifted_image = shiftImage(floating, registering_shift3)

# registrations = []
# for floating in floating_list:
#     registering_shift = brute(registerImages, ((-100, 100), (-100, 100)), Ns=20, args=(fixed, floating))
#     registrations.append(registering_shift)

# registrations_arr = np.array(registrations)
# np.save("registrations.npy", registrations_arr)

registrations = np.load("registrations.npy")
shifted_list = [shiftImage(image, shift) for image, shift in zip(floating_list, registrations)]

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1 = plt.imshow(fixed, cmap="Greys_r")
# ax1 = plt.imshow(shifted_image, alpha=0.25, cmap="Purples_r")
# plt.show()
