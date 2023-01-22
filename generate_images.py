import random
import os
import shutil
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
from draw_image_using_pillow import Draw_Geometrical_Shapes

class Generate_Images:

    def __init__(self, resolution_image, background_color):
        # Create a new image with a black background
        self.resolution_image = resolution_image
        self.background_color = background_color
    
    def create_directories(self, directory_name="new_directory"):
        # check if the directory exists
        self.directory_name = directory_name
        if os.path.exists(self.directory_name):
            # delete the directory
            shutil.rmtree(self.directory_name)
            print(f"{self.directory_name} Deleted!")

        # create the new directory
        os.makedirs(self.directory_name+"/train/circle_images")
        os.makedirs(self.directory_name+"/train/no_circle_images")
        os.makedirs(self.directory_name+"/validation/circle_images")
        os.makedirs(self.directory_name+"/validation/no_circle_images")
        os.makedirs(self.directory_name+"/test/circle_images")
        os.makedirs(self.directory_name+"/test/no_circle_images")
        print(f"{self.directory_name} Created!")

# Generate images using pillow
    def generate_images(self, num_images, include_circle=True, images_for="Train"):
        for i in range(num_images):
            # create an instance of Draw_Geometrical_Shapes
            self.drawing = Draw_Geometrical_Shapes(self.resolution_image, self.background_color)

            # create a list of objects of the methods that includes circle
            methods_list = [self.drawing.conics, self.drawing.quadrilateral, self.drawing.line, self.drawing.polygon]
            # shuffle the list of methods
            random.shuffle(methods_list)
            # iterate through the shuffled list
            for method in methods_list:
                if include_circle:
                    method()
                    if method == self.drawing.conics:
                        break
                else:
                    if method != self.drawing.conics:
                        method()

            # Save the image as a PNG file
            if include_circle:
                self.drawing.image.save(self.directory_name+"/"+images_for+f"/circle_images/circle_{str(i+1)}.png")
            else:
                self.drawing.image.save(self.directory_name+"/"+images_for+f"/no_circle_images/no_circle_{str(i+1)}.png")


# Initialize the object
geometrical_shape = Generate_Images(resolution_image=(100, 100), background_color=(0, 0, 0))
# Create a directory to save the images
geometrical_shape.create_directories(directory_name="g")
# Generate images
geometrical_shape.generate_images(num_images=20, include_circle=True, images_for="Validation")