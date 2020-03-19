# Image-Classifier---real-img-Vs-Van-Gogh-picture
Image Classifier - real images and Van Gogh's paintings

Classification between real images and paintings can be
dificult because there are similar traits and features
in both cases like, human faces, landscapes and different 
real word objects.

One approach will be to focus on some small traits, found
in paintings, such as brush strokers and color blending.

I chosed to start with an already trained MODEL VGG16
VGG16 is a model trained to identify different features
on different layers ... starting from edge detection
to simple shapes, to more complex features like being
able to identify face features.

After the model was chosed we had to fine tune it
by removing the last layer and replacing it with
a dense layer of size 2 ... which would classify
our prediction in 2 different classes :
    1.IS THE IMAGE REAL
    2.IS IS A PAINTING
    
We than gadered all the van gogh paintings from
a csv file containg the links that can be found on kaggle:
https://www.kaggle.com/gfolego/vangogh.

We got a total of 172 paitings and we gathered the same
amount of pictures from real word with common elements
such as people feces, landscapes and so.
The image set was too small to train the 
network so we augumented the images
resunting into a total of 1650 pictures
and 1650 paintings.
The images were downscaled to 224x224 to
reduce the computing time and to better fit to our model

The optimizer used was Adam Optimiser with a step
of 0.0001 and with CategoricalCrossentropy as loss.

After some testing we found the the optimum was accuired 
in the range of 12-15 epochs with a batch size of 10
and 160 setps per epoch

The validation, test and training sets were separated,
and after the final test we found that our model 
has an accuracy of 85%.
