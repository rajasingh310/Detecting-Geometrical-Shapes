import random
import os
import shutil
from draw_image_using_pillow import Draw_Geometrical_Shapes

# Create a directory to save the images
directory_name = "geometrical_shapes_using_pillow"

# check if the directory exists
if os.path.exists(directory_name):
    # delete the directory
    shutil.rmtree(directory_name)
    print(f"{directory_name} Deleted!")

# create the new directory
os.mkdir(directory_name)
os.mkdir(directory_name+"/circle_images")
os.mkdir(directory_name+"/no_circle_images")
print(f"{directory_name} Created!")

# Generate images using pillow

for i in range(500):
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
    drawing.image.save(f"geometrical_shapes_using_pillow/circle_images/circle_{str(i+1)}.png")

for i in range(500):
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
    drawing.image.save(f"geometrical_shapes_using_pillow/no_circle_images/no_circle_{str(i+1)}.png")