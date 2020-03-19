import tensorflow as tf 
import numpy as np

# creating the tensors
path_train = 'C:\\Users\\bulzg\\Desktop\\train'
path_valid = 'C:\\Users\\bulzg\\Desktop\\test'

train_batches = tf.keras.preprocessing.image.ImageDataGenerator().flow_from_directory(path_train, target_size=(224,224), classes=['real', 'picture'], batch_size=500)
valid_batches = tf.keras.preprocessing.image.ImageDataGenerator().flow_from_directory(path_valid, target_size=(224,224), classes=['real', 'picture'], batch_size=2)


model = tf.keras.models.load_model('trained_goh_model.h5')

prediction = model.predict_generator(valid_batches, steps=1, verbose=0)

ratio=0

for _ in range(25):
    batch = next(valid_batches)
    prediction = model.predict_on_batch(batch)
    for i in range(20):
        # get index of the higher predition probability
        prediction_index = (np.where(prediction[i] == np.amax(prediction[i]))[0] == 0)
        # get batch labeling
        label = batch[1] 
        real_index = (label[i][0] == 1)

        if(prediction_index == real_index):
            ratio = ratio + 1

print(ratio/500)
