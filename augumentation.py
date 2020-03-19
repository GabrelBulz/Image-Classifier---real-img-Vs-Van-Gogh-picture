import tensorflow as tf 
import PIL
import numpy as np 
import os
import scipy.misc
from matplotlib.pyplot import imread
from matplotlib.image import imsave


img_path = 'C:\\Users\\bulzg\\Desktop\\train\\real'
save_path='C:\\Users\\bulzg\\Desktop\\train\\test\\'


generator = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=10,width_shift_range=0.1,
                                                            height_shift_range=0.1,shear_range=0.15,
                                                            zoom_range=0.1,channel_shift_range=10,
                                                            horizontal_flip=True)

name_imgs = os.listdir(img_path)

for i in name_imgs:
    index_img = name_imgs.index(i)
    img = imread(img_path + '\\' + i)
    img = np.expand_dims(img,0)
    # print(np.shape(img))
    augumented_iter = generator.flow(img)

    augumented_images = [next(augumented_iter)[0].astype(np.uint8) for i in range(10)]
 
    cont=0
    for resulted_img in augumented_images:
        imsave(save_path + str(index_img) + str(cont) + '.jpg', resulted_img)
        cont = cont + 1


