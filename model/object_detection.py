import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten

class GeometricalShapesDetectionModel:
    def __init__(self):
        # Create an ImageDataGenerator object
        self.datagen = tf.keras.preprocessing.image.ImageDataGenerator()

        # Define batch sizes for train and validation generators
        self.batch_size_train = 32
        self.batch_size_val = 8

        # Create a generator to read images from the training directory
        self.train_generator = self.datagen.flow_from_directory(
            '../image_generator/geometrical_shapes_using_pillow/Training',
            target_size=(100, 100),
            batch_size=self.batch_size_train,
            class_mode='categorical')

        # Create a generator to read images from the validation directory
        self.validation_generator = self.datagen.flow_from_directory(
            '../image_generator/geometrical_shapes_using_pillow/Validation',
            target_size=(100, 100),
            batch_size=self.batch_size_val,
            class_mode='categorical')

        # Create a generator to read images from the test directory
        self.test_generator = self.datagen.flow_from_directory(
            '../image_generator/geometrical_shapes_using_pillow/Test',
            target_size=(100, 100),
            class_mode='categorical')

        # Create a simple model
        self.model = Sequential()
        self.model.add(Conv2D(128, kernel_size=(3, 3), activation='relu', input_shape=(100, 100, 3)))
        self.model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
        self.model.add(Conv2D(8, kernel_size=(3, 3), activation='relu'))
        self.model.add(Flatten())
        self.model.add(Dense(2, activation='softmax'))

        # Compile the model
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    def train(self):
        # Train the model
        self.model.fit(
            self.train_generator,
            steps_per_epoch=len(self.train_generator.classes) / self.batch_size_train,
            epochs=1,
            validation_data=self.validation_generator,
            validation_steps=len(self.validation_generator.classes) / self.batch_size_val)

    def evaluate(self):
        # Evaluate the model on test data
        test_loss, test_acc = self.model.evaluate(self.test_generator)
        print("Test accuracy: {:.2f}%".format(test_acc * 100))


# main function to run the model
if __name__ == "__main__":
    model = GeometricalShapesDetectionModel()
    model.train()
    model.evaluate()