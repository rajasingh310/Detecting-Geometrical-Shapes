import random
import os
import shutil
from draw_image_using_pillow import DrawGeometricalShapes


class GenerateImages:

    def __init__(self, resolution_image, background_color):
        """
        Constructor to initialize the image resolution and background color
        """
        self.resolution_image = resolution_image
        self.background_color = background_color

    def create_directories(self, directory_name="new_directory"):
        """
        Create the directories for the images
        """
        self.directory_name = directory_name
        # Delete the directory if it already exists
        if os.path.exists(self.directory_name):
            shutil.rmtree(self.directory_name)
            print(f"{self.directory_name} Deleted!")

        # Create the new directory
        os.makedirs(self.directory_name)
        print(f"{self.directory_name} Created!")

        os.makedirs(os.path.join(self.directory_name, "Training/circle_images"), exist_ok=True)
        os.makedirs(os.path.join(self.directory_name, "Training/no_circle_images"), exist_ok=True)
        os.makedirs(os.path.join(self.directory_name, "Validation/circle_images"), exist_ok=True)
        os.makedirs(os.path.join(self.directory_name, "Validation/no_circle_images"), exist_ok=True)
        os.makedirs(os.path.join(self.directory_name, "Test/circle_images"), exist_ok=True)
        os.makedirs(os.path.join(self.directory_name, "Test/no_circle_images"), exist_ok=True)

    def generate_images(self, num_images, include_circle=True, images_for="Training"):
        """
        Generate images using pillow
        """
        for i in range(num_images):
            self.drawing = DrawGeometricalShapes(self.resolution_image, self.background_color)
            self.shape_drawing_methods = [
                self.drawing.conics,
                self.drawing.quadrilateral,
                self.drawing.line,
                self.drawing.polygon
            ]
            random.shuffle(self.shape_drawing_methods)

            for method in self.shape_drawing_methods:
                if include_circle:
                    method()
                    if method == self.drawing.conics:
                        break
                else:
                    if method != self.drawing.conics:
                        method()
                    else:
                        break

            # Save the image as a PNG file
            if include_circle:
                self.drawing.image.save(self.directory_name + "/" + images_for + f"/circle_images/circle_{str(i + 1)}.png")
            else:
                self.drawing.image.save(self.directory_name + "/" + images_for + f"/no_circle_images/no_circle_{str(i + 1)}.png")