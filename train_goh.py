import tensorflow as tf 
import numpy as np

# creating the tensors
path_train = 'C:\\Users\\bulzg\\Desktop\\train'
path_valid = 'C:\\Users\\bulzg\\Desktop\\test'

train_batches = tf.keras.preprocessing.image.ImageDataGenerator().flow_from_directory(path_train, target_size=(224,224), classes=['real', 'picture'], batch_size=10)
valid_batches = tf.keras.preprocessing.image.ImageDataGenerator().flow_from_directory(path_valid, target_size=(224,224), classes=['real', 'picture'], batch_size=10)

# build a fine tuned bgg16 model

vgg_model = tf.keras.applications.vgg16.VGG16()

# copy vgg into out model 
model = tf.keras.Sequential()
for layer in vgg_model.layers:
    model.add(layer)
    
# delete the last layer to be able to put our new 2 choise dense layer 
model.layers.pop()

for layer in model.layers:
    layer.trainable = False

# add our new dense layer 
model.add(tf.keras.layers.Dense(2, activation='softmax'))

model.compile(tf.keras.optimizers.Adam(lr=.0001), loss = tf.keras.losses.CategoricalCrossentropy(), metrics=['accuracy'])

model.fit_generator(train_batches, steps_per_epoch=160, validation_data=valid_batches, validation_steps=160, verbose=1, epochs=10)

model.save('trained_goh_model.h5')

