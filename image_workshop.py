#%matplotlib inline
import numpy as np
import os

from PIL import Image
import matplotlib.pylab as plt


def img_to_array(filename):
    
    img = Image.open("images/"+ filename)
    img_array = np.asarray(img)[:,:,3]
    
    return img_array


filelist = os.listdir('images')
filtered_list =[i for i in filelist if "original" in i]

#combine_img_array = np.empty()
for i, file in enumerate(filtered_list):
    img_array = img_to_array(file)
    if i==0:
        combine_img_array = img_array
    else:
        combine_img_array = np.hstack((combine_img_array,img_array))
#np.random.randint(0,99,[5,5])
plt.imshow(combine_img_array,cmap='gray_r')


