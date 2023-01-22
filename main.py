import random
import os
import shutil
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, Dropout
from sklearn.metrics import accuracy_score
from draw_image_using_pillow import Draw_Geometrical_Shapes

# Create a directory to save the images
directory_name = "geometrical_shapes_using_pillow"

# check if the directory exists
if os.path.exists(directory_name):
    # delete the directory
    shutil.rmtree(directory_name)
    print(f"{directory_name} Deleted!")

# create the new directory
os.makedirs(directory_name+"/train/circle_images")
os.makedirs(directory_name+"/train/no_circle_images")
os.makedirs(directory_name+"/validation/circle_images")
os.makedirs(directory_name+"/validation/no_circle_images")
os.makedirs(directory_name+"/test/circle_images")
os.makedirs(directory_name+"/test/no_circle_images")
print(f"{directory_name} Created!")

# Generate images using pillow

for i in range(800):
    # create an instance of Draw_Geometrical_Shapes
    drawing = Draw_Geometrical_Shapes(resolution_image=(100, 100), background_color=(0, 0, 0))

    # create a list of objects of the methods that includes circle
    methods_list = [drawing.conics, drawing.quadrilateral, drawing.line, drawing.polygon]
    # shuffle the list of methods
    random.shuffle(methods_list)
    # iterate through the shuffled list
    for method in methods_list:
        method()
        if method == drawing.conics:
            break

    #drawing.image.show()
    # Save the image as a PNG file
    drawing.image.save(f"geometrical_shapes_using_pillow/train/circle_images/circle_{str(i+1)}.png")

for i in range(800):
    # create an instance of Draw_Geometrical_Shapes
    drawing = Draw_Geometrical_Shapes(resolution_image=(100, 100), background_color=(0, 0, 0))

    # create a list of objects of the methods that includes circle
    methods_list = [drawing.conics, drawing.quadrilateral, drawing.line, drawing.polygon]
    # shuffle the list of methods
    random.shuffle(methods_list)
    # iterate through the shuffled list
    for method in methods_list:
        if method == drawing.conics:
            break
        else:
            method()

    #drawing.image.show()
    # Save the image as a PNG file
    drawing.image.save(f"geometrical_shapes_using_pillow/train/no_circle_images/no_circle_{str(i+1)}.png")

for i in range(200):
    # create an instance of Draw_Geometrical_Shapes
    drawing = Draw_Geometrical_Shapes(resolution_image=(100, 100), background_color=(0, 0, 0))

    # create a list of objects of the methods that includes circle
    methods_list = [drawing.conics, drawing.quadrilateral, drawing.line, drawing.polygon]
    # shuffle the list of methods
    random.shuffle(methods_list)
    # iterate through the shuffled list
    for method in methods_list:
        method()
        if method == drawing.conics:
            break

    # drawing.image.show()
    # Save the image as a PNG file
    drawing.image.save(f"geometrical_shapes_using_pillow/validation/circle_images/circle_{str(i + 1)}.png")

for i in range(200):
    # create an instance of Draw_Geometrical_Shapes
    drawing = Draw_Geometrical_Shapes(resolution_image=(100, 100), background_color=(0, 0, 0))

    # create a list of objects of the methods that includes circle
    methods_list = [drawing.conics, drawing.quadrilateral, drawing.line, drawing.polygon]
    # shuffle the list of methods
    random.shuffle(methods_list)
    # iterate through the shuffled list
    for method in methods_list:
        if method == drawing.conics:
            break
        else:
            method()

    # drawing.image.show()
    # Save the image as a PNG file
    drawing.image.save(f"geometrical_shapes_using_pillow/validation/no_circle_images/no_circle_{str(i + 1)}.png")

for i in range(100):
    # create an instance of Draw_Geometrical_Shapes
    drawing = Draw_Geometrical_Shapes(resolution_image=(100, 100), background_color=(0, 0, 0))

    # create a list of objects of the methods that includes circle
    methods_list = [drawing.conics, drawing.quadrilateral, drawing.line, drawing.polygon]
    # shuffle the list of methods
    random.shuffle(methods_list)
    # iterate through the shuffled list
    for method in methods_list:
        method()
        if method == drawing.conics:
            break

    #drawing.image.show()
    # Save the image as a PNG file
    drawing.image.save(f"geometrical_shapes_using_pillow/test/circle_images/circle_{str(i+1)}.png")

for i in range(100):
    # create an instance of Draw_Geometrical_Shapes
    drawing = Draw_Geometrical_Shapes(resolution_image=(100, 100), background_color=(0, 0, 0))

    # create a list of objects of the methods that includes circle
    methods_list = [drawing.conics, drawing.quadrilateral, drawing.line, drawing.polygon]
    # shuffle the list of methods
    random.shuffle(methods_list)
    # iterate through the shuffled list
    for method in methods_list:
        if method == drawing.conics:
            break
        else:
            method()

    #drawing.image.show()
    # Save the image as a PNG file
    drawing.image.save(f"geometrical_shapes_using_pillow/test/no_circle_images/no_circle_{str(i+1)}.png")

# Create an ImageDataGenerator object
datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale = 1./255)

# Create a generator to read images from the training directory
batch_size_train = 32
train_generator = datagen.flow_from_directory(
        'geometrical_shapes_using_pillow/train',  # This is the source directory for training images
        target_size=(100, 100),  # All images will be resized to 150x150
        batch_size=batch_size_train,
        class_mode='categorical')  # Since we use categorical_crossentropy loss, we need categorical labels

# Create a generator to read images from the validation directory
batch_size_val = 8
validation_generator = datagen.flow_from_directory(
        'geometrical_shapes_using_pillow/validation',
        target_size=(100, 100),
        batch_size=batch_size_val,
        class_mode='categorical')

test_generator = datagen.flow_from_directory(
        'geometrical_shapes_using_pillow/test',  # This is the source directory for training images
        target_size=(100, 100),  # All images will be resized to 150x150
        class_mode='categorical')  # Since we use categorical_crossentropy loss, we need categorical labels

# Create a simple model
model = Sequential()
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(Dropout(0.2))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(Dropout(0.2))
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(Dropout(0.2))
model.add(Conv2D(8, kernel_size=(3, 3), activation='relu'))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit_generator(
        train_generator,
        steps_per_epoch=len(train_generator.classes)/batch_size_train,
        epochs=5,
        validation_data=validation_generator,
        validation_steps=len(validation_generator.classes)/batch_size_val)

y_predict = model.predict(test_generator)

accuracy = accuracy_score(test_generator.labels, y_predict)
print("Test accuracy: {:.2f}%".format(accuracy*100))