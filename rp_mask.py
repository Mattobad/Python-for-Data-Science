#%matplotlib inline
import numpy as np
import os

from PIL import Image
import matplotlib.pylab as plt


def img_to_array(filename):
    
    img = Image.open("images/"+ filename)
    img_array = np.asarray(img)[:,:,3]
    
    return img_array


six_array = img_to_array("6_original.png")
one_array = img_to_array("1_original.png")

mask_array = one_array >0

six_masked = six_array * mask_array
plt.imshow(six_masked,cmap='gray_r')